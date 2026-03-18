#!/usr/bin/python3

# makeTLspec: Take a CTAN component name and make spec snippets for it
#
# Copyright (c) 2023		Tom Callaway <spot@fedoraproject.org>
# Copyright (c) 2013-2016	Tomas Popela <tpopela@redhat.com> (from chromium-latest.py)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import datetime
from optparse import OptionParser
import os
import pathlib
import requests
import sys
import tarfile
import urllib.request, urllib.parse, urllib.error

def dlProgress(count, blockSize, totalSize):
	if (totalSize <= blockSize):
		percent = int(count * 100)
	else:
		percent = int(count * blockSize * 100 / totalSize)
	sys.stdout.write("\r" + "Downloading ... %d%%" % percent)
	sys.stdout.flush()

def license_to_spdx(argument):
	switcher = {
        'Arphic': 'Arphic-1999',
		'lppl1.3c': 'LPPL-1.3c',
		'lppl1.3a': 'LPPL-1.3a',
		'lppl1.3': 'LPPL-1.3c',
		'lppl1.2': 'LPPL-1.2',
		'lppl1.1': 'LPPL-1.1',
		'lppl1.0': 'LPPL-1.0',
		'lppl': 'LPPL-1.3c',
		'apache2': 'Apache-2.0',
		'artistic2': 'Artistic-2.0',
		'bsd': 'BSD',
                'bsd3': 'BSD-3-Clause',
                'fdl': 'GFDL-1.3-or-later',
		'fsl': 'GFSL',
		'gpl2': 'GPL-2.0-or-later',
                'gpl3': 'GPL-3.0-or-later',
                'gpl': 'GPL-1.0-or-later',
                'knuth': 'Knuth',
                'lgpl2.1': 'LPGL-2.1-or-later',
                'lgpl': 'LGPL-2.0-or-later',
                'mit': 'MIT',
                'ofl': 'OFL-1.1',
                'pd': 'LicenseRef-Fedora-Public-Domain',
                'other-free': 'UNKNOWN'
	}
	return switcher.get(argument, "UNKNOWN")

def license_to_fedora(argument):
	switcher = {
		'lppl1.3c': 'LPPL 1.3',
		'lppl1.3': 'LPPL 1.3',
		'lppl1.2': 'LPPL 1.2',
		'lppl1.1': 'LPPL 1.1',
		'lppl1': 'LPPL 1',
		'lppl': 'LPPL',
		'apache2': 'ASL 2.0',
		'artistic2': 'Artistic 2.0',
		'bsd': 'BSD',
		'fdl': 'GFDL',
		'fsl': 'GFSL',
		'gpl2': 'GPLv2',
		'gpl3': 'GPLv3',
		'gpl': 'GPL+',
		'knuth': 'Knuth',
		'lgpl2.1': 'LGPLv2',
		'lgpl': 'LGPLv2+',
		'ofl': 'OFL',
		'pd': 'Public Domain',
		'other-free': 'UNKNOWN'
	}
	return switcher.get(argument, "UNKNOWN")

def remove_file_if_exists(filename):
	if os.path.isfile("./%s" % filename):
		try:
			os.remove(filename)
		except Exception:
			pass

def downloadit(component):
	mirror = "https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet/archive/"
	# mirror = "http://ctan.math.illinois.edu/systems/texlive/tlnet/archive/"
	if options.verbose:
		print("Downloading main tarball for %s..." % component)
	componentfile = component + ".tar.xz"
	componentdocfile = component + ".doc.tar.xz"

	texlivegitdir = str(pathlib.Path.home()) + "/git/texlive"
	try:
		os.chdir(texlivegitdir)
	except OSError:
		print("Could not change to %s... bailing out" % texlivegitdir)
		return

	if (options.clean):
		remove_file_if_exists(componentfile)
		remove_file_if_exists(componentdocfile)

	# Make sure we have not already downloaded the component bits
	for item in [componentfile, componentdocfile]:
		if os.path.isfile(item):
			print("%s already exists!" % item)
		else:
			url = mirror + item
			request = requests.get(url)
			if request.status_code == 200:
				print("Downloading %s" % url)
				info = urllib.request.urlretrieve(url, item, reporthook=dlProgress)[1]
				urllib.request.urlcleanup()
				print("")
			else:
				print('Tarball for %s is not on this mirror.' % item)
				remove_file_if_exists (item)
				# sys.exit(1)

