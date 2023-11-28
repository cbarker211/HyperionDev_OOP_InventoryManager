Capstone 4 - Nike Warehouse Inventory Manager 

-------------- Project Description --------------

This program was created for Compulsory Task 1 of Task 32 in the Software Engineering Bootcamp by HyperionDev. The program manages the inventory for a Nike warehouse, taking advantage of object orientated programming. The user can view the inventory, add and restock items, and view highly stocked items for sale.

--------------- Table of Contents ---------------

Section.......................................Line

Installation................................15

Usage..........................................20

Credits.........................................42

----------------- Installation ------------------

To install this project, simply copy the inventory.py python script, and the inventory.txt text file into the same working directory.
To run this program, you should have Python installed on your machine. For more information visit https://www.python.org/downloads/.

--------------------- Usage ---------------------

Upon running the script, the data from inventory.txt will be automatically loaded into the program, and a menu will appear.

To read additional data from the 'inventory.txt' file, and append it onto the exisiting inventory, please enter 'ra'. This is useful where multiple inventories must be imported.

To read a separate set of data from a different 'inventory.txt' file, and overwrite the existing inventory, please enter 'ro'. This is useful for working with separate inventories individually.

To add a new shoe to the inventory, please enter 'as'. Please note, the country must be a valid exisiting country, the product code must be a valid 5 digit integer without the 'SKU' prefix, and the product cost and quantities must be positive numbers. This option will update the shoe list within the program, and add the new shoe to the 'inventory.txt' file. It will create the file if necessary, includuing adding the headerline to an empty file. 

To view a table of all shoes, please enter 'va'. A screenshot of an example table is included in file 'va_table.png'.

To restock the shoe with the lowest quantity, please enter 'rs'. The program will display the shoe with the lowest quantity, and ask the user if they want to restock the item. If there are multiple shoes with the same minimum quantity, the user will be asked to choose which shoe to restock. If the user chooses to restock the item, the user will be asked for the new quantity (must be a positive integer).

To search for a shoe using the product code, choose 'ss', and enter the product code without the SKU prefix. The program will then search the shoe list for the correct product and display the details to the user.

To view a table of the value per item for all shoes, please enter 'vp'. A screenshot of an example table is included in file 'vp_table.png'.

To view the shoe or shoes with the highest quantity, choose 'hq'. The program will list these items as for sale.

Finally, to exit the program choose 'e'.

-------------------- Credits --------------------

Thanks to HyperionDev for the instructions to complete this task.
