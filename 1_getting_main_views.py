import chimerax.core.commands as chimera
import os
# Define the PDB ID you want to open
pdb_id = "7vs5"


# close previous session
chimera.run(session, "close")

# set chimeraX working directory to the current directory
current_dir = "/home/tony/iGEM/final_presentation"
chimera.run(session, f"cd {current_dir}")

# open the trimmed file and view it
chimera.run(session, "open receptor.pdb")
chimera.run(session, "view")
chimera.run(session, "turn y 50")
chimera.run(session, "turn x -5")
chimera.run(session, "turn z -11")
chimera.run(session, "view")
chimera.run(session, "view name trimmed_view")


# load the PDB file and view it
chimera.run(session, text=f"open {pdb_id}")
chimera.run(session, "view")
chimera.run(session, "turn y 40")
chimera.run(session, "view")
chimera.run(session, "view name 7vs5_view")


# create the full assembly and view it
chimera.run(session, "sym #2 assembly 1 copies false")
chimera.run(session, "color #3 bypolymer")
chimera.run(session, "turn y 90") 
chimera.run(session, "turn z 100")
chimera.run(session, "turn x -85")
chimera.run(session, "view")
chimera.run(session, "view name full_capsid_view")

# save progress
chimera.run(session, "save 1_getting_main_views.cxs")