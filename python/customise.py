import FWCore.ParameterSet.Config as cms

def customize_HLT_trkIter2GlobalPtSeedXX(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")

  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr,
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 4.0 ),
                            VertexCollection = cms.InputTag( 'hltTrimmedPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.05 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )
          
  process.hltIter2PFlowPixelHitDoublets.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr

  process.HLTIterativeTrackingIteration2.replace(
    process.hltIter2PFlowPixelTrackingRegions,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr)
  )

  return process


def customize_HLT_trkIter2GlobalPtSeedXXForBTag(process,ptVal=0.9):

  ptStr = str(ptVal).replace(".","p")
  
  setattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag",
          cms.EDProducer( 'GlobalTrackingRegionWithVerticesEDProducer',
                          RegionPSet = cms.PSet( 
                            useFixedError = cms.bool( True ),
                            nSigmaZ = cms.double( 0.0 ),
                            VertexCollection = cms.InputTag( 'hltFastPVPixelVertices' ),
                            beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
                            useFoundVertices = cms.bool( True ),
                            fixedError = cms.double( 0.2 ),
                            sigmaZVertex = cms.double( 3.0 ),
                            useFakeVertices = cms.bool( False ),
                            ptMin = cms.double( ptVal ),
                            originRadius = cms.double( 0.3 ),
                            precise = cms.bool( True ),
                            useMultipleScattering = cms.bool( False )
                          )
                        )
        )

  process.hltIter2PFlowPixelHitDoubletsForBTag.trackingRegions = 'hltIter2PFlowPixelTrackingRegionsGlobalPtSeed'+ptStr+'ForBTag'

  process.HLTIterativeTrackingIteration2ForBTag.replace(
    process.hltIter2PFlowPixelTrackingRegionsForBTag,
    getattr(process,"hltIter2PFlowPixelTrackingRegionsGlobalPtSeed"+ptStr+"ForBTag")
  )

  return process
