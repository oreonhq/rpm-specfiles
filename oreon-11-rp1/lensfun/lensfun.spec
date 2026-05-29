%global source0_hash dafb39c08ef24a0e2abd00d05d7341b1bf1f0c38bfcd5a4c69cf5f0ecb6db112
%global source1_hash dedba907e034e12177c1d69ab4e0edecbb94f76aeb27e38fa6823b88cbbc67c1

%if !0%{?bootstrap} && (0%{?fedora} || 0%{?rhel} > 6) || (0%{?oreon} >= 11)
%global tests 1
%global python3 python%{python3_pkgversion}
%endif

Name:    lensfun
Version: 0.3.4
Summary: Library to rectify defects introduced by photographic lenses
Release: 11%{?dist}

License: LGPLv3 and CC-BY-SA
URL: https://lensfun.github.io/
Source0:        https://github.com/lensfun/lensfun/archive/v%{version}/%{name}-%{version}.tar.gz
# Updated database. To generate:
# curl -L -o version_1-$(date +"%Y-%m-%d").tar.bz2 http://lensfun.sourceforge.net/db/version_1.tar.bz2
# Update this whenever updating the package
Source1: version_1-2024-06-27.tar.bz2

## upstream patches

## upstreamable patches
# install manpages only when INSTALL_HELPER_SCRIPTS=ON
Patch200: lensfun-0.3.2-INSTALL_HELPER_SCRIPTS.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
%if 0%{?python3:1}
BuildRequires: %{python3} %{python3}-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-setuptools
# we cannot use pyproject_buildrequires as setup.py is created in
# build phase
BuildRequires: python3-pip
BuildRequires: python3-wheel
%else
Obsoletes: lensfun-python3 < %{version}-%{release}
Obsoletes: lensfun-tools < %{version}-%{release}
%endif
# for rst2man, if INSTALL_HELPER_SCRIPTS != OFF
BuildRequires: /usr/bin/rst2man

%description
The lensfun library provides an open source database of photographic lenses and
their characteristics. It not only provides a way to read and search the
database, but also provides a set of algorithms for correcting images based on
detailed knowledge of lens properties. Right now lensfun is designed to correct
distortion, transversal (also known as lateral) chromatic aberrations,
vignetting and color contribution of a lens.

%package devel
Summary: Development toolkit for %{name}
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains library and header files needed to build applications
using lensfun.

%package tools
Summary: Tools for managing %{name} data
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
Requires: %{python3}-lensfun = %{version}-%{release}
%description tools
This package contains tools to fetch lens database updates and manage lens
adapters in lensfun.

%package -n %{python3}-lensfun
Summary:  Python3 lensfun bindings
Requires: %{name}%{?_isa} = %{version}-%{release}
%if 0%{?rhel} == 7 || (0%{?oreon} >= 11)
## pkgname changed in epel7 from python34- to python36-
Obsoletes: python34-lensfun < %{version}-%{release}
%endif
%description -n %{python3}-lensfun
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
# extract the updated data
pushd data/db
tar xvf %{SOURCE1} > /dev/null
popd

# disable calls to setup.py, we use our own python build/install macros
# this is the 0.3.4 version...
sed -i -e '/${PYTHON} ${SETUP_PY}/d' apps/CMakeLists.txt
# ...this is how it is on master branch, for future-proofing
sed -i -e '/${Python3_EXECUTABLE} ${SETUP_PY}/d' apps/CMakeLists.txt
# creating a timestamp doesn't work with build step disabled
sed -i -e '/touch/d' apps/CMakeLists.txt

%if 0%{?python3:1}
sed -i.shbang \
  -e "s|^#!/usr/bin/env python3$|#!%{__python3}|g" \
  apps/lensfun-add-adapter \
  apps/lensfun-update-data
%endif

# For CMake 4
sed -i -e 's@CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12 FATAL_ERROR@CMAKE_MINIMUM_REQUIRED(VERSION 3.5@' CMakeLists.txt

%build
%cmake \
  -DBUILD_DOC:BOOL=ON \
  -DBUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir}/devel-docs \
  %{?!python3:-DINSTALL_HELPER_SCRIPTS:BOOL=OFF}

%cmake_build

%cmake_build --target doc

# do a proper guideline-compliant build of the python library
%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
pushd apps
%py3_build
%else
pushd %_vpath_builddir/apps
%pyproject_wheel
%endif
popd


%install
%cmake_install

# do a proper guideline-compliant install of the python library
%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
pushd apps
%py3_install
%else
pushd %_vpath_builddir/apps
%pyproject_install
%pyproject_save_files -L lensfun
%endif
popd

# create/own /var/lib/lensfun-updates
mkdir -p %{buildroot}/var/lib/lensfun-updates

## unpackaged files
# omit g-lensfun-update-data because it needs gksudo which we don't ship
rm -fv %{buildroot}%{_bindir}/g-lensfun-update-data \
       %{buildroot}%{_mandir}/man1/g-lensfun-update-data.* \
       %{buildroot}%{_docdir}/%{name}/doxygen.svg

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
%ctest
%endif


%ldconfig_scriptlets

%files
%doc README.md
%license docs/cc-by-sa-3.0.txt docs/lgpl-3.0.txt
%{_datadir}/lensfun/
%{_libdir}/liblensfun.so.%{version}
%{_libdir}/liblensfun.so.1*
%dir /var/lib/lensfun-updates/

%files devel
%doc %{_pkgdocdir}/devel-docs
%{_includedir}/lensfun/
%{_libdir}/liblensfun.so
%{_libdir}/pkgconfig/lensfun.pc

%if 0%{?python3:1}
%files tools
%{_bindir}/lensfun-add-adapter
%{_bindir}/lensfun-update-data
%{_mandir}/man1/lensfun-add-adapter.1*
%{_mandir}/man1/lensfun-update-data.1*

%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
%files -n %{python3}-lensfun
%{python3_sitelib}/lensfun-*.egg-info/
%{python3_sitelib}/lensfun/
%else
%files -n %{python3}-lensfun -f %{pyproject_files}
%endif
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.4-11
- Import
