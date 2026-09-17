%global source0_hash 41ad51e02a3ec6981611be473221a3877fd359d3c1fa2172b4265dbe55f8b746

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
%undefine _include_frame_pointers

Name: argyllcms
Version: 3.4.1
Release: 4%{?dist}

# Main code - AGPL-3.0-or-later
# spectro, xml - GPL-2.0-or-later
# xicc - GPL-3.0-or-later
# cgats, icc - MIT
# documentation - GFDL-1.3-or-later
License: AGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT AND GFDL-1.3-or-later
Summary: ICC compatible color management system
URL: https://www.argyllcms.com
Source0: %{url}/Argyll_V%{version}_src.zip#/%{name}-%{version}.zip

BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: jam

Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

Spectral sample data is supported, allowing a selection of illuminants observer
types, and paper fluorescent whitener additive compensation. Profiles can also
incorporate source specific gamut mappings for perceptual and saturation
intents. Gamut mapping and profile linking uses the CIECAM02 appearance model,
a unique gamut mapping algorithm, and a wide selection of rendering intents. It
also includes code for the fastest portable 8 bit raster color conversion
engine available anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using a VRML
viewer.

%package doc
Summary: Argyll CMS documentation
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description doc
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

This package contains the Argyll color management system documentation.

%package data
Summary: Argyll CMS assets
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: color-filesystem

%description data
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

This package contains the Argyll color management system assets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Argyll_V%{version}

# Exporting correct build flags...
echo "CCFLAGS += \${CFLAGS} -std=gnu89 -fcommon -fPIC -fno-strict-aliasing ;" >> Jamtop
echo "LINKFLAGS += \${LDFLAGS} ;" >> Jamtop

# Unbundling libraries...
rm -rf jpeg png tiff usb zlib

# Removing executable flag from files...
find -type f -name '*.txt' -exec chmod -x '{}' \;
find doc -type f -exec chmod -x '{}' \;
find doc -type f -name '*.htm*' -exec sed -ie 's,\r,,' '{}' \;

%build
%set_build_flags
jam -fJambase %{?_smp_mflags} -sPREFIX=%{_prefix} -sDESTDIR=%{buildroot} -sREFSUBDIR=share/color/argyll/ref all

%install
jam -fJambase -sPREFIX=%{_prefix} -sDESTDIR=%{buildroot} -sREFSUBDIR=share/color/argyll/ref install
rm -f %{buildroot}/%{_bindir}/*.txt
 
mkdir -p %{buildroot}%{_metainfodir}
mv %{buildroot}%{_bindir}/com.argyllcms.metainfo.xml %{buildroot}%{_metainfodir}/com.argyllcms.metainfo.xml

%files
%license License*.txt
%doc log.txt ReadMe.txt
%{_bindir}/applycal
%{_bindir}/average
%{_bindir}/cb2ti3
%{_bindir}/cctiff
%{_bindir}/ccxxmake
%{_bindir}/chartread
%{_bindir}/collink
%{_bindir}/colprof
%{_bindir}/colverify
%{_bindir}/cxf2ti3
%{_bindir}/dispcal
%{_bindir}/dispread
%{_bindir}/dispwin
%{_bindir}/extracticc
%{_bindir}/extractttag
%{_bindir}/fakeCMY
%{_bindir}/fakeread
%{_bindir}/greytiff
%{_bindir}/iccdump
%{_bindir}/iccgamut
%{_bindir}/icclu
%{_bindir}/iccvcgt
%{_bindir}/illumread
%{_bindir}/invprofcheck
%{_bindir}/kodak2ti3
%{_bindir}/ls2ti3
%{_bindir}/mppcheck
%{_bindir}/mpplu
%{_bindir}/mppprof
%{_bindir}/oeminst
%{_bindir}/printcal
%{_bindir}/printtarg
%{_bindir}/profcheck
%{_bindir}/refine
%{_bindir}/revfix
%{_bindir}/scanin
%{_bindir}/spec2cie
%{_bindir}/specplot
%{_bindir}/splitti3
%{_bindir}/spotread
%{_bindir}/synthcal
%{_bindir}/synthread
%{_bindir}/targen
%{_bindir}/tiffgamut
%{_bindir}/timage
%{_bindir}/txt2ti3
%{_bindir}/viewgam
%{_bindir}/xicclu
%{_metainfodir}/com.argyllcms.metainfo.xml

%files doc
%license doc/DocLicense.txt
%doc doc/*.html doc/*.jpg doc/SG*.txt
%doc doc/ccmxs doc/ccsss

%files data
%{_datadir}/color/argyll/

%changelog
%autochangelog
