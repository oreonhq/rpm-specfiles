%global source0_hash af961e4e8122b9e1fa325ae20c98f0a17b2087e2c777832ae6e47025ec921331
Name:       clingo
Version:    5.8.2
Release:        1%{?dist}
Summary:        A grounder and solver for logic programs
License:    MIT
URL:        https://potassco.org/clingo/
Source0:        https://github.com/potassco/clingo/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     clingo.clasp-disable-class-memaccess-warning.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  re2c
# /oreon:deps
%description
Clingo is part of the Potassco project for Answer Set Programming
(ASP). ASP offers a simple and powerful modeling language to describe
combinatorial problems as logic programs. The clingo system then takes
such a logic program and computes answer sets representing solutions
to the given problem.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n lua-%{name}
Summary:        Lua bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  lua-devel
%description -n lua-%{name}
Lua bindings for Clingo, a grounder and solver for logic programs.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%package -n python3-%{name}
Summary:        Python 3 bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3, python3-devel
BuildRequires:  python3-cffi
BuildRequires:  make
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
This module provides functions and classes to work with ground terms and to
control the instantiation process. In clingo builts, additional functions to
control and inspect the solving process are available.

Functions defined in a python script block are callable during the
instantiation process using @-syntax. The default grounding/solving process can
be customized if a main function is provided.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCLINGO_MANAGE_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DCLINGO_BUILD_APPS:BOOL=ON \
  -DPython_EXECUTABLE=%{__python3} \
  -DCLINGO_BUILD_SHARED:BOOL=ON \
  -DCLINGO_BUILD_WITH_PYTHON:BOOL=ON \
  -DLUACLINGO_INSTALL_DIR:PATH=%{lua_libdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles clingo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles lua-clingo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-clingo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n clingo-devel -f %{oreon_filedir}/clingo-devel.list
%files -n lua-clingo -f %{oreon_filedir}/lua-clingo.list
%files -n python3-clingo -f %{oreon_filedir}/python3-clingo.list

%changelog

%autochangelog
