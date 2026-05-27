%global source0_hash 42fe9e4dfaee72cfb7f6b21393c15e598c0087dca05f0eca73fcea7e0928cd3a

%global ename  dash-to-panel
%global extdir %{_datadir}/gnome-shell/extensions/dash-to-panel@jderose9.github.com

Name:           gnome-shell-extension-%{ename}
Version:        72
Release:        2%{?dist}
Summary:        Integrated icon taskbar and status panel for Gnome Shell
License:        GPL-2.0-or-later
URL:            https://github.com/home-sweet-gnome/dash-to-panel
Source0:        https://github.com/home-sweet-gnome/dash-to-panel/archive/v72/gnome-shell-extension-dash-to-panel-72.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell >= 45~rc

%description
Dash to Panel is an icon taskbar for Gnome Shell. This extension moves the dash
into the gnome main panel so that the application launchers and system tray are
combined into a single panel, similar to that found in KDE Plasma and Windows
7+. A separate dock is no longer needed for easy access to running and favorited
applications.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{ename}-%{version} -p1

%build
%make_build VERSION=%{version}

%install
%make_install VERSION=%{version}
rm -v %{buildroot}%{extdir}/{COPYING,README.md}

%find_lang %{ename}

%files -f %{ename}.lang
%license COPYING
%doc README.md
%{extdir}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{ename}.gschema.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 72-2
- Prepare for Oreon 11 (RP1)
