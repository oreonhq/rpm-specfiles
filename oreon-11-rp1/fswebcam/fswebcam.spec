%global source0_hash cff0cbd91457133847e40944db3ee0b6f81d06506cef260687bde8348c8a0ce4

Name:           fswebcam
Version:        20200725
Release:        14%{?dist}
Summary:        Tiny and flexible webcam program

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.sanslogic.co.uk/fswebcam/
Source0:        %{url}files/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  make

%description
A tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG README LICENSE example.conf
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
%autochangelog
