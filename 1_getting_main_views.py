import chimerax.core.commands as chimera

trimmed_chains = ["hj", "hk", "hl", "hm", "hn", 
                "ew", "ex", "ey", "fc", "fh",
                "fd", "ls", "lu", "nc"]

# Define the chains of each polymer, from ChimeraX
Major_capsid_protein = "aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd be bf bg bh bi bj bk bl bm bn bo bp bq br bs bt bu bv bw bx by bz ca cb cc cd ce cf cg ch ci cj ck cl cm cn co cp cq cr cs ct cu cv cw cx cy cz da db dc dd de df dg dh di dj dk dl dm dn do dp dq dr ds dt du dv dw dx dy dz ea eb ec ed ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex ey ez fa fb fc fd fe ff fg fh fi fj fk fl fm fn fo fp fq fr fs ft fu fv fw fx fy fz ga gb gc gd ge gf gg gh gi gj gk gl gm gn go gp gq gr gs gt gu gv gw gx gy gz ha hb hc hd"
Capsid_vertex_protein = "he hf hg hh hi hj hk hl hm hn ho"
Small_outer_capsid_protein = "hp hq hr hs ht hu hv hw hx hy hz ia ib ic id ie if ig ih ii ij ik il im in io ip iq ir is it iu iv iw ix iy iz ja jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq jr js jt ju jv jw jx jy jz ka kb kc kd ke kf kg kh ki kj kk kl km kn ko kp kq kr ks kt ku kv kw kx ky kz la lb lc ld le lf lg lh li lj lk ll lm ln lo lp lq lr ls lt lu lv lw lx ly lz ma mb mc md me mf mg mh mi mj mk ml mm mn mo mp mq ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni nj nk nl nm nn no np nq ns nt nu nv nw nx ny nz oa ob oc od oe of og"
# split the string into a list of strings
Major_capsid_protein = Major_capsid_protein.split(" ")
Capsid_vertex_protein = Capsid_vertex_protein.split(" ")
Small_outer_capsid_protein = Small_outer_capsid_protein.split(" ")


# Define the PDB ID you want to open
pdb_id = "7vs5"

# close previous session and clear log
chimera.run(session, "close")
chimera.run(session, "log clear")

# set chimeraX working directory to the current directory
current_dir = "/home/tony/iGEM/final_presentation"
chimera.run(session, f"cd {current_dir}")

# set the background color to something
chimera.run(session, "set bg #FFFFFF")

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

# color the structures
Major_capsid_protein_string = ",".join(Major_capsid_protein)
Capsid_vertex_protein_string = ",".join(Capsid_vertex_protein)
Small_outer_capsid_protein_string = ",".join(Small_outer_capsid_protein)

chimera.run(session, "color #2/" + Major_capsid_protein_string + " hot pink")
chimera.run(session, "color #2/" + Capsid_vertex_protein_string + " cyan")
chimera.run(session, "color #2/" + Small_outer_capsid_protein_string + " light gray")

#  close trimmed file to save memory
chimera.run(session, "close #1")

# create the full assembly and view it
chimera.run(session, "sym #2 assembly 1 copies false")
chimera.run(session, "turn y 90") 
chimera.run(session, "turn z 100")
chimera.run(session, "turn x -85")
chimera.run(session, "view")
chimera.run(session, "view name full_capsid_view")

# create a selection of the trimmed chains
trimmed_chains_string = ",".join(trimmed_chains)
chimera.run(session, "name trimmed_sel #2/" + trimmed_chains_string)

# save progress
chimera.run(session, "save 1_getting_main_views.cxs")


# chimera.run(session, "info polymer")
# chimera.run(session, "log save temp_log.html")
# find a way to output the log to a string