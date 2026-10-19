%global source0_hash 8097f2522657374162a4e5e3c58898fe0c367e307b0ff4c50848b6b0323409fe
Name:           lxshortcut
Version:        0.1.2
Release:        32%{?dist}
Summary:        Small utility to edit application shortcuts
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://lxde.org
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
# /oreon:deps
%description
LXShortcut is a small utility to edit application shortcuts created with 
freedesktop.org Desktop Entry spec. Now editing of application shortcuts 
becomes quite easy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
