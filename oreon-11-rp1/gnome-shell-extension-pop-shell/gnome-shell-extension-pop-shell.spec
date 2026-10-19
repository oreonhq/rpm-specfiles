%global source0_hash 1e580da52a08140f30024441ba954d7798301c3f4afe07d146f06a102719d0f1
%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      3cb093b8e6a36c48dd5e84533dc874ea74cd8a9e
%global shortcommit %{sub %{commit} 1 7}
Name:           gnome-shell-extension-%{extension}
Version:        1.2.0^28.%{shortcommit}
Release:        1%{?dist}
Summary:        GNOME Shell extension for advanced tiling window management
License:        GPL-3.0-only
URL:            https://github.com/pop-os/shell
BuildArch:      noarch
Source0:        https://github.com/pop-os/shell/archive/%{commit}/%{extension}-3cb093b.tar.gz
Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
Patch:          0001-Remove-schema-handling-from-transpile.sh.patch
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}
# oreon:deps
BuildRequires:  make
BuildRequires:  typescript
# /oreon:deps
%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.

%package shortcut-overrides
Summary:        Shortcut overrides for %{name}
%description shortcut-overrides
Shortcut overrides for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n shell-%{commit}

%build

%make_build compile
%install
%make_install
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-shell-extension-pop-shell-shortcut-overrides -f %{oreon_filedir}/gnome-shell-extension-pop-shell-shortcut-overrides.list

%changelog

%autochangelog
