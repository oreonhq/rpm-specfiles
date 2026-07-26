%global source0_hash 22940585cc1e4b84fc588aaa940ea154c77356c512a1b5da2963d6c084e9da0b

%global commit d35e0874b5c1d350d831fdf9b94e234e6e7dfdb5
%global commitdate 20241103
%global shortcommit %{sub %{commit} 1 7}

%global cosmic_minver 1.0.0~alpha.3

Name:           cosmic-config-fedora
Version:        0~git.%{commitdate}.1.%{shortcommit}
Release:        5%{?dist}
Summary:        COSMIC default system configuration

License:        GPL-3.0-or-later
URL:            https://pagure.io/fedora-cosmic/cosmic-config-fedora
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Allow swapping with other versions if desired
Provides:       system-cosmic-config
Conflicts:      system-cosmic-config

Requires:       cosmic-comp >= %{cosmic_minver}
Requires:       cosmic-settings >= %{cosmic_minver}

BuildArch:      noarch

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/cosmic
%{_datadir}/cosmic/*

%dnl ----------------------------------------------------------------

%package -n     initial-setup-gui-wayland-cosmic
Summary:        COSMIC Wayland Initial Setup GUI configuration
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)

Requires:       xorg-x11-server-Xwayland
Requires:       initial-setup-gui >= 0.3.99
Requires:       cosmic-comp >= %{cosmic_minver}
Supplements:    (initial-setup-gui and cosmic-comp)

%description -n initial-setup-gui-wayland-cosmic
This package contains configuration and dependencies for
Anaconda Initial Setup to use COSMIC for the display server.

%files -n initial-setup-gui-wayland-cosmic
%license LICENSE
%{_libexecdir}/initial-setup/run-gui-backend

%dnl ----------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}
cp -av cosmic-config %{buildroot}%{_datadir}/cosmic

mkdir -p %{buildroot}%{_libexecdir}/initial-setup
install -pm 0755 initial-setup/run-gui-backend %{buildroot}%{_libexecdir}/initial-setup/

%changelog
%autochangelog
