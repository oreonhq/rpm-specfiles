%global source0_hash cc666b8e9b7a97289c0988e4cf31b2a818703089371fc8f59b43be1c0c8e48d7

%global commit 8a368f4904cb83df6555db04b3bdf7ddf8ac9f91
%global date   20231130
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:        Utility to capture video from a DV camera
Name:           dvgrab
Version:        3.5
Release:        39.%{date}git%{shortcommit}%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kinodv.org/
Source:         https://github.com/ddennedy/dvgrab/archive/%{commit}/dvgrab-%{commit}.tar.gz
BuildRequires:  libraw1394-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libdv-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libjpeg-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

ExcludeArch:    s390 s390x

%description
The dvgrab utility will capture digital video from a DV source on the firewire
(IEEE-1394) bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dvgrab-%{commit}
autoreconf -ivf

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README ChangeLog NEWS
%{_bindir}/dvgrab
%{_mandir}/man1/dvgrab.1*

%changelog
%autochangelog
