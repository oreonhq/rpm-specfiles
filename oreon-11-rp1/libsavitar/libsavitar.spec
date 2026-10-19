%global source1_hash 968a5c8306448ebe8129449b097d76eedd9e7ddfd1e68888a71975897374d281
%global source0_hash ed44dd42426ba4f592c2d83f652af5c2c60a1f619d16d31afa0babc2a0c997ce
Name:           libsavitar
Version:        5.3.0
Release:        1%{?dist}
Summary:        C++ implementation of 3mf loading with SIP Python bindings
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/libSavitar
Source0:        https://github.com/Ultimaker/libSavitar/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/Ultimaker/pySavitar/archive/%{version}.tar.gz#/pySavitar-%{version}.tar.gz
Source2:        FindSIP.cmake
Source3:        SIPMacros.cmake
Source4:        CMakeLists.txt
Source5:        SavitarConfig.cmake.in
Source6:        COPYING-CMAKE-SCRIPTS
Patch0:         libsavitar-5.2.2-export-fix.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  /usr/bin/sip
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pugixml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel
# /oreon:deps
%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package        devel
Summary:        Development files for libsavitar
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        LGPL-3.0-or-later AND BSD-3-Clause
%description    devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n     python3-savitar
Summary:        Python 3 libSavitar bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python3-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libSavitar-%{version} -p1 -S git -a 1

cp -a pySavitar-%{version}/python .
mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE6} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE4} %{SOURCE5} .

# Wrong end of line encoding
dos2unix README.md

%build

export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-savitar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libsavitar-devel -f %{oreon_filedir}/libsavitar-devel.list
%files -n python3-savitar -f %{oreon_filedir}/python3-savitar.list

%changelog

%autochangelog
