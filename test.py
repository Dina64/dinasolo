arser = argparse.ArgumentParser(description="Simple password cracker. "+ 
	"Only a proof-of-concept for educational purposes. "+
	" See github.com/mthambipillai/password-cracker for the full code and documentation.")
parser.add_argument("hash", help="SHA256 hash of the password to crack.")
parser.add_argument("method",
	help="Cracking method to use. Possible values are : brute_force, dict, dict_repl, targeted. ")
parser.add_argument("-l", "--length_max", type=int, default=5,
	help="Maximum password length in 'brute_force' method. Default is 5.")
parser.add_argument("-d", "--dictionary", default="",
	help="File name of the dictionary to use in 'dict' or 'dict_repl' methods.")
parser.add_argument("-w", "--words", default="",
	help="List of words separated by commas. To be used as input to the 'targeted' method.")
parser.add_argument("-r", "--replacements", default="",
	help="List of replacements separated by commas. To be used as input to the 'dict_repl' method. "+
	"Each replacement of a char 'o' by a char 'n' must be written 'o/n'.")
args = parser.parse_args()

if(args.method=="brute_force"):
	bruteforce_attack(args.hash, args.length_max)
elif(args.method=="dict"):
	if(args.dictionary==""):
		print("Method 'dict' requires argument 'dictionary'")
		quit()
	dictionary_attack(args.hash, args.dictionary)
elif(args.method=="dict_repl"):
	if(args.dictionary==""):
		print("Method 'dict_repl' requires argument 'dictionary'")
		quit()
	if(args.replacements==""):
		print("Method 'dict_repl' requires argument 'replacements'")
		quit()
	replacements = map(lambda r: r.split("/"), args.replacements.split(","))
	dict_attack_with_replacements(args.hash, args.dictionary, replacements)
elif(args.method=="targeted"):
	if(args.words==""):
		print("Method 'targeted' requires argument 'words'")
		quit()
	words_set = set(args.words.split(","))
	targeted_attack(args.hash, words_set)
else:
	print("Cracking method '"+args.method+"' doesn't exist.")
	quit()

print("Failed to crack the password with this method and these parameters.")				
