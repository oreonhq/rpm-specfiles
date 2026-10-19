%global source0_hash f3ed7a8e4aa2cf4e8cf47d3b563a02559e0cb4934db2662b2f9661b824e2b186
%global sconsopts VERSION=%{version} PREFIX=%{_prefix} PREFIX_CONF=%{_sysconfdir} ZLIB_W32=%{mingw32_prefix} SKIPUTILS=NSISMenu STRIP_CP=false NSIS_MAX_STRLEN=8192 NSIS_CONFIG_LOG=yes
%global sconsopts64 %{sconsopts} TARGET_ARCH=amd64
Name:           mingw-nsis
Version:        3.12
Release:        1%{?dist}
Summary:        Nullsoft Scriptable Install System
License:        Zlib AND CPL-1.0
URL:            http://nsis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nsis/nsis-%{version}-src.tar.bz2
Patch0:         nsis-nsismenu.patch
Patch1:         0001-Use-RPM_OPT_FLAGS-for-the-natively-built-parts.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib
BuildRequires:  python3
BuildRequires:  python3-scons
BuildRequires:  zlib-devel
# /oreon:deps
%description
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes native Fedora binaries of makensis (etc.) and
all plugins.

%package -n mingw-nsis-base
Summary:        Nullsoft Scriptable Install System - base files
%description -n mingw-nsis-base
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the natife Fedora binaries and the common
files for both mingw32-nsis and mingw64-nsis.

%package -n mingw32-nsis
Summary:        Nullsoft Scriptable Install System - win32
BuildArch:      noarch
Requires:       mingw-nsis-base = %{version}-%{release}
%description -n mingw32-nsis
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the binaries compiled for win32.

%package -n mingw64-nsis
Summary:        Nullsoft Scriptable Install System - win64
BuildArch:      noarch
Requires:       mingw-nsis-base = %{version}-%{release}
%description -n mingw64-nsis
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes the binaries compiled for win64.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n nsis-%{version}-src

# Remove executable bits
find -type f -exec chmod -x {} \;

# See Patch0
mv 'Contrib/NSIS Menu' 'Contrib/NSISMenu'

%build

scons %{sconsopts}
scons %{sconsopts64}
%install
scons %{sconsopts} PREFIX_DEST=%{buildroot} install
scons %{sconsopts64} PREFIX_DEST=%{buildroot} install
mv %{buildroot}%{_docdir}/nsis %{buildroot}%{_docdir}/%{name}
%oreon_autofiles mingw-nsis-base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-nsis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-nsis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw-nsis-base -f %{oreon_filedir}/mingw-nsis-base.list
%files -n mingw32-nsis -f %{oreon_filedir}/mingw32-nsis.list
%files -n mingw64-nsis -f %{oreon_filedir}/mingw64-nsis.list

%changelog

%autochangelog
