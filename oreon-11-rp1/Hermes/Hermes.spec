%global source0_hash 4231e0905295ef6e5079eb292bdf55fde0ea48d7585ee5a85fa3d77c3fce5b6b
Name:           Hermes
Version:        1.3.3
Release:        52%{?dist}
Summary:        Pixel format conversion library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://web.archive.org/web/20040202225109/http://www.clanlib.org/hermes/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         Hermes-1.3.3-debian.patch
Patch1:         Hermes-1.3.3-64bit.patch
Patch2:         Hermes-1.3.3-configure.patch
Patch3:         Hermes-1.3.3-gcc15.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

On x86 and MMX architectures, handwritten assembler routines are taking over
the job and doing it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C compiler
as there is no platform specific code but those are supported: DOS, Win32
(Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment), some BeOS
support.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# mark asm files as NOT needing execstack
for i in src/*.S; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done
# Regenerate the autofoo stuff, fixing the broken old libtool
# and regenerating these from source is good to do anyways
rm -rf aclocal.m4 autom4te.cache compile config.* configure install-sh libtool lt* missing mkinstalldirs
autoreconf -ivf

%build

%configure --disable-dependency-tracking --disable-static
%make_build
%install
%makeinstall
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles Hermes-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n Hermes-devel -f %{oreon_filedir}/Hermes-devel.list

%changelog

%autochangelog
