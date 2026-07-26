%global source0_hash 2ba8244063434c6297751461e7d61a52b06aec171c63f747d7277a1e4bd7f6e1

%global commit 9b1fe3f623bd204b358f91fc5fd9ccfd3c68b7f4
%global commitdate 20260216
%global shortcommit %{sub %{commit} 1 7}

Name:           miracle-wm-config
Version:        0~git.%{commitdate}.2.%{shortcommit}
Release:        1%{?dist}
Summary:        Miracle Window Manager system configuration

License:        GPL-3.0-or-later
URL:            https://pagure.io/fedora-miracle/miracle-wm-config
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

Requires:       desktop-backgrounds-compat
Requires:       miracle-wm >= 0.8.3
Requires:       DankMaterialShell >= 1.2.3

BuildArch:      noarch

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{_libexecdir}/miracle-wm-dms-session
%dir %{_datadir}/miracle-wm
%{_datadir}/miracle-wm/default-config/
%{_datadir}/miracle-wm/DankMaterialShell-default-config/

%dnl ----------------------------------------------------------------

%package -n     initial-setup-gui-wayland-miraclewm
Summary:        Miracle-WM Wayland Initial Setup GUI configuration
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)

Requires:       xorg-x11-server-Xwayland
Requires:       initial-setup-gui >= 0.3.99
Requires:       miracle-wm >= 0.3.4
Supplements:    (initial-setup-gui and miracle-wm)

%description -n initial-setup-gui-wayland-miraclewm
This package contains configuration and dependencies for
Anaconda Initial Setup to use Miracle-WM for the display server.

%files -n initial-setup-gui-wayland-miraclewm
%license LICENSE
%{_libexecdir}/initial-setup/run-gui-backend

%dnl ----------------------------------------------------------------

%package -n     sddm-wayland-miraclewm
Summary:        Miracle-WM Wayland SDDM greeter configuration

Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver

Requires:       desktop-backgrounds-compat
Requires:       sddm >= 0.20.0
Requires:       layer-shell-qt
Requires:       miracle-wm >= 0.3.4

%description -n sddm-wayland-miraclewm
This package contains configuration and dependencies for SDDM
to use Miracle-WM for the greeter display server.

%files -n sddm-wayland-miraclewm
%license LICENSE
%{_prefix}/lib/sddm/sddm.conf.d/miracle-wm.conf

%dnl ----------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/miracle-wm/
cp -av miraclewm-config %{buildroot}%{_datadir}/miracle-wm/default-config
cp -av DankMaterialShell-config %{buildroot}%{_datadir}/miracle-wm/DankMaterialShell-default-config
rm %{buildroot}%{_datadir}/miracle-wm/DankMaterialShell-default-config/miracle-wm-dms-session

mkdir -p %{buildroot}%{_libexecdir}
install -pm 0755 DankMaterialShell-config/miracle-wm-dms-session %{buildroot}%{_libexecdir}/miracle-wm-dms-session

mkdir -p %{buildroot}%{_libexecdir}/initial-setup
install -pm 0755 initial-setup/run-gui-backend %{buildroot}%{_libexecdir}/initial-setup/

mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
install -pm 0644 sddm/miracle-wm.conf %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/

%changelog
%autochangelog
