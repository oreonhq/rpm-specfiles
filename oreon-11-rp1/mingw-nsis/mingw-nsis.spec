%global source0_hash 19e72062676ebdc67c11dc032ba80b979cdbffd3886c60b04bb442cdd401ff4b

%global sconsopts VERSION=%{version} PREFIX=%{_prefix} PREFIX_CONF=%{_sysconfdir} ZLIB_W32=%{mingw32_prefix} SKIPUTILS=NSISMenu STRIP_CP=false NSIS_MAX_STRLEN=8192 NSIS_CONFIG_LOG=yes
%global sconsopts64 %{sconsopts} TARGET_ARCH=amd64

Name:           mingw-nsis
Version:        3.11
Release:        3%{?dist}
Summary:        Nullsoft Scriptable Install System

License:        Zlib AND CPL-1.0
URL:            http://nsis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nsis/nsis-%{version}-src.tar.bz2

# Workaround recent scons not handling the space in 'NSIS Menu' correctly, see also %%prep
# scons: *** Invalid value(s) for variable 'SKIPUTILS': 'NSIS,Menu'
Patch0:         nsis-nsismenu.patch
# Use RPM_OPT_FLAGS for the natively-built parts
Patch1:         0001-Use-RPM_OPT_FLAGS-for-the-natively-built-parts.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-scons
BuildRequires:  zlib-devel

BuildRequires:  mingw32-filesystem >= 40
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 40
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib

# Don't build NSIS Menu as it doesn't actually work on POSIX systems: 1. it
# doesn't find its index.html file without patching, 2. it has various links to
# .exe files such as the makensisw.exe W32 GUI which are not available in the
# POSIX version at all and 3. the documentation links have backslashes in the
# URLs and the relative paths are wrong. Almost none of the links worked when I
# tested it (after patching problem 1.).
# Also removes unnecessary wxGTK dependency for this otherwise GUI-less package.
# (Does it really make sense to drag in wxGTK just to display a HTML file?)
# If you really want to reenable this, it needs a lot of fixing. Oh, and it'd
# need a .desktop file too.
# -- Kevin Kofler
# BuildRequires:  wxGTK-devel

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

%files -n mingw-nsis-base
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/GenPat
%{_bindir}/makensis
%{_sysconfdir}/nsisconf.nsh
%dir %{_datadir}/nsis
%dir %{_datadir}/nsis/Bin
%{_datadir}/nsis/Bin/MakeLangId.exe
%{_datadir}/nsis/Bin/makensisw.exe
%{_datadir}/nsis/Bin/zip2exe.exe
%{_datadir}/nsis/Contrib/
%{_datadir}/nsis/Include/
%dir %{_datadir}/nsis/Plugins
%dir %{_datadir}/nsis/Stubs
%{_datadir}/nsis/Stubs/uninst

%files -n mingw32-nsis
%{_datadir}/nsis/Bin/RegTool-x86.bin
%{_datadir}/nsis/Plugins/x86-ansi/
%{_datadir}/nsis/Plugins/x86-unicode/
%{_datadir}/nsis/Stubs/bzip2_solid-x86-ansi
%{_datadir}/nsis/Stubs/bzip2_solid-x86-unicode
%{_datadir}/nsis/Stubs/bzip2-x86-ansi
%{_datadir}/nsis/Stubs/bzip2-x86-unicode
%{_datadir}/nsis/Stubs/lzma_solid-x86-ansi
%{_datadir}/nsis/Stubs/lzma_solid-x86-unicode
%{_datadir}/nsis/Stubs/lzma-x86-ansi
%{_datadir}/nsis/Stubs/lzma-x86-unicode
%{_datadir}/nsis/Stubs/zlib_solid-x86-ansi
%{_datadir}/nsis/Stubs/zlib_solid-x86-unicode
%{_datadir}/nsis/Stubs/zlib-x86-ansi
%{_datadir}/nsis/Stubs/zlib-x86-unicode

%files -n mingw64-nsis
%{_datadir}/nsis/Bin/RegTool-amd64.bin
%{_datadir}/nsis/Plugins/amd64-unicode/
%{_datadir}/nsis/Stubs/bzip2-amd64-unicode
%{_datadir}/nsis/Stubs/bzip2_solid-amd64-unicode
%{_datadir}/nsis/Stubs/lzma-amd64-unicode
%{_datadir}/nsis/Stubs/lzma_solid-amd64-unicode
%{_datadir}/nsis/Stubs/zlib-amd64-unicode
%{_datadir}/nsis/Stubs/zlib_solid-amd64-unicode

%changelog
%autochangelog
