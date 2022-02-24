import selfies as sf
import pandas as pd
from colorama import Fore, Style

###########################################################

class StringFormatterChemistry:
	def __init__(self, S):
		self.SELFIES = S
		self.ELEMENTS = ['C', 'O', 'N', 'Cl', 'H', 'F']
	
	def colorize(self): #color codes elements for clarity
		output = "" #rebuild original string with colors
		for character in self.SELFIES:
			if character not in self.ELEMENTS:
				output += character
			else: #is an element so needs to be colorized
				if character == 'C':
					output += (Style.BRIGHT + Fore.YELLOW + character + Fore.RESET)
				elif character == 'O':
					output += (Style.BRIGHT + Fore.RED + character + Fore.RESET)
				elif character == 'N':
					output += (Style.BRIGHT + Fore.BLUE + character + Fore.RESET)
				elif character == 'Cl':
					output += (Style.BRIGHT + Fore.GREEN + character + Fore.RESET)
				elif character == 'H':
					output += (Style.BRIGHT + Fore.LIGHTBLACK_EX + character + Fore.RESET)
				elif character == 'F':
					output += (Style.BRIGHT + Fore.MAGENTA + character + Fore.RESET)
		return output

###########################################################

original_smiles = "CC(C)O" #original
encoded_selfies = sf.encoder(original_smiles) #encode to selfies
decoded_smiles = sf.decoder(encoded_selfies) #decode to smiles

smiles_df = pd.read_csv("TEST.csv")
smiles_dataset = smiles_df['smiles'].values.tolist()
selfies_dataset = []

for i in range(len(smiles_dataset)):
	SFC = StringFormatterChemistry(sf.encoder(smiles_dataset[i]))
	S = SFC.colorize()
	if i % 1009 == 0: print(S)
	selfies_dataset.append(S)
