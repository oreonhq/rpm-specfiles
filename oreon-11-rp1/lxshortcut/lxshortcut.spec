%global source0_hash 8097f2522657374162a4e5e3c58898fe0c367e307b0ff4c50848b6b0323409fe

Name:           lxshortcut
Version:        0.1.2
Release:        32%{?dist}
Summary:        Small utility to edit application shortcuts

# COPYING	GPL-3.0-or-later
# src		GPL-2.0-or-later
# SPDX confirmed
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://lxde.org
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxshortcut
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  gettext
BuildRequires:  intltool

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

%files -f %{name}.lang
%doc ChangeLog
%doc README
%license COPYING

%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui

%changelog
%autochangelog
