%global source0_hash 438b5f7ec7e31a45ed3756630fe447f42015acda53ec09202f48628726b5e875
Name:           castget
Version:        2.0.1
Release:        1%{?dist}
Summary:        A command-line podcast downloader
License:        LGPL-2.1-or-later
URL:            https://castget.johndal.com/
Source0:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0:		stdlib.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  id3lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
castget is a simple, command-line based RSS enclosure downloader. It is
primarily intended for automatic, unattended downloading of podcasts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

CFLAGS+=-std=gnu17
%configure LDFLAGS=-Wl,--copy-dt-needed-entries
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
