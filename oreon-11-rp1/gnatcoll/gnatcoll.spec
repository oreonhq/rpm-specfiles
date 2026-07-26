%global source0_hash b1fdda9803277636366780c23fdc727e5b8a730008bcbfd0c721779659399a54

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gnatcoll-core
%global upstream_version  26.0.0
%global upstream_commit   8e270f83719d4284782a965edd80246be15b949b

Name:           gnatcoll
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        The GNAT Components Collection
Summary(sv):    GNAT Components Collection

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND CC-BY-3.0
# The license is GPLv3+ with the GCC runtime exception, except for:
# - minimal/src/getRSS.c : CC-BY-3.0

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora-specific] Remove unnecessary redirection.
Patch:          %{name}-core-fix-html-dir-indirection.patch
# Adjust a pathname in the manual, replacing the Adacore-specific pathname with
# the FHS-compliant pathname where this package installs the examples:
Patch:          %{name}-core-doc-examples-dir.patch
# Use 'gnatcoll_core.gpr' and 'gnatcoll_projects.gpr' instead of 'gnatcoll.gpr'
# in the examples.
Patch:          %{name}-core-refine-dependencies-gnatcoll.patch
# [GCC 15.2.1] Fix unsupported use of the Access attribute.
Patch:          %{name}-core-fix-base64-coder-example.patch

BuildRequires:  gcc-gnat gprbuild make sed
BuildRequires:  fedora-gnat-project-common

BuildRequires:  libgpr-devel
BuildRequires:  xmlada-devel

BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

# The package "gnatcoll" is a metapackage that pulls in all the binary library
# packages to prevent problems when Fedora is upgraded:
Requires:       gnatcoll-core gnatcoll-gmp gnatcoll-iconv
Requires:       gnatcoll-readline gnatcoll-syslog
Requires:       gnatcoll-sql gnatcoll-sqlite gnatcoll-postgres gnatcoll-xref
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%global common_description_en \
The GNAT Components Collection is a library of general-purpose packages that \
are part of the GNAT technology. The components complement the predefined Ada \
and GNAT libraries and deal with a range of common programming issues \
including string and text processing, memory management, and file handling.

%global common_description_sv \
GNAT Components Collection är ett bibliotek med universalpaket som ingår i \
GNAT-sviten. Komponenterna kompletterar adas och GNATs fördefinierade \
bibliotek, och löser diverse vanliga programmeringsproblem såsom sträng- och \
textbehandling, minneshantering och filhantering.

%description %{common_description_en}

Gnatcoll has been divided into separate modules. The gnatcoll package pulls in
the binaries of all the modules to prevent problems when Fedora is upgraded.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description -l sv %{common_description_sv}

Gnatcoll har delats upp i skilda moduler. Paketet gnatcoll drar in alla
modulernas binärfiler för att undvika problem när Fedora uppgraderas.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.

#################
## Subpackages ##
#################

%package devel
Summary:        Development metapackage for the GNAT Components Collection
Summary(sv):    Metapaket för programmering med GNAT Components Collection
Requires:       gnatcoll-core-devel gnatcoll-bindings-devel gnatcoll-db-devel
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%description devel %{common_description_en}

Gnatcoll has been divided into separate modules. The gnatcoll-devel package
pulls in the development packages of all the modules to prevent problems when
Fedora is upgraded.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv %{common_description_sv}

Gnatcoll har delats upp i skilda moduler. Paketet gnatcoll-devel drar in alla
modulernas programmeringspaket för att undvika problem när Fedora uppgraderas.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.

%package core
Summary:        The GNAT Components Collection – core packages
Summary(sv):    GNAT Components Collection – centrala paket
Obsoletes:      gnatcoll-core < 2:25.0.0
# Self-obsoleting is necessary to pull in gnatcoll-projects on upgrade.
# This Obsoletes tag shall be kept at least in Fedora 42 and 43.

%description core %{common_description_en}

The gnatcoll-core package contains the core module of the GNAT Components
Collection.

%description core -l sv %{common_description_sv}

Paketet gnatcoll-core innehåller den centrala modulen i GNAT Components
Collection.

