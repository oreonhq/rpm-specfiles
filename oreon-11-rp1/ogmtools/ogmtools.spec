%global source0_hash c8d61d1dbceb981dc7399c1a85e43b509fd3d071fb8d3ca89ea9385e6e40fdea

Name:           ogmtools
Version:        1.5
Release:        41%{?dist}
Summary:        Tools for Ogg media streams

License:        GPL-2.0-or-later
URL:            https://www.bunkus.org/videotools/ogmtools
Source:         %{url}/%{name}-%{version}.tar.bz2
Patch:          ogmtools-1.5-optflags.patch
Patch:          ogmtools-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  libdvdread-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel

# Bundled and forked copy
Provides:       bundled(avilib)

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

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/dvdxchap
%{_bindir}/ogmcat
%{_bindir}/ogmdemux
%{_bindir}/ogminfo
%{_bindir}/ogmmerge
%{_bindir}/ogmsplit
%{_mandir}/man1/dvdxchap.1*
%{_mandir}/man1/ogmcat.1*
%{_mandir}/man1/ogmdemux.1*
%{_mandir}/man1/ogminfo.1*
%{_mandir}/man1/ogmmerge.1*
%{_mandir}/man1/ogmsplit.1*

%changelog
%autochangelog
