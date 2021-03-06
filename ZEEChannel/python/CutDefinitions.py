import FWCore.ParameterSet.Config as cms
import copy
import string

import OSUDisplacedHiggs.Configuration.objectDefinitions as objectDefs

##########################################################################

# BEGIN JET CUTS

jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 0")
    )

jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

jet_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 0")
    )

jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )

##########################################################################

# BEGIN ELECTRON CUTS

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron ECAL crack veto")
    )

electron_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2")
    )

electron_pt_42_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 42"),
    numberRequired = cms.string(">= 2")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_id_alias
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_iso_alias
    )

electron_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_antiiso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_antiiso_alias
    )


electron_2electron_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("extra electron veto")
    )

diElectron_invElectron_Z_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("abs(invMass(electron,electron) - 91.2) < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_electron - mass_Z) < 10")
    )

# diElectron Invariant Mass > 81.2GeV
diElectron_invMass_above81_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass (electron,electron) > 81.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass > 81.2GeV")
    )

# diElectron Invariant Mass < 101.2GeV
diElectron_invMass_below101_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass (electron,electron) < 101.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass < 101.2GeV")
    )

# electron d0 < 100 microns
electron_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 100 mum")
    )

# electron 100 < d0 < 200 microns
electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100 & " + "10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron 100 < d0 < 200 mum")
    )

# electron d0 > 100 microns
electron_d0_above100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 > 100 mum")
    )

# electron d0 < 200 microns
electron_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 200 mum")
    )

##########################################################################

# BEGIN ELECTRON-JET CUTS

electronjet_deltaR_veto = cms.PSet(
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )
