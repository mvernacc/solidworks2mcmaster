SolidWorks BOM to McMaster
==========================

My labmates and I frequently uses McMaster to buy components for experimental apparatuses that we have designed using SolidWorks CAD. We find that putting together a McMaster shopping cart from the CAD bill-of-materials is tedious and sometimes error-prone.

This repo contains scripts to auto-generate a McMaster order from a SolidWorks BOM.

## How to use

Whenever I download a CAD model from McMaster, I put "McMaster-###" in the filename, where "###" is the McMaster part number. This script looks for that string in the filename, so you must use this naming scheme.

Steps:
  1. In soldiworks, create a drawing of your assembly.
  2. Add a bill of materials to the drawing. The bill of materials must have a `SW-File Name(File Name)` column and a `QTY.` column. you can use the BOM template file `mcmaster_order_bom_template.sldbomtbt`.
  3. Save the BOM as a csv file.
  4. Run `python sldbom2mcmaster.py bom.csv`, where `bom.csv` is the CSV file you jsut exported.
  5. Open [mcmaster.com](https://www.mcmaster.com/) in a web browser. Click "Order", then "Paste products and quantities".
  6. Copy and paste the product numbers and quantities from your terminal into the McMaster website.
  7. Check the quantities after you build your order. Many McMaster products are sold by the pack, not by "each", and this program does not know how many items are in a pack.


## Legal

McMaster is a trademark of the McMaster-Carr Supply Company and SolidWorks is a trademark of Dassault Systemes SE. Neither the McMaster-Carr Supply Company nor Dassault Systemes SE are affiliated with or endorse this software.
