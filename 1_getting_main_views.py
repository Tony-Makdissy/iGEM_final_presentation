import chimerax.core.commands as chimera

trimmed_chains = ["hj", "hk", "hl", "hm", "hn", 
                "ew", "ex", "ey", "fc", "fh",
                "fd", "ls", "lu", "nc"]

# Define the PDB ID you want to open
pdb_id = "7vs5"

# close previous session and clear log
chimera.run(session, "close")
chimera.run(session, "log clear")

# set chimeraX working directory to the current directory
current_dir = "/home/tony/iGEM/final_presentation"
chimera.run(session, f"cd {current_dir}")

# set the background color to something
chimera.run(session, "set bg #D8BFD8")

# open the trimmed file and view it
chimera.run(session, "open receptor.pdb")
chimera.run(session, "view")
chimera.run(session, "turn y 50")
chimera.run(session, "turn x -5")
chimera.run(session, "turn z -11")
chimera.run(session, "view")
chimera.run(session, "view name trimmed_view")

# open the binder file and view it
chimera.run(session, "open binder.pdb")
chimera.run(session, "view #2")
chimera.run(session, "turn y 20")
chimera.run(session, "view name binder_view")

# close binder to save memory
chimera.run(session, "close #2")

# load the PDB file and view it
chimera.run(session, text=f"open {pdb_id}")
chimera.run(session, "view")
chimera.run(session, "turn y 40")
chimera.run(session, "view")
chimera.run(session, "view name 7vs5_view")

# close trimmed file to save memory
chimera.run(session, "close #1")

# create the full assembly and view it
chimera.run(session, "sym #2 assembly 1 copies false")
chimera.run(session, "turn y 90") 
chimera.run(session, "turn z 100")
chimera.run(session, "turn x -85")
chimera.run(session, "view")
chimera.run(session, "view name full_capsid_view")

# color the structures
chimera.run(session, "color #1 bypolymer")
chimera.run(session, "color #2 bypolymer")

# create a selection of the trimmed chains
trimmed_chains_string = ",".join(trimmed_chains)
chimera.run(session, "name trimmed_sel #2/" + trimmed_chains_string)

# save progress
chimera.run(session, "save 1_getting_main_views.cxs")


# chimera.run(session, "info polymer")
# chimera.run(session, "log save temp_log.html")
# find a way to output the log to a string