%global source0_hash 85005300693a16ccebd9af58dcad582dee6d1ccbc066414c9524af9bed87cb51
Name:           chibi-scheme
Version:        0.12.0
Release:        1%{?dist}
Summary:        Minimal Scheme implementation for use as an extension language
License:        BSD-3-Clause AND MIT
URL:            http://synthcode.com/wiki/chibi-scheme
Source0:        http://synthcode.com/scheme/chibi/%{name}-%{version}.tgz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Chibi-Scheme is a very small library intended for use as an extension
and scripting language in C programs. In addition to support for
lightweight VM-based threads, each VM itself runs in an isolated
heap allowing multiple VMs to run simultaneously in different OS threads.

The default language is R7RS Scheme, with support for all libraries.
Support for additional languages such as JavaScript, Go, Lua and Bash
are planned for future releases. Scheme is chosen as a substrate because
its first class continuations and guaranteed tail-call optimization
makes implementing other languages easy.

Chibi-Scheme is known to work on 32 and 64-bit Linux, FreeBSD and OS X,
Plan9, Windows (using Cygwin), iOS, and Emscripten.

%package devel
Summary:        Development files for chibi-scheme
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n %name-devel
Chibi-Scheme is a very small library intended for use as an extension
and scripting language in C programs. In addition to support for
lightweight VM-based threads, each VM itself runs in an isolated
heap allowing multiple VMs to run simultaneously in different OS threads.

The default language is R7RS Scheme, with support for all libraries.
Support for additional languages such as JavaScript, Go, Lua and Bash
are planned for future releases. Scheme is chosen as a substrate because
its first class continuations and guaranteed tail-call optimization
makes implementing other languages easy.

Chibi-Scheme is known to work on 32 and 64-bit Linux, FreeBSD and OS X,
Plan9, Windows (using Cygwin), iOS, and Emscripten.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} SNOWPREFIX=%{_prefix} SNOWLIBDIR=%{_libdir} doc all
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} SNOWPREFIX=%{_prefix} SNOWLIBDIR=%{_libdir} IMAGE_FILES=""
%oreon_autofiles chibi-scheme-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%{_bindir}/chibi-scheme -mchibi.repl -d %{_datadir}/chibi/chibi.img
%{_bindir}/chibi-scheme -xscheme.red -mchibi.repl -d %{_datadir}/chibi/red.img
%{_bindir}/chibi-scheme -mchibi.snow.commands -mchibi.snow.interface -mchibi.snow.package -mchibi.snow.utils -d %{_datadir}/chibi/snow.img
%preun

if [ $1 -lt 1 ]; then
    rm -f %{_datadir}/chibi/chibi.img
    rm -f %{_datadir}/chibi/red.img
    rm -f %{_datadir}/chibi/snow.img
fi
%files -f %{oreon_filedir}/main.list
%files -n chibi-scheme-devel -f %{oreon_filedir}/chibi-scheme-devel.list

%changelog

%autochangelog
