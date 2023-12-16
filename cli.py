from pixeljoint.pixeljoint import Pixeljoint
import argparse

def main():
	"""
	This function is responsible for the CLI part
	of the pixeljoint project.
	"""
	parser = argparse.ArgumentParser(description='CLI for managing the pixeljoint scraper.')

	parser.add_argument('-a', '--archive', required=True, help='The archive to keep track of downloads.')
	parser.add_argument('-o', '--output', required=True, help='The download output folder.')
	parser.add_argument('profile_list', help='Text file containing a list of pixeljoint profiles.')

	args = parser.parse_args()

	pj = Pixeljoint(args.output, args.profile_list, args.archive)
	pj.start()

if __name__ == "__main__":
	main()