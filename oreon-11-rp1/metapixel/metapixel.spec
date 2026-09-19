%global source0_hash 8d77810978da397c070b9b4e228ae6204e9f5c524518ad1a4fcab9462171f55b

Summary: Photomosaic Generator
Name: metapixel
Version: 1.0.2
Release: 27%{?dist}
# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL: http://www.complang.tuwien.ac.at/schani/metapixel/
Source: http://www.complang.tuwien.ac.at/schani/%{name}/files/%{name}-%{version}.tar.gz

Requires: perl-interpreter
BuildRequires:  gcc
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: giflib-devel
BuildRequires: make
BuildRequires: perl-generators

Patch0:	metapixel-build-fixes.patch
Patch1: metapixel-copyright.patch
Patch2: metapixel-install.patch
# giflib-5.x compatibility
Patch3: metapixel-giflib5.patch

%description
A program for generating photomosaics.  It can generate classical 
photomosaics, in which the source image is viewed as a matrix of equally sized 
rectangles for each of which a matching image is substituted, as well as 
collage-style photomosaics, in which rectangular parts of the source image 
at arbitrary positions (i.e. not aligned to a matrix) are substituted by 
matching images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make PREFIX=$RPM_BUILD_ROOT/usr install

%files
%doc NEWS README
%license COPYING
%{_mandir}/man1/metapixel.1*
%{_bindir}/metapixel-prepare
%{_bindir}/metapixel
%{_bindir}/metapixel-imagesize
%{_bindir}/metapixel-sizesort

%changelog
%autochangelog
