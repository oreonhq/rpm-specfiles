%global source0_hash 2d1c2cb96ee7e44064c5f6c9692d1f886772dbaa7ec0d200e9254b134daabbad

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     templates-parser
%global upstream_version  26.0.0
%global upstream_commit   cc94ff9833cfe776d462b490aac9727b623742c8

Name:           templates_parser
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        An Ada library for parsing templates

License:        GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception
# The license is GPLv3+ with either GCC or GNAT runtime exception.
#
# OPEN ISSUE: What are the licenses of the manpages? Can't find a "Debian
# contributors license" (or alike).

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

# Manpages from Debian package
Source1:        templates2ada.1
Source2:        templatespp.1

BuildRequires:  gcc-gnat gprbuild make sed
BuildRequires:  fedora-gnat-project-common
BuildRequires:  xmlada-devel

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Templates Parser is the templates engine of the Ada Web Server. It is \
designed to parse files and replace some specific tags in these files \
with some specified values.

%description %{common_description_en}

#################
## Subpackages ##
#################

%package devel
Summary:        Development files for Templates Parser
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       xmlada-devel
Recommends:     %{name}-doc
Recommends:     %{name}-tools

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use Templates Parser.

%package doc
Summary:        Documentation for Templates Parser
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Fonts are required by the Read the Docs Sphinx theme.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF.

%package tools
Summary:        Tools based on Templates Parser
License:        GPL-3.0-or-later

%description tools %{common_description_en}

This package contains the tools templates2ada and templatespp. Templates2ada is
a tool that will generate a set of Ada packages from a template file.
Templatespp is a pre-processor based on Templates Parser. It is generally used
from scripts to process files and generate other files.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# XML/Ada is installed.
cp config/tp_xmlada_installed.gpr tp_xmlada.gpr

# The makefile must be edited to correct the version number because docs/conf.py
# reads Makefile directly to get VERSION.
sed --regexp-extended --in-place \
    '--expression=s|^( *VERSION[ 	]*[:?]?=[ 	]*).*$|\1%{version}|' \
    Makefile

###########
## Build ##
###########

%build

# Options (project variables) for Templates Parser.
%global tp_options -XVERSION=%{version} \\\
                   -XPRJ_BUILD=Release \\\
                   -XPRJ_TARGET=Linux \\\
                   -XTP_TASKING=Standard_Tasking \\\
                   -XTP_XMLADA=Installed \\\
                   -XLIBRARY_TYPE=relocatable \\\
                   -XXMLADA_BUILD=relocatable

# Build the library and tools.
gprbuild %{GPRbuild_flags} %{tp_options} -P templates_parser.gpr
gprbuild %{GPRbuild_flags} %{tp_options} -P tools/tools.gpr -cargs -fPIE

# Make the documentation. Additional makefile variables are required
# by the GPRbuild project of the examples that need to be built before
# the documentation can be compiled. Compiler switch "-fPIE" is
# required as hardened builds are enabled for this package.
make -C docs html latexpdf \
     GPRBUILD="gprbuild -cargs -fPIE -gargs" \
     PRJ_TARGET=Linux PRJ_BUILD=Release \
     TARGET=$(gcc -dumpmachine) VERSION=%{version}

#############
## Install ##
#############

%install

# Install the library and tools.
%{GPRinstall} %{tp_options} --no-build-var -P templates_parser.gpr
%{GPRinstall} %{tp_options} --mode=usage -P tools/tools.gpr

# Fix up the symlink.
ln --symbolic --force lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so

# Install the man pages.
mkdir --parents %{buildroot}%{_mandir}/man1
cp --preserve=timestamps %{SOURCE1} %{buildroot}%{_mandir}/man1/
cp --preserve=timestamps %{SOURCE2} %{buildroot}%{_mandir}/man1/

# Copy the examples.
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/templates.tads %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/all_urls.thtml %{buildroot}%{_pkgdocdir}/examples

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%{_libdir}/lib%{name}-%{version}.so

%files devel
%{_GNAT_project_dir}/%{name}.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv

%files tools
%{_bindir}/templates2ada
%{_bindir}/templatespp
%attr(644,-,-) %{_mandir}/man1/*.1*

###############
## Changelog ##
###############

%changelog
%autochangelog
