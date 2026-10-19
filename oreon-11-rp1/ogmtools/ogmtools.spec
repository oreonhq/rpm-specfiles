%global source0_hash c8d61d1dbceb981dc7399c1a85e43b509fd3d071fb8d3ca89ea9385e6e40fdea
Name:           ogmtools
Version:        1.5
Release:        1%{?dist}
Summary:        Tools for Ogg media streams
License:        GPL-2.0-or-later
URL:            https://www.bunkus.org/videotools/ogmtools
Source0:        https://www.bunkus.org/videotools/%{name}/%{name}-%{version}.tar.bz2
Patch:          ogmtools-1.5-optflags.patch
Patch:          ogmtools-configure-c99.patch
Provides:       bundled(avilib)
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libdvdread-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
# /oreon:deps
%description
These tools allow information about (ogminfo) or extraction from (ogmdemux) or
creation of (ogmmerge) OGG media streams. Note that OGM is used for "OGG media
streams".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Convert Changelog to UTF-8
iconv -f iso8859-1 -t utf8 ChangeLog -o ChangeLog.txt
touch -r ChangeLog ChangeLog.txt
mv ChangeLog.txt ChangeLog

%build

export CXXFLAGS="-std=c++14 %{optflags}"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
