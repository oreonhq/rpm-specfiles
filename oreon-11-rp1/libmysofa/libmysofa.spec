%global source0_hash 11dabd3b69d2cd7a0c01b680e9e64b3c4aa4f0b99b55e58f10a17f043d38e4c4
%global commit 4585a0ae5bc98894750baf70e7f7989360e5a376
Name:           libmysofa
Version:        1.3.3
Release:        1%{?dist}
Summary:        C functions for reading HRTFs
License:        BSD-3-Clause
URL:            https://github.com/hoene/libmysofa
Source0:        https://github.com/hoene/%{name}/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
%{?!_without_tests:BuildRequires: nodejs, /usr/bin/node}
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
This is a simple set of C functions to read AES SOFA files, if they
contain HRTFs stored according to the AES69-2015 standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mysofa
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n mysofa
Tools for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libmysofa-%{commit}

%build

%cmake \
  -DBUILD_STATIC_LIBS=OFF \
  -DCODE_COVERAGE=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON
%cmake_build
%install
%cmake_install
%{?!_without_tests:
%oreon_autofiles mysofa usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export MYSOFA2JSON=%{_builddir}/%{buildsubdir}/%{_vpath_builddir}/src/mysofa2json
%ctest
}
%files -f %{oreon_filedir}/main.list
%files -n libmysofa-devel -f %{oreon_filedir}/libmysofa-devel.list
%files -n mysofa -f %{oreon_filedir}/mysofa.list

%changelog

%autochangelog
