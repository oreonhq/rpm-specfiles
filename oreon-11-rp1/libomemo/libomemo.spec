%global source0_hash b64d603f675774c922ae9b0c841dd4dbbb59c3780d6ac60bc40dbcf7b0428519
Name: libomemo
Version: 0.8.1
Release:        1%{?dist}
License: MIT
Summary:        OMEMO implementation in plain C
URL: https://github.com/gkdr/%{name}
Source0:        https://github.com/gkdr/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
Implements OMEMO (XEP-0384) in plain C.

Input and output are XML strings, so it does not force you to use a certain
XML lib. While the actual protocol functions do not depend on any kind of
storage, it comes with a basic implementation in SQLite.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package contains header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DOMEMO_INSTALL:BOOL=ON \
    -DOMEMO_WITH_TESTS:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libomemo-devel -f %{oreon_filedir}/libomemo-devel.list

%changelog

%autochangelog