%package core-devel
Summary:        Development files for the GNAT Components Collection – core packages
Summary(sv):    Filer för programmering med GNAT Components Collection – centrala paket
Requires:       gnatcoll-core%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     gnatcoll-core-doc
Suggests:       gnatcoll-bindings-devel gnatcoll-db-devel
# FIXME: We hope to remove the metapackages some day. What shall be done with
# this Suggests tag then?
Obsoletes:      gnatcoll-core-devel < 2:25.0.0
# Self-obsoleting is necessary to pull in gnatcoll-projects-devel on upgrade.
# This Obsoletes tag shall be kept at least in Fedora 42 and 43.

%description core-devel %{common_description_en}

The gnatcoll-core-devel package contains source code and linking information for
developing applications that use the GNAT Components Collection core packages.

%description core-devel -l sv %{common_description_sv}

Paketet gnatcoll-core-devel innehåller källkod och länkningsinformation som
behövs för att utveckla program som använder GNAT Components Collections
centrala paket.

%package -n gnatcoll-projects
Summary:        The GNAT Components Collection – GNAT project handling
Summary(sv):    GNAT Components Collection – GNATprojekthantering
Obsoletes:      gnatcoll-core < 2:25.0.0
# This subpackage was split out in version 25 and shall be pulled in on upgrade
# from earlier versions. It shall not be pulled in again on further upgrades.
# This Obsoletes tag shall be kept at least in Fedora 42 and 43.

%description -n gnatcoll-projects
This is the GNAT project component of the GNAT Components Collection. It
provides a high-level API to manipulate GNAT project files.

%description -n gnatcoll-projects -l sv
Detta är GNATprojektkomponenten i GNAT Components Collection. Den
tillhandahåller ett högnivågränssnitt för att hantera GNATprojektfiler.

%package -n gnatcoll-projects-devel
Summary:        Development files for the GNAT Components Collection – GNAT project handling
Summary(sv):    Filer för programmering med GNAT Components Collection – GNATprojekthantering
Requires:       gnatcoll-projects%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-core-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       libgpr-devel xmlada-devel
# Documentation and examples for gnatcoll-projects are included in gnatcoll-core-doc.
Recommends:     gnatcoll-core-doc
Obsoletes:      gnatcoll-core-devel < 2:25.0.0
# This subpackage was split out in version 25 and shall be pulled in on upgrade
# from earlier versions. It shall not be pulled in again on further upgrades.
# This Obsoletes tag shall be kept at least in Fedora 42 and 43.

%description -n gnatcoll-projects-devel
This package contains source code and linking information for developing
applications that use the GNAT project component of the GNAT Components
Collection. It provides a high-level API to manipulate GNAT project files.

This package also contains the backward-compatible project file gnatcoll.gpr.

%description -n gnatcoll-projects-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder GNATprojektkomponenten i GNAT Components
Collection. Den tillhandahåller ett högnivågränssnitt för att hantera
GNATprojektfiler.

Detta paket innehåller också den bakåtkompatibla projektfilen gnatcoll.gpr.

%package core-doc
Summary:        Documentation for the GNAT Components Collection – core packages
Summary(sv):    Dokumentation till GNAT Components Collection – centrala paket
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.
# The example code is licensed under GPLv3+ with the GCC runtime exception.
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Fonts are required by the Read the Docs Sphinx theme.
Provides:       gnatcoll-doc = %{epoch}:%{version}-%{release}
Obsoletes:      gnatcoll-doc < 2:24.0.0-2
# This documentation package has been renamed to gnatcoll-core-doc to emphasize
# its scope now that gnatcoll-db-doc has been introduced as a subpackage of
# gnatcoll-db.
# These Provides and Obsoletes tags shall be kept at least in Fedora 41 and 42.

%description core-doc %{common_description_en}

The gnatcoll-core-doc package contains the documentation for the core components
of the GNAT Components Collection.

%description core-doc -l sv %{common_description_sv}

Paketet gnatcoll-core-doc innehåller dokumentationen till GNAT Components
Collections centrala komponenter.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

# The information in the VERSION files is read by the Python-based
# configuration scripts. File `core/VERSION` is also read by
# `docs/conf.py`.
for component in minimal core projects ; do
    echo '%{version}' > ./${component}/VERSION
done

# Scenario variables.
%global scn_vars -XLIBRARY_TYPE=relocatable \\\
                 -XXMLADA_BUILD=relocatable \\\
                 -XGPR_BUILD=relocatable

###########
## Build ##
###########

%build

