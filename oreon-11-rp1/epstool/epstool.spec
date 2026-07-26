%global source0_hash f3f14b95146868ff3f93c8720d5539deef3b6531630a552165664c7ee3c2cfdd

Name:           epstool
Version:        3.08
Release:        33%{?dist}
Summary:        A utility to create or extract preview images in EPS files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm
Source0:        http://mirror.cs.wisc.edu/pub/mirrors/ghost/ghostgum/%{name}-%{version}.tar.gz
# Patch to compile with gcc 4.3 and newer (taken from Gentoo)
Patch0:         epstool-3.08-gcc43.patch

BuildRequires: make
BuildRequires:  gcc

%description
Epstool is a utility to create or extract preview images in EPS files,
fix bounding boxes and convert to bitmaps.

Features:
* Add EPSI, DOS EPS or Mac PICT previews.
* Extract PostScript from DOS EPS files.
* Uses Ghostscript to create preview bitmaps.
* Create a TIFF, WMF, PICT or Interchange preview from part of a
  bitmap created by Ghostscript.
* works under Win32, Win64, OS/2 and Unix.
* works on little-endian machines (Intel) or big endian (Sun Sparc,
  Motorola) machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
# SMP build doesn't work.
%make_build -j1

%install
rm -rf %{buildroot}
install -D -p -m 755 bin/epstool %{buildroot}%{_bindir}/epstool
install -D -p -m 644 doc/epstool.1 %{buildroot}%{_mandir}/man1/epstool.1

%files
%doc LICENCE doc/epstool.htm doc/gsview.css
%{_bindir}/epstool
%{_mandir}/man1/epstool.1.*

%changelog
%autochangelog
