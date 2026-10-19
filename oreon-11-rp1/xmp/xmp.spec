%global source0_hash cbfdab11233708c4de6ab965f64d96d4cb5b9d8e14d2d23df3b1b896386f870f
Name: xmp
Version: 4.3.1
Release:        1%{?dist}
Summary:        A multi-format module player
Source0:        https://downloads.sourceforge.net/project/xmp/xmp/%{version}/xmp-%{version}.tar.gz
Patch0: xmp-pulse.patch
License: GPL-2.0-or-later
URL: http://xmp.sourceforge.net/
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  libxmp-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
This is the Extended Module Player, a portable module player that plays
over 90 mainstream and obscure module formats, including Protracker MOD,
Fasttracker II XM, Scream Tracker 3 S3M and Impulse Tracker IT files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  --enable-pulseaudio \
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
