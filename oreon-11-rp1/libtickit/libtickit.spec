%global source0_hash 4af827ba3aeaf591f4364c20d6e31c608e46fa6ada9ef7389ed5fba597f797b8
%global libname tickit
%global libtickit_ver  v0.4
%bcond_without unibilium
Name:           lib%{libname}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Terminal Interface Construction Kit
License:        MIT
URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/trunk/%{libtickit_ver}/+download/%{name}-%{version}.tar.gz
%if %{with unibilium}
%else
%endif
# oreon:deps
BuildRequires:  //bin/prove
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(Convert::Color)
BuildRequires:  perl(Convert::Color::XTerm)
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(unibilium)
# /oreon:deps
%description
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtermkey-devel%{?_isa}
%if %{with unibilium}
Requires:       unibilium-devel%{?_isa}
%endif
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
rm -f src/linechars.inc src/xterm-palette.inc

%build

CFLAGS="%{__global_cflags}" LDFLAGS="%{__global_ldflags}" %{make_build} VERBOSE=1
%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1
make examples
%files -f %{oreon_filedir}/main.list
%files -n libtickit-devel -f %{oreon_filedir}/libtickit-devel.list

%changelog

%autochangelog
