%global source0_hash c24a81dea8e9f7f3c877618d3812a5293df772abc6b90fad1d34fa62326141bc
%define __cmake_in_source_build 1
Name:           libcomps
Version:        0.1.24
Release:        1%{?dist}
Summary:        Comps XML file manipulation library
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/libcomps
Source0:        https://github.com/rpm-software-management/libcomps/archive/refs/tags/0.1.24.tar.gz#/libcomps-0.1.24.tar.gz
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package devel
Summary:        Development files for libcomps library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for libcomps library.

%package doc
Summary:        Documentation files for libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  doxygen
%description doc
Documentation files for libcomps library.

%package -n python-%{name}-doc
Summary:        Documentation files for python bindings libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python3-sphinx
%description -n python-%{name}-doc
Documentation files for python bindings libcomps library.

%package -n python3-%{name}
Summary:        Python 3 bindings for libcomps library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  make
%{?python_provide:%python_provide python3-%{name}}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      platform-python-%{name} < %{version}-%{release}
%description -n python3-%{name}
Python3 bindings for libcomps library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

mkdir build-py3
mkdir build-doc

%build

pushd build-py3
  %cmake ../libcomps/
  %cmake_build
popd
pushd build-doc
  %cmake ../libcomps/
  %cmake_build -t docs
  %cmake_build -t pydocs
popd
%install
pushd build-py3
  %cmake_install
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd build-py3
  %cmake_build -t test
  %cmake_build -t pytest
popd
%if %{undefined ldconfig_scriptlets}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%else
%ldconfig_scriptlets
%endif
%files -f %{oreon_filedir}/main.list
%files -n libcomps-devel -f %{oreon_filedir}/libcomps-devel.list
%files -n libcomps-doc -f %{oreon_filedir}/libcomps-doc.list
%files -n python-libcomps-doc -f %{oreon_filedir}/python-libcomps-doc.list
%files -n python3-libcomps -f %{oreon_filedir}/python3-libcomps.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.24-1
- Prepare for Oreon 11 (RP1)
