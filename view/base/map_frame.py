from tkinter import Frame, ttk
from tkinter import BOTH
from tkintermapview import TkinterMapView
from AGP.text_processor.utils.console import console
from AGP.main_utils.timeit import measure

start_coords = (-19.42381, -39.09992)


class MapFrame(ttk.Frame):

    def __init__(self, container: Frame):
        super().__init__(container)
        self.config(borderwidth=2, relief="groove")

        self.map = TkinterMapView(self)
        self.map.set_position(*start_coords)
        self.map.set_zoom(8)
        # google satellite
        self.map.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",  # noqa
                                 max_zoom=22)
        self.map.pack(expand=True, fill=BOTH)
        self.toggled_values = []

    @property
    def marker_list(self):
        return self.map.canvas_marker_list

    def set_markers(self, lat_long: list[tuple[float, float, str]]):
        for p in lat_long:
            marker = self.map.set_marker(
                deg_x=p[0],
                deg_y=p[1],
                text=p[2],
                font=('Helvetica', 8),

                command=lambda x: self.emmit_controller(m_value=marker.text)
            )

    def set_markers_near_wells(self, lat_long: list[tuple[str, float, list[float, float]]]):  # noqa
        for p in lat_long:
            marker = self.map.set_marker(
                marker_color_outside='#09ad8f',
                deg_x=p[2][0],
                deg_y=p[2][1],
                text=p[0],
                font=('Helvetica', 8),
                command=lambda x: self.emmit_controller(m_value=marker.text)
            )

    def clean_markers(self, *args):

        while self.marker_list:
            for marker in self.marker_list:
                marker.delete()
        return

    def clear_polygons(self, pol):
        while self.map.canvas_polygon_list:
            for p in self.map.canvas_polygon_list:
                p.delete()
        return

    def emmit_controller(self, m_value, *args):
        self.toggled_values.append(m_value)
        self.map.event_generate('<<MARKER_CLICK>>')
