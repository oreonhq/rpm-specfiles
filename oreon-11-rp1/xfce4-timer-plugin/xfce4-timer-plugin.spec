%global source0_hash acf4c861af88608b9e802a76a4b05846bd30189e0085e826680cc179b6df4cd3

%global minorver 1.7
%global _hardened_build 1

Name:		xfce4-timer-plugin
Version:	1.7.3
Release:	%autorelease
Summary:	Timer for the Xfce panel
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{minorver}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxml2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)

Requires:	xfce4-panel

%description
A timer for the Xfce panel. It supports countdown periods and alarms at 
certain times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-static

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/xfce4/panel/plugins/libxfcetimer*
%{_datadir}/xfce4/panel/plugins/xfce4-timer-plugin.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-timer-plugin.*g

%changelog
%autochangelog
