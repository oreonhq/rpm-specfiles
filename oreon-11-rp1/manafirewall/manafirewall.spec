%global source0_hash 1aae4eebc708afe2e01bba6d055a3b2b94aa0cf6094a11f4650daaec19236ba7

# Force out of source build
%undefine __cmake_in_source_build

Name:		manafirewall
Version:	0.0.3
Release:	18%{?dist}
Summary:	ManaTools FirewallD configuration tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/manatools/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	cmake			>= 3.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig
BuildRequires:	python3-devel		>= 3.4.0
BuildRequires:	python3-setuptools
BuildRequires:	python3-yaml
BuildRequires:	python3-yui
BuildRequires:	python3-manatools	>= 0.0.3

Requires:	hicolor-icon-theme
Requires:	python3-yaml
Requires:	python3-yui
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-firewall	>= 0.9.0
Requires:	firewalld
# Ensure base TUI deps are installed
Requires:	libyui-ncurses
Requires:	libyui-mga-ncurses

Provides:	%{name}-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)

%description
%{name} is the graphical configuration tool for firewalld based on python
manatools and libYui (Suse widget abstraction library), to be run using
Qt 5, GTK+ 3, or ncurses interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake	-DCHECK_RUNTIME_DEPENDENCIES=ON
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate		\
	%{buildroot}%{_datadir}/applications/*.desktop
# Validate metainfo-files.
appstream-util validate-relax --nonet		\
	%{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files -f %{name}.lang
%doc README.md TODO.md
%license AUTHORS LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_metainfodir}/*%{name}.metainfo.xml

%changelog
%autochangelog
