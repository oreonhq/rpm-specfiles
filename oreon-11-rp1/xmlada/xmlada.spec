%global source0_hash a202f1c9955d26973d30e6d0357ba83f4031bc218006d620fa916420316a4f24
%bcond_with bootstrap
%global upstream_owner    AdaCore
%global upstream_name     xmlada
%global upstream_version  26.0.0
%global upstream_commit   5e5b761eb827f458efd2043a5e9ab03e1a614720
Name:           xmlada
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        XML library for Ada
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND Unicode-DFS-2016
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        xmlada.gpr
%if %{without bootstrap}
%else
%endif
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
XML/Ada includes support for parsing XML files, including DTDs, full support for \
SAX, and an almost complete support for the core part of the DOM. It includes \
support for validating XML files with XML schemas.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
# /oreon:deps
%description %{common_description_en}

#################
## Subpackages ##
#################

%if %{without bootstrap}

%package devel
Summary:        Development files for the XML/Ada library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc
%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the XML/Ada library.

%package static
Summary:        Static libraries of XML/Ada
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
%description static %{common_description_en}

This package contains the XML/Ada libraries for static linking. It is needed
for linking GPRbuild statically so that GPRbuild will remain functional when
libraries are upgraded.

Other Fedora packages shall require xmlada-devel rather than xmlada-static if
possible.

%package doc
Summary:        Documentation for the XML/Ada library
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.

%else

# When bootstrapping gprbuild, only a package that contains source code is
# produced, so a debug package is not needed.
%global debug_package %{nil}

%package sources
Summary:        Sources of the XML/Ada library (for bootstrapping GPRbuild)
BuildArch:      noarch
%description sources %{common_description_en}

This package contains source code for bootstrapping GPRbuild on architectures
on which GPRbuild is not yet available.

%endif

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# Set version number.
sed --in-place --expression 's/18.0w/%{version}/' configure configure.in

###########
## Build ##
###########

%build

%if %{without bootstrap}
%configure --enable-build=distrib --enable-shared
%{make_build} shared static-pic GPROPTS='%{GPRbuild_flags}'
make -C docs html latexpdf
%else
%{configure} --enable-build=distrib
%endif
%install
%if %{without bootstrap}
for component_dir in dom schema unicode sax input_sources ; do
    diff --exclude "*.a" --exclude "*.so*" --exclude ".cvsignore" \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/relocatable \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/static-pic
done
function run_gprinstall {
    local libtype=$1
    local component=$2
    local directory=$3  # directory name in the source tree
    %{GPRinstall -s xmlada/${component}} \
               --build-var=LIBRARY_TYPE --build-var=XMLADA_BUILD \
               --build-name=${libtype} -XLIBRARY_TYPE=${libtype} \
               -P ${directory}/%{name}_${component}.gpr
}
for libtype in relocatable static-pic ; do
    for component in dom schema unicode sax ; do
        run_gprinstall ${libtype} ${component} ${component}
    done
    run_gprinstall ${libtype} input input_sources
done
install --mode=u=rw,go=r,a-s --preserve-timestamps \
        %{SOURCE1} --target-directory=%{buildroot}%{_GNAT_project_dir}
for component in dom input_sources schema unicode sax ; do
    ln --symbolic --force lib%{name}_${component}.so.%{version} \
       %{buildroot}%{_libdir}/lib%{name}_${component}.so
done
mv --no-target-directory %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples
rmdir %{buildroot}%{_datadir}/examples
for component in dom input schema unicode sax ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}/${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/%{name}_${component}.gpr
done
%else
mkdir --parents %{buildroot}%{_includedir}/%{name}/sources
cp -r . %{buildroot}%{_includedir}/%{name}/sources
find %{buildroot}%{_includedir}/%{name}/sources -type f ! -name "*ad[sb]" ! -name "*gpr" -delete
find %{buildroot}%{_includedir}/%{name}/sources -type d -empty -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list
%files -n xmlada-devel -f %{oreon_filedir}/xmlada-devel.list
%files -n xmlada-static -f %{oreon_filedir}/xmlada-static.list
%files -n xmlada-doc -f %{oreon_filedir}/xmlada-doc.list

%changelog

%autochangelog
%endif
