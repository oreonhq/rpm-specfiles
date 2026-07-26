%global source0_hash 4f69f7f13a8ef4076d499d798b6bddfc1800d30aa19b0354006a23754de54c64

Name:           yascreen
Version:        2.06
Release:        4%{?dist}
Summary:        Yet Another Screen Library (lib(n)curses alternative)

License:        LGPL-3.0-only
URL:            https://github.com/bbonev/yascreen/
Source0:        %{url}releases/download/v%{version}/yascreen-%{version}.tar.xz
Source1:        %{url}releases/download/v%{version}/yascreen-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/yascreen/master/debian/upstream/signing-key.asc

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make

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
# allow debug info to be generated
chmod +x $RPM_BUILD_ROOT%{_libdir}/libyascreen.so.0.0.0
# remove unpackaged static library
rm -f $RPM_BUILD_ROOT%{_libdir}/libyascreen.a

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/yascreen.pc
%{_mandir}/man3/yascreen.3*
%{_includedir}/yascreen.h

%changelog
%autochangelog
