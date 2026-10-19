%global source0_hash b1fdda9803277636366780c23fdc727e5b8a730008bcbfd0c721779659399a54
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
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Patch:          %{name}-core-fix-html-dir-indirection.patch
Patch:          %{name}-core-doc-examples-dir.patch
Patch:          %{name}-core-refine-dependencies-gnatcoll.patch
Patch:          %{name}-core-fix-base64-coder-example.patch
ExclusiveArch:  %{GPRbuild_arches}
Requires:       gnatcoll-core gnatcoll-gmp gnatcoll-iconv
Requires:       gnatcoll-readline gnatcoll-syslog
Requires:       gnatcoll-sql gnatcoll-sqlite gnatcoll-postgres gnatcoll-xref
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
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  libgpr-devel
BuildRequires:  make
BuildRequires:  python-unversioned-command
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  xmlada-devel
# /oreon:deps
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
Obsoletes:      gnatcoll-core-devel < 2:25.0.0
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
Recommends:     gnatcoll-core-doc
Obsoletes:      gnatcoll-core-devel < 2:25.0.0
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
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
Provides:       gnatcoll-doc = %{epoch}:%{version}-%{release}
Obsoletes:      gnatcoll-doc < 2:24.0.0-2
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

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

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

for component in minimal core projects ; do
    ./${component}/gnatcoll_${component}.gpr.py \
        build --configure-only --enable-constant-update
done
for component in minimal core projects ; do
    GPR_PROJECT_PATH=${PWD}/${component}/:$GPR_PROJECT_PATH
done
export GPR_PROJECT_PATH
for component in minimal core projects ; do
    gprbuild %{GPRbuild_flags} %{scn_vars} \
             -P ${component}/gnatcoll_${component}.gpr
done
make -C docs html latexpdf
%install
for component in minimal core projects ; do
    GPR_PROJECT_PATH=${PWD}/${component}/:$GPR_PROJECT_PATH
done
export GPR_PROJECT_PATH
for component in minimal core projects ; do
    %{GPRinstall -s gnatcoll-${component} -a gnatcoll-${component}} \
                 --no-build-var %{scn_vars} \
                 -P ${component}/gnatcoll_${component}.gpr
done
for component in minimal core projects ; do
    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       %{buildroot}%{_libdir}/libgnatcoll_${component}.so
done
%{GPRinstall} -P gnatcoll.gpr
sed --in-place \
    --expression='/^--  This project has been generated/d' \
    %{buildroot}%{_GNAT_project_dir}/gnatcoll.gpr
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples
rmdir %{buildroot}%{_datadir}/examples
for component in minimal core projects ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
done
%oreon_autofiles gnatcoll-projects usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-projects-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnatcoll-devel -f %{oreon_filedir}/gnatcoll-devel.list
%files -n gnatcoll-core -f %{oreon_filedir}/gnatcoll-core.list
%files -n gnatcoll-core-devel -f %{oreon_filedir}/gnatcoll-core-devel.list
%files -n gnatcoll-projects -f %{oreon_filedir}/gnatcoll-projects.list
%files -n gnatcoll-projects-devel -f %{oreon_filedir}/gnatcoll-projects-devel.list
%files -n gnatcoll-core-doc -f %{oreon_filedir}/gnatcoll-core-doc.list

%changelog

%autochangelog
