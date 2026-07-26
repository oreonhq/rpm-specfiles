%global source0_hash 3cf2107aa9f28600711f56df513e90a03bb80996db977250cf0b7fb8d9aee7dd

%global commit 41bbf185db8af3bd3443207510677ca87b2177de
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251228

Name:           gnome-shell-extension-pipewire-settings
Version:        9~git%{commitdate}.%{shortcommit}
Release:        2%{?dist}
Summary:        Minimal PipeWire configuration menu for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/gaheldev/pipewire-settings
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  gnome-shell-rpm-generators

Requires: gnome-shell(api) = 50

%description
A drop-down menu for GNOME Shell for configuring the PipeWire quantum and
sample rate values.

Setting a sample rate or buffer size will incite PipeWire to run with that
fixed value. Toggling Force Settings will force the graph to run at the
specified sample rate and buffer size unless set to dynamic. Toggling
Persist on restart will load the current configuration on restart,
however, settings can't be forced automatically on restart.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C

%build
# No build steps required

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/
cp -a pipewire-settings@gaheldev.github.com %{buildroot}%{_datadir}/gnome-shell/extensions/

%files
%license LICENSE.md
%doc README.md
%{_datadir}/gnome-shell/extensions/pipewire-settings@gaheldev.github.com/

%changelog
%autochangelog