if __name__ == "__main__":
	# We want to be in ~/git/texlive/
	texlivegitdir = str(pathlib.Path.home()) + "/git/texlive"
	sourceslistpath = texlivegitdir + "/sourceslistfile.txt"
	packagespath = texlivegitdir + "/packagesfile.txt"
	fileslistpath = texlivegitdir + "/fileslistfile.txt" 

	mirror = "http://ctan.math.illinois.edu/systems/texlive/tlnet/archive/"

	usage = "usage: %prog [options] CTANcomponent"
	parser = OptionParser(usage)
	parser.add_option("-c", "--clean", action="store_true", help="Re-download sources")
	parser.add_option("-d", "--download", action="store_true", help="Download files fresh")
	parser.add_option("-s", "--startingsourcenum", default="1", help="Starting sourcenum for the sourceslist [default: %default]")
	parser.add_option("-t", "--timestamp", action="store_true", help="add a timestamp to the output files (if any)")
	parser.add_option("-v", "--verbose", action="store_true", help="Tell us what is happening")
	parser.add_option("-w", "--write", action="store_true", help="Write output to files")
	options, args = parser.parse_args()
	if len(args) < 1:
		parser.error("incorrect number of arguments found")

	if options.timestamp:
		now = datetime.now()
		timestamp = now.strftime("%Y%m%d-%H%M%S")
		sourceslistpath = texlivegitdir + "/sourceslistfile-{0:s}.txt".format(timestamp)
		packagespath = texlivegitdir + "/packagesfile-{0:s}.txt".format(timestamp)
		fileslistpath = texlivegitdir + "/fileslistfile-{0:s}.txt".format(timestamp)

	if options.write:
		# Probably want a warning if these are found since they'll be destroyed otherwise.
		sourceslistfile = open(sourceslistpath, "w")
		packagesfile = open(packagespath, "w")
		fileslistfile = open(fileslistpath, "w")
	counter = int(options.startingsourcenum)
	sortedargs = sorted(args)
	for component in sortedargs:
		masterfilelist = []
		masterdirlist = []
		if options.verbose:
			print("Starting SPEC generation for %s..." % component)
		if options.download:
			downloadit(component)

		if "collection" in component:
			if options.verbose:
				print("Component %s appears to be a collection, using strict requires." % component)
			strictreq = True
		else:
			strictreq = False

		# Unpack tarballs if they exist
		componentfile = component + ".tar.xz"
		componentdocfile = component + ".doc.tar.xz"
		sandboxdir = texlivegitdir + "/sandbox"

		if not os.path.exists(sandboxdir):
			os.makedirs(sandboxdir)

		try:
                	os.chdir(sandboxdir)
		except OSError:
			print("Could not change to %s... bailing out" % sandboxdir)
		else:
			if os.path.isfile(texlivegitdir + "/{0:s}".format(componentfile)) or os.path.isfile(texlivegitdir + "/{0:s}".format(componentdocfile)):
				for file in [componentfile, componentdocfile]:
					if os.path.isfile(texlivegitdir + "/{0:s}".format(file)):
						if options.write:
							sourceslistfile.write("Source{0:d}: {1:s}{2:s}\n".format(counter, mirror, file))
							counter += 1
						else:
							print("Source{0:d}: {1:s}{2:s}".format(counter, mirror, file))
							counter += 1

						if options.verbose:
							print("Unpacking {0:s} ...".format(file), end="")
						tar = tarfile.open(texlivegitdir + "/" + file)
						filelist = tar.getnames()
						justdirs = []
						justfiles = []
						for newfile in filelist:
							mypath = pathlib.Path(newfile)
							# we dont want to generate provides for files in doc packages
							if file == componentfile:
								justfiles.append(mypath.name)
							justdirs.append(mypath.parent)
						cleandirs = [str(x) for x in justdirs if not str(x).startswith('tlpkg')]
						# Eliminate dupes
						cleandirs = list( dict.fromkeys(cleandirs) )
						masterdirlist = masterdirlist + cleandirs
						masterfilelist = masterfilelist + justfiles
						tar.extractall()
						tar.close()
						if options.verbose:
							print(" done!")

				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				if options.write:
					packagesfile.write("%package {0:s}\n".format(component))
				else:
					print("%package {0:s}".format(component))
				# Figure out the summary
				for line in f:
					if line.startswith('shortdesc'):
						summarytxt = line.replace('shortdesc ', '')
						if options.write:
							packagesfile.write("Summary: {0:s}\n".format(summarytxt.rstrip()))
						else:
							print("Summary: {0:s}".format(summarytxt.rstrip()))
				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				# Figure out the version
				for line in f:
					if line.startswith('revision'):
						vernum = line.replace('revision ', '')
						if options.write:
							packagesfile.write("Version: svn{0:s}\n".format(vernum.rstrip()))
						else:
							print("Version: svn{0:s}".format(vernum.rstrip()))
				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				# Figure out the license
				license = ''
				for line in f:
					if line.startswith('catalogue-license'):
						license = line.replace('catalogue-license ', '')
						# print(license_to_fedora(license.rstrip()))
						if options.write:
							packagesfile.write("License: {0:s}\n".format(license_to_spdx(license.rstrip())))
						else:
							print("License: {0:s}".format(license_to_spdx(license.rstrip())))

				# Print our universal requires
				if options.write:
					packagesfile.write("Requires: texlive-base texlive-kpathsea\n")
				else:
					print("Requires: texlive-base texlive-kpathsea")

				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				# Print component specific requires ...
				for line in f:
					if line.startswith('depend'):
						require = line.replace('depend ', '')
						require = require.rstrip()
						if not require.endswith('.ARCH'):
							if options.write:
								if strictreq:
									packagesfile.write("Requires: texlive-{0:s}\n".format(require))
								else:
									packagesfile.write("Requires: tex({0:s}.sty)\n".format(require))
							else:
								if strictreq:
									print("Requires: texlive-{0:s}\n".format(require))
								else:
									print("Requires: tex({0:s}.sty)".format(require))

				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				# Package specific provides
				for monkey in sorted(masterfilelist):
					if str(monkey).rstrip().endswith('.sty') or str(monkey).rstrip().endswith('.tex') or str(monkey).rstrip().endswith('.bbx') or str(monkey).rstrip().endswith('.cbx') or str(monkey).rstrip().endswith('.fd') or str(monkey).rstrip().endswith('.cls') or str(monkey).rstrip().endswith('.def') or str(monkey).rstrip().endswith('.map') or str(monkey).rstrip().endswith('.enc') or str(monkey).rstrip().endswith('.bug') or str(monkey).rstrip().endswith('.bg2') or str(monkey).rstrip().endswith('.clo'):
						if options.write:
							packagesfile.write("Provides: tex(" + str(monkey) + ") = %{tl_version}\n")
						else:
							print("Provides: tex(" + str(monkey) + ") = %{tl_version}")

				# spacer between %package and %description
				if options.write:
					packagesfile.write("\n")
				else:
					print("")

				f = open(sandboxdir + '/tlpkg/tlpobj/' + component + '.tlpobj', 'r')
				# Here is where we make the description section for the component.

				if options.write:
					packagesfile.write("%description {0:s}\n".format(component))
				else:
					print("%description {0:s}".format(component))
				for line in f:
					if line.startswith('longdesc'):
						descline = line.replace('longdesc ', '')
						if options.write:
							packagesfile.write(descline.rstrip() + "\n")
						else:
							print(descline.rstrip())
				if options.write:
					packagesfile.write("\n")
				else:
					print("")

				# Here is where we make the files section for the component.
				if options.write:
					fileslistfile.write("%files {0:s}\n".format(component))
					fileslistfile.write("%license {0:s}.txt\n".format(license.rstrip()))
				else:
					print("%files {0:s}".format(component))
					print("%license {0:s}.txt".format(license.rstrip()))
				for x in sorted(masterdirlist):
					if x.startswith('doc'):
						if options.write:
							fileslistfile.write('%doc %{{_texdir}}/texmf-dist/{0:s}\n'.format(x))
						else:
							print('%doc %{{_texdir}}/texmf-dist/{0:s}'.format(x))
					else:
						if options.write:
							fileslistfile.write('%{{_texdir}}/texmf-dist/{0:s}\n'.format(x))
						else:
							print('%{{_texdir}}/texmf-dist/{0:s}'.format(x))
				if options.write:
					fileslistfile.write("\n")
				else:
					print("")
			else:
				print("Component {0:s} not found, maybe retired?".format(component))
	sourceslistfile.close()
	packagesfile.close()
	fileslistfile.close()
	print("That's all folks.")

