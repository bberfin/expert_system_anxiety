from engine.inference import Inference

# knowledgeBaseFile = "./data/birds/knowledge.json"
# clauseBaseFile = "./data/birds/clause.json"
#
# inferenceEngine = Inference()
# inferenceEngine.startEngine(knowledgeBaseFile,
#                             clauseBaseFile,
#                             verbose=True,
#                             method=inferenceEngine.BACKWARD)

# # for disease inference
knowledgeBaseFile = "static\jsonFiles\knowledge.json"
clauseBaseFile = "static\jsonFiles\clause.json"

inferenceEngine = Inference()
inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.FORWARD)
