%global source0_hash b8da767c0ed66e2c0e8c2f78a8c827d8757634179b114a1352590f4e6d0b32c8
%global theme_name     Bluebird
Name:           bluebird
Version:        1.3
Release:        19%{?dist}
Summary:        A clean minimalistic theme for Xfce, GTK+ 2 and 3
License:        GPL-2.0-or-later OR LicenseRef-Callaway-CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/
Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
Bluebird is a GTK2/3/xfwm4/metacity theme based on Zuki Blues.
The xfwm theme is based on axiom.

%package gtk2-theme
Summary:        Bluebird GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines
%description gtk2-theme
Themes for GTK+2 as part of the Bluebird theme.

%package gtk3-theme
Summary:        Bluebird GTK+3 themes
%description gtk3-theme
Themes for GTK+3 as part of the Bluebird theme.

%package metacity-theme
Summary:        Bluebird Metacity themes
Requires:       metacity
%description metacity-theme
Themes for Metacity as part of the Bluebird theme.

%package xfwm4-theme
Summary:        Bluebird Xfwm4 themes
Requires:       xfwm4
%description xfwm4-theme
Themes for Xfwm4 as part of the Bluebird theme.

%package xfce4-notifyd-theme
Summary:        Bluebird Xfce4 notifyd theme
Requires:       xfce4-notifyd
%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Bluebird theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{theme_name}-%{version}

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}
cp -pr gtk-2.0/ gtk-3.0/ metacity-1/ xfwm4/ %{buildroot}%{_datadir}/themes/%{theme_name}
%oreon_autofiles bluebird-gtk2-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluebird-gtk3-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluebird-metacity-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluebird-xfwm4-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluebird-xfce4-notifyd-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bluebird-gtk2-theme -f %{oreon_filedir}/bluebird-gtk2-theme.list
%files -n bluebird-gtk3-theme -f %{oreon_filedir}/bluebird-gtk3-theme.list
%files -n bluebird-metacity-theme -f %{oreon_filedir}/bluebird-metacity-theme.list
%files -n bluebird-xfwm4-theme -f %{oreon_filedir}/bluebird-xfwm4-theme.list
%files -n bluebird-xfce4-notifyd-theme -f %{oreon_filedir}/bluebird-xfce4-notifyd-theme.list

%changelog

%autochangelog