# Configure the projects but don't build them.
for component in minimal core projects ; do
    ./${component}/gnatcoll_${component}.gpr.py \
        build --configure-only --enable-constant-update
done

# Extend the GNAT project search path as `gnatcoll_projects` depends on
# `gnatcoll_core` and `gnatcoll_core` depends on `gnatcoll_minimal`.
for component in minimal core projects ; do
    GPR_PROJECT_PATH=${PWD}/${component}/:$GPR_PROJECT_PATH
done
export GPR_PROJECT_PATH

# Build the libraries
for component in minimal core projects ; do
    gprbuild %{GPRbuild_flags} %{scn_vars} \
             -P ${component}/gnatcoll_${component}.gpr
done

# Make the documentation.
make -C docs html latexpdf

#############
## Install ##
#############

%install

# Extend the GNAT project search path as `gnatcoll_projects` depends on
# `gnatcoll_core` and `gnatcoll_core` depends on `gnatcoll_minimal`.
for component in minimal core projects ; do
    GPR_PROJECT_PATH=${PWD}/${component}/:$GPR_PROJECT_PATH
done
export GPR_PROJECT_PATH

# Install the libraries.
for component in minimal core projects ; do
    %{GPRinstall -s gnatcoll-${component} -a gnatcoll-${component}} \
                 --no-build-var %{scn_vars} \
                 -P ${component}/gnatcoll_${component}.gpr
done

# Fix up the symlinks.
for component in minimal core projects ; do
    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       %{buildroot}%{_libdir}/libgnatcoll_${component}.so
done

# Install `gnatcoll.gpr` for backward compatibility: the high-level
# API for manipulating GNAT project files has been split off from the
# set of core components, and the name of the GNAT project file of the
# remaining core components has been changed to `gnatcoll_core.gpr`.
# This (abstract) project file references both `gnatcoll_core.gpr` and
# `gnatcoll_projects.gpr`.
%{GPRinstall} -P gnatcoll.gpr

# Delete a comment that mentions the architecture.
sed --in-place \
    --expression='/^--  This project has been generated/d' \
    %{buildroot}%{_GNAT_project_dir}/gnatcoll.gpr

# Move the examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples

rmdir %{buildroot}%{_datadir}/examples

# Make the generated usage project files architecture-independent.
for component in minimal core projects ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Delete the package Linker, which contains linker parameters that a
    #    shared library normally doesn't need, and can contain architecture-
    #    specific pathnames.
    # 4: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 5: Replace the value of Library_Dir with Directories.Libdir.
    # 6: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

###########
## Files ##
###########

%files
# empty metapackage

%files devel
# empty metapackage

%files core
%license COPYING3 COPYING.RUNTIME
%{_libdir}/lib%{name}_minimal.so.%{version}
%{_libdir}/lib%{name}_core.so.%{version}

%files projects
%{_libdir}/lib%{name}_projects.so.%{version}

%files core-devel
%{_GNAT_project_dir}/%{name}_minimal.gpr
%dir %{_includedir}/%{name}-minimal
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/%{name}-minimal/*.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/%{name}-minimal/*.ad[sb]
%dir %{_libdir}/%{name}-minimal
%attr(444,-,-) %{_libdir}/%{name}-minimal/*.ali
%{_libdir}/lib%{name}_minimal.so

%{_GNAT_project_dir}/%{name}_core.gpr
%dir %{_includedir}/%{name}-core
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/%{name}-core/*.[chS]
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/%{name}-core/*.ad[sb]
%dir %{_libdir}/%{name}-core
%attr(444,-,-) %{_libdir}/%{name}-core/*.ali
%{_libdir}/lib%{name}_core.so

%files projects-devel
%{_GNAT_project_dir}/%{name}_projects.gpr
%{_includedir}/%{name}-projects
%dir %{_libdir}/%{name}-projects
%attr(444,-,-) %{_libdir}/%{name}-projects/*.ali
%{_libdir}/lib%{name}_projects.so
# GNAT project `gnatcoll.gpr`. Added for backward-compatibility.
%{_GNAT_project_dir}/%{name}.gpr

%files core-doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/GNATColl.pdf
%{_pkgdocdir}/html
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude /%{_pkgdocdir}/html/.buildinfo
%exclude /%{_pkgdocdir}/html/objects.inv

###############
## Changelog ##
###############

%changelog
%autochangelog
