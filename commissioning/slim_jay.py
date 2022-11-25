import awkward as ak
import numpy as np
import time
import uproot

# Time it
starttime = time.time()

# Input ntuple
file_input = uproot.open("./input/ntuples/jay/LowMassQsquared20220819.root:nano/tree",
                         file_handler=uproot.MultithreadedFileSource,
                         num_workers=100)

file_output = uproot.recreate("./output/slimmed/slimmed.root")
file_output.mktree("tree", {"B_mass": ("float",(1,))}) #,"Jpsi_mass": ("float", (1,)) })

ibatch=0
entries=5000
bmass_nvalues=0
bmass_values=[]

branches_used = ['JpsiKE_Jpsi_mass_nofit',
                 'JpsiKE_pi_pdg',
                 'JpsiKE_B_vprob',
                 'JpsiKE_B_fls3d',
                 'JpsiKE_B_mass_nofit',
                 'JpsiKE_B_pt',
                 'JpsiKE_B_alpha',
                 'JpsiKE_e1_pt',
                 'JpsiKE_e2_pt',
                 'JpsiKE_e1_eta',
                 'JpsiKE_e2_eta',
                 'JpsiKE_pi_pt',
                 'JpsiKE_pi_eta',
                 'JpsiKE_B_pvips']

print()
print("Available branches",file_input.keys())
print("Branches used",branches_used)
for batch in file_input.iterate(step_size="10 mb",
                                library="ak",
                                filter_name=branches_used):
    print(ibatch)
    ibatch+=1

    cut = (
        #(batch['JpsiKE_Jpsi_mass_nofit'] < 3.2) & (batch['JpsiKE_Jpsi_mass_nofit'] > 2.9)
        (batch['JpsiKE_Jpsi_mass_nofit'] < 2.45) & (batch['JpsiKE_Jpsi_mass_nofit'] > 1.05)
    & (np.abs(batch['JpsiKE_pi_pdg']) == 211)
    & (batch['JpsiKE_B_vprob'] > 0.00)
    & (batch['JpsiKE_B_fls3d'] > 0. )
    & (batch['JpsiKE_B_mass_nofit'] > 4.5 )
    & (batch['JpsiKE_B_mass_nofit'] < 6.0 )
    & (batch['JpsiKE_B_pt'] > 0.0 )
    & (batch['JpsiKE_B_alpha'] > 0.0 )
    & (batch['JpsiKE_e1_pt'] >0. )
    & (batch['JpsiKE_e2_pt'] > 0. )
    & (np.abs(batch['JpsiKE_e1_eta']) <1.3)
    & (np.abs(batch['JpsiKE_e2_eta']) < 1.3 )
    & (batch['JpsiKE_pi_pt'] > 4.0)
    & (np.abs(batch['JpsiKE_pi_eta'])<200.))

    entries_skimmed = batch["JpsiKE_B_mass_nofit", cut]
    bmass_values = (ak.flatten(entries_skimmed, axis=1))
    bmass_values = [[i] for i in bmass_values]
    bmass_nvalues += len(bmass_values)
    for start in range(0, len(bmass_values),entries):
        file_output["tree"].extend({"B_mass": bmass_values[start: start + entries]})#,"Jpsi_mass": jpsistuff[start: start + entries]})

print(f"entries per basket {entries}, time {time.time() - starttime}")
print(f"Number of entries on bmass branch: {bmass_nvalues}")
