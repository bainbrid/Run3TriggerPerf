import uproot
import numpy as np
import time
import awkward as ak

starttime = time.time()

file = uproot.open("./data/input.root:nano/tree",
                   file_handler=uproot.MultithreadedFileSource,
                   num_workers=100)
outfile = uproot.recreate("./data/slimmed.root")

outfile.mktree("tree", {"B_mass": ("float",(1,))}) #,"Jpsi_mass": ("float", (1,)) })
starttime = time.time()
counter =0
entries=5000
print(file.keys())
lenfinal = 0
for batch in file.iterate(step_size="10 mb", library="ak",filter_name =['JpsiKE_Jpsi_mass_nofit', 'JpsiKE_pi_pdg', 'JpsiKE_B_vprob', 'JpsiKE_B_fls3d', 'JpsiKE_B_mass_nofit','JpsiKE_B_pt','JpsiKE_B_alpha','JpsiKE_e1_pt','JpsiKE_e2_pt','JpsiKE_e1_eta','JpsiKE_e2_eta','JpsiKE_pi_pt','JpsiKE_pi_eta','JpsiKE_B_pvips']):
    print(counter)                                                                                                                                                                                                                                                                                                                                                                                               
    counter+=1
    
    cut = (batch['JpsiKE_Jpsi_mass_nofit'] < 3.2) & (batch['JpsiKE_Jpsi_mass_nofit'] > 2.9) & (np.abs(batch['JpsiKE_pi_pdg']) == 211) & (batch['JpsiKE_B_vprob'] > 0.00) & (batch['JpsiKE_B_fls3d'] > 0. ) & (batch['JpsiKE_B_mass_nofit'] > 4.5 ) &(batch['JpsiKE_B_mass_nofit'] < 6.0 )&(batch['JpsiKE_B_pt'] > 0.0 )&(batch['JpsiKE_B_alpha'] > 0.0 )&(batch['JpsiKE_e1_pt'] >0. )&(batch['JpsiKE_e2_pt'] > 0. )&(np.abs(batch['JpsiKE_e1_eta']) <1.3)&(np.abs(batch['JpsiKE_e2_eta']) < 1.3 )&(batch['JpsiKE_pi_pt'] > 4.0)&(np.abs(batch['JpsiKE_pi_eta'])<200.)
    
    newstuff = batch["JpsiKE_B_mass_nofit", cut]
    bmassvalues = (ak.flatten(newstuff, axis=1))
    bmassvalues = [[i] for i in bmassvalues]
    lenfinal += len(bmassvalues)
    for start in range(0, len(bmassvalues),entries):
        outfile["tree"].extend({"B_mass": bmassvalues[start: start + entries]})#,"Jpsi_mass": jpsistuff[start: start + entries]})
    
print(f"entries per basket {entries}, time {time.time() - starttime}")
print("lenfinal",lenfinal)
