%global source0_hash aaf3d7e9654ef6cf8ec442ad9e4316c481f9a6087a8e8949261140f5ae136aeb

%global _hardened_build 1
%global majorver 0.8
%global gen_name calculator

Name:		xfce4-calculator-plugin
Version:	0.8.0
Release:	%autorelease
Summary:	A calculator plugin for the Xfce4 panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{majorver}/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-panel-devel
BuildRequires:	gtk2-devel
BuildRequires:	meson
Requires:	xfce4-panel

%description
xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

Place the plugin in your panel, enter your calculation into the text field 
and press Enter to calculate the result.

The plugin supports common mathematical operators (+, -, *, /, ^) with usual 
precedence rules and some basic functions (e.g., trigonometric functions) 
and constants.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# remove empty file
rm -f NEWS

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_datadir}/xfce4/panel/plugins/%{gen_name}.desktop
%{_datadir}/icons/hicolor/*/*/*calculator*

%changelog
%autochangelog
