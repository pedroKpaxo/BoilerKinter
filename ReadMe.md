# A boiler plate for a tkinter MVC style Project

The objective of this project is to provide a fast boiler plate for a  MVC style tkinter project!

# Table of Contents

- [Model](#Model)
- [View](#View)
- [Controller](#Controller)
- [Database](#Database)

# Model

Here you can run all your logic, process everything to feed your database and more.
The model module can be expanded to all your needs.
It comes with a SQLAlchemy pre configured module, that can be found on [Database](#Database).

# View

Here is were you run all your GUI code.
</br> Importing widgtes from the widgets folder, and packing or griding them inside your <strong>mainview.py</strong> file.

- [MainView](#MainView)
- [Frames](#Frames)
- [Widgets](#Widgets)

## MainView

[MainView File](blank_app/BoilerView/mainview.py)

Here all the widgets are imported in a simple manner, and gets packed inside a MainApp that is a TopLevel tk.TK() element.

## Frames

[Frames Module](blank_app/BoilerView/Widgets/Frames)

On this module you can find some pre built frames, with organized layouts inside them, that can be modified and expanded according to your needs.
Once you got all your frames working, you can import them in the [Widgets](#Widgets) module, and them import them into the mainview.py module.

## Widgets

[Widgets Module](blank_app/BoilerView/Widgets)

On this module you can find some pre built widgets that inherits from the Frames module, and them gets expanded.

Check out our [Layout](blank_app/BoilerView/Widgets/layouts.py) that contains frames and buttons from the [Frames](#Frames) module.


# Database

Here you can find a pre-configured module using SQLAlchemy.

- The config.py file holds all the database configuration.
- The database.py holds the main object that runs all the logic.
- The Models module holds all the models and database logic.

