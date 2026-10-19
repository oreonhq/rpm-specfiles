%global source0_hash cff0cbd91457133847e40944db3ee0b6f81d06506cef260687bde8348c8a0ce4
Name:           fswebcam
Version:        20200725
Release:        1%{?dist}
Summary:        Tiny and flexible webcam program
License:        GPL-2.0-only
URL:            http://www.sanslogic.co.uk/fswebcam/
Source0:        http://www.sanslogic.co.uk/%{name}/files/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  make
# /oreon:deps
%description
A tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
