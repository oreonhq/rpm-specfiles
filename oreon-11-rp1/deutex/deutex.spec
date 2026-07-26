%global source0_hash 74bc442169623d5b35dd5c62d8d1747da4358a6d499a6c8a21e6a71c3cf97e98

%define waddir  %{_datadir}/doom

Name:           deutex
Version:        5.2.3
Release:        4%{?dist}
Summary:        DOOM wad file manipulator

# All files LGPLv2+ or GPLv2+ except ./src/lzw.c which is MIT
License:        GPL-2.0-or-later and MIT
URL:            https://github.com/Doom-Utils/deutex
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         deutex-5.2.0-waddir.patch
BuildRequires:	gcc, autoconf, automake, asciidoc
BuildRequires: make
BuildRequires: libpng-devel

%description
DeuTex is a wad composer for Doom, Heretic, Hexen and Strife. It can be
used to extract the lumps of a wad and save them as individual files.
Conversely, it can also build a wad from separate files. When extracting
a lump to a file, it does not just copy the raw data, it converts it to
an appropriate format (such as PPM for graphics, Sun audio for samples,
etc.). Conversely, when it reads files for inclusion in pwads, it does
the necessary conversions (for example, from PPM to Doom picture
format). In addition, DeuTex has functions such as merging wads, etc. If
you're doing any wad hacking beyond level editing, DeuTex is a must.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0

%build
autoreconf -if
%configure --with-libpng
make CFLAGS="$RPM_OPT_FLAGS -DDOOMDIR=\"\\\"%{waddir}\\\"\"" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/deutex
%{_mandir}/man6/*
%license LICENSE
%doc COPYING COPYING.LIB AUTHORS README.adoc NEWS.adoc

%changelog
%autochangelog
