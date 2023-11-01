import chimerax.core.commands as chimera

# set chimeraX working directory to the current directory
current_dir = "/home/tony/iGEM/final_presentation"
chimera.run(session, f"cd {current_dir}")

# read in the saved session
chimera.run(session, "open 1_getting_main_views.cxs")
chimera.run(session, "show all")
chimera.run(session, "hide #2 models")
chimera.run(session, "view full_capsid_view")

# start recording
chimera.run(session, "movie record")

# roll the structure for n cycles with m degree per frame
cycles = 5 # default 2
degree_per_frame = 12 # default 4
total_frames = cycles * 360 // degree_per_frame
chimera.run(session, f"roll y {degree_per_frame} {total_frames}")
chimera.run(session, f"wait {total_frames}")


# go to the default view of 7vs5
total_frames = 50
chimera.run(session, f"fly {total_frames} start 7vs5_view")
chimera.run(session, f"wait {total_frames}")

# hide big capsid structure
total_frames = 50
chimera.run(session, "show #2 models")
chimera.run(session, f"crossfade {total_frames}; hide #1 models")
chimera.run(session, f"wait {total_frames}")

# just wait
total_frames = 25
chimera.run(session, f"wait {total_frames}")


# zoom in to the trimmed structure
total_frames = 50
chimera.run(session, f"fly {total_frames} start trimmed_view")
chimera.run(session, f"wait {total_frames}")

# hide other parts of the structure
total_frames = 50
chimera.run(session, f"crossfade {total_frames}; hide ~trimmed_sel")
chimera.run(session, f"wait {total_frames}")

# just wait
total_frames = 25
chimera.run(session, f"wait {total_frames}")


# add the binder
chimera.run(session, "open binder.pdb")
# chimera.run(session, "hide #3")

# set intial position to the binder
binder_displacement = 760
chimera.run(session, f"move z {binder_displacement} models #3")

# draw surface of the receptor
chimera.run(session, "show trimmed_sel surface")

# color the binder
chimera.run(session, "show #3 atoms")
chimera.run(session, "style #3 sphere")
chimera.run(session, "color #3 conflower blue")
# chimera.run(session, "wait 1")


# let the binder move to the receptor
total_frames = 100
for _ in range(total_frames):
    chimera.run(session, f"move z -{binder_displacement / total_frames} models #3")
    chimera.run(session, f"wait 1")

# just wait
total_frames = 25
chimera.run(session, f"wait {total_frames}")

# hide the binder
total_frames = 25
chimera.run(session, f"crossfade {total_frames};hide #3 atoms; show #3 cartoon; transparency #3 50 target all")
chimera.run(session, f"wait {total_frames}")


# zoom in to the binder
total_frames = 50
chimera.run(session, f"select trimmed_sel")
chimera.run(session, f"fly {total_frames} start binder_view")
chimera.run(session, f"wait {total_frames}")

# mark the zone around the binder
total_frames = 50
max_radius = 5
for i in range(total_frames+1, 0, -1):
    chimera.run(session, f"color zone sel near #3 distance {max_radius/i}")
    chimera.run(session, f"wait 1")

# just wait
total_frames = 50
chimera.run(session, f"wait {total_frames}")

# stop recording
chimera.run(session, "movie encode test.mp4")