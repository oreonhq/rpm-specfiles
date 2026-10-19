%global source0_hash f8576ce5589fd15620abb73ff049ea31f55ddbd1bba6d1ffa87452658e7bc85f
%undefine _include_frame_pointers
Name: argyllcms
Version: 3.5.0
Release:        1%{?dist}
License: AGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT AND GFDL-1.3-or-later
Summary:        ICC compatible color management system
URL: https://www.argyllcms.com
Source0:        https://www.%{name}.com/Argyll_V%{version}_src.zip#/%{name}-%{version}.zip
Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  jam
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
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
%oreon_autofiles argyllcms-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles argyllcms-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n argyllcms-doc -f %{oreon_filedir}/argyllcms-doc.list
%files -n argyllcms-data -f %{oreon_filedir}/argyllcms-data.list

%changelog

%autochangelog
