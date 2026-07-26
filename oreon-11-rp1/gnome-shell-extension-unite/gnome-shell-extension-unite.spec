%global source0_hash d9e6abf0d97df22f85405a9ff7170a2580bd0b657d4f3d8ffd72297707381d05

%global extuuid		unite@hardpixel.eu
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		unite-shell
%global giturl		https://github.com/hardpixel/%{gitname}

Name:		gnome-shell-extension-unite
Version:	8
Release:	21%{?dist}
Summary:	GNOME Shell Extension Unite by hardpixel

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://extensions.gnome.org/extension/1287/unite
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	gnome-shell-extension-common
Requires:	xprop

%description
Unite is a GNOME Shell extension which makes a few layout tweaks to the
top panel and removes window decorations to make it look like Ubuntu
Unity Shell.

  * Adds window buttons to the top panel for maximized windows.
  * Shows current window title in the app menu for maximized windows.
  * Removes titlebars on maximized windows.
  * Hides window controls on maximized windows with headerbars.
  * Moves the date to the right, fixes icons spacing and removes
    dropdown arrows.
  * Moves legacy tray icons to the top panel.
  * Moves notifications to the right.
  * Hides activities button.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{version} -p 1

%build
# noop

%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}

%files
%license LICENSE
%doc README.md
%{extdir}

%changelog
%autochangelog
