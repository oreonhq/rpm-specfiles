%global source0_hash 4909eacc26c4cd5a9afcd1468aec26e7c646544639031bdad4f71173aa82f3c3
Name:       xwd
Version:    1.0.10
Release:        1%{?dist}
Summary:        Dump an X window to file
License:    MIT-open-group AND HPND-sell-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
Xwd is an X Window System window dumping utility. Xwd allows X users to
store window images in a specially formatted dump file. This file can then
be read by various other X utilities for redisplay, printing, editing,
formatting, archiving, image processing, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
