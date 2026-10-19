%global source2_hash c459c03d0ae871d59b60255303bb972a3ece8ff4a4a63a1f8c90229f64234ecf
%global source0_hash 56505c73c64be6f216e4912e6b3245ed2d385c1fdb7039c84aa4c56a7ef7d7a7
Name:           yascreen
Version:        2.14
Release:        1%{?dist}
Summary:        Yet Another Screen Library (lib(n)curses alternative)
License:        LGPL-3.0-only
URL:            https://github.com/bbonev/yascreen/
Source0:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}releases/download/v%{version}/yascreen-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/yascreen/master/debian/upstream/signing-key.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
lib(n)curses alternative oriented towards modern terminals.

Suitable for developing terminal applications or daemons with
telnet access and terminal support.

Main features

 * small footprint
 * does not have external dependencies
 * allows both internal and external event loop
 * allows stdin/stdout or external input/output (can work over socket)
 * supports basic set of telnet sequences, making it suitable for built-in
   terminal interfaces for daemons
 * supports a limited set of input keystroke sequences
 * fully Unicode compatible (parts of this depend on wcwidth in libc)
 * supports utf8 verification of input
 * relies only on a limited subset of ANSI/xterm ESC sequences, making it
   compatible with mostly all modern terminals (inspired by linenoise)
 * there is no curses API and ancient terminal compatibility, hence less bloat
 * clean API with opaque private data, usable from C/C++

%package devel
Summary:        Development files for yascreen
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel

This package contains the header files and libraries needed to
compile applications or shared objects that use yascreen.

%global _hardened_build 1

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%set_build_flags
export CFLAGS="${RPM_OPT_FLAGS}"
NO_FLTO=1 DEBUG="" %make_build PREFIX=%{_prefix} LIBDIR=/%{_lib}/
%install
%make_install INSTALL+=" --strip-program=true" PREFIX=%{_prefix} LIBDIR=/%{_lib}/
chmod +x $RPM_BUILD_ROOT%{_libdir}/libyascreen.so.0.0.0
rm -f $RPM_BUILD_ROOT%{_libdir}/libyascreen.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n yascreen-devel -f %{oreon_filedir}/yascreen-devel.list

%changelog

%autochangelog
