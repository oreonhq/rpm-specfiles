%global source0_hash 1cedc0b4795e6f4234b1d52172f74d7163ecb8142fbb35dc86c905df5478d8fa
%global gxvattr 1
Summary:        Utility for getting and setting Xv attributes
Name:       xvattr
Version:    1.3
Release:        1%{?dist}
License:    GPL-2.0-or-later
URL:        http://www.dtek.chalmers.se/groups/dvd/
Source0:        http://ajax.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
Patch0:     xvattr-1.3-Convert-documentation-to-UTF-8.patch
Patch1:     xvattr-1.3-Use-GTK_CFLAGS-properly.patch
Patch2:     xvattr-1.3-Make-GTK-tools-optional.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gtk+-devel
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  perl-podlators
# /oreon:deps
%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY.

%package -n gxvattr
Summary: GTK1-based GUI for Xv attributes
%description -n gxvattr
GTK1-based GUI for inspecting and setting Xv attributes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf --install --force

%build

%configure \
    --enable-gtk
%{make_build}
%install
%{make_install}
%oreon_autofiles gxvattr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gxvattr -f %{oreon_filedir}/gxvattr.list

%changelog

%autochangelog
