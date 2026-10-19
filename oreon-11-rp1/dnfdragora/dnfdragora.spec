%global source0_hash acb86155b5bbde4348482287fe1f8676548b0a9e51f7a9ae38de7ac3c5f69023
%undefine __cmake_in_source_build
%global commit 2f707ee21aae9fa512a1fe261959fbaa17291d63
%global commitdate 20250421
%global shortcommit %{sub %{commit} 1 7}
Name:		dnfdragora
Version:	2.99.0^git%{commitdate}.1.%{shortcommit}
Release:        1%{?dist}
Summary:        DNF package-manager based on libYui abstraction
License:	GPL-3.0-or-later
URL:		https://github.com/manatools/%{name}
%dnl Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:        https://github.com/manatools/%{name}/archive/%{commit}/%{name}-2f707ee.tar.gz
BuildArch:	noarch
Requires:	dnf5daemon-server	>= 5.2.7
Requires:	filesystem
Requires:	comps-extras
Requires:	hicolor-icon-theme
Requires:	libyui-mga-ncurses
Requires:	python3-libdnf5		>= 5.2.7
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-PyYAML
Requires:	python3-yui		>= 1.1.1-10
Provides:	%{name}-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  python3-PyYAML
BuildRequires:  python3-cairosvg
BuildRequires:  python3-devel
BuildRequires:  python3-libdnf5
BuildRequires:  python3-manatools
BuildRequires:  python3-pillow
BuildRequires:  python3-pystray
BuildRequires:  python3-pyxdg
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-yui
# /oreon:deps
%description
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.

%package updater
Summary:	Update notifier applet for %{name}
Requires:	%{name}			== %{version}-%{release}
Requires:	libnotify
Requires:	python3-pyxdg
Requires:	python3-cairosvg
Requires:	python3-pillow
Requires:	python3-pystray		>= 0.16
Obsoletes:	%{name}-gui		< 1.0.1-7
%description updater
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.

This package provides the update notifier applet for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 %{?commit:-n %{name}-%{commit}}

%build

%cmake \
  -DCHECK_RUNTIME_DEPENDENCIES=ON \
  -DENABLE_COMPS=ON               \
  %{nil}
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet		\
	%{buildroot}%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n dnfdragora-updater -f %{oreon_filedir}/dnfdragora-updater.list

%changelog

%autochangelog
