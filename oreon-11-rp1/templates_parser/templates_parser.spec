%global source0_hash 2d1c2cb96ee7e44064c5f6c9692d1f886772dbaa7ec0d200e9254b134daabbad
%global upstream_owner    AdaCore
%global upstream_name     templates-parser
%global upstream_version  26.0.0
%global upstream_commit   cc94ff9833cfe776d462b490aac9727b623742c8
Name:           templates_parser
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        An Ada library for parsing templates
License:        GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Source1:        templates2ada.1
Source2:        templatespp.1
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
Templates Parser is the templates engine of the Ada Web Server. It is \
designed to parse files and replace some specific tags in these files \
with some specified values.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  xmlada-devel
# /oreon:deps
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
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
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

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

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

%global tp_options -XVERSION=%{version} \\\
                   -XPRJ_BUILD=Release \\\
                   -XPRJ_TARGET=Linux \\\
                   -XTP_TASKING=Standard_Tasking \\\
                   -XTP_XMLADA=Installed \\\
                   -XLIBRARY_TYPE=relocatable \\\
                   -XXMLADA_BUILD=relocatable
gprbuild %{GPRbuild_flags} %{tp_options} -P templates_parser.gpr
gprbuild %{GPRbuild_flags} %{tp_options} -P tools/tools.gpr -cargs -fPIE
make -C docs html latexpdf \
     GPRBUILD="gprbuild -cargs -fPIE -gargs" \
     PRJ_TARGET=Linux PRJ_BUILD=Release \
     TARGET=$(gcc -dumpmachine) VERSION=%{version}
%install
%{GPRinstall} %{tp_options} --no-build-var -P templates_parser.gpr
%{GPRinstall} %{tp_options} --mode=usage -P tools/tools.gpr
ln --symbolic --force lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so
mkdir --parents %{buildroot}%{_mandir}/man1
cp --preserve=timestamps %{SOURCE1} %{buildroot}%{_mandir}/man1/
cp --preserve=timestamps %{SOURCE2} %{buildroot}%{_mandir}/man1/
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/templates.tads %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/all_urls.thtml %{buildroot}%{_pkgdocdir}/examples
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}.gpr
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n templates_parser-devel -f %{oreon_filedir}/templates_parser-devel.list
%files -n templates_parser-doc -f %{oreon_filedir}/templates_parser-doc.list
%files -n templates_parser-tools -f %{oreon_filedir}/templates_parser-tools.list

%changelog

%autochangelog
