%global commit 0ece2e11960fed2b0aada10ea73efbda4773055c
%global source0_hash 2de662c4c84b16e9ab6a13165d9efc60b5ee996b2ab283091aa5c575b5ce6636

Name:           oreon-system-manager
Version:        0.1.1
Release:        2%{?dist}
Summary:        Oreon system management GUI
License:        GPL-3.0-or-later
URL:            https://github.com/oreonhq/oreon-system-manager
Source0:        https://github.com/oreonhq/oreon-system-manager/archive/%{commit}.tar.gz#/oreon-system-manager-%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  gtk4-devel
BuildRequires:  glib2-devel
BuildRequires:  graphene-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel

Requires:       gtk4%{?_isa}
Requires:       dnf
Requires:       polkit
Recommends:     docker
Recommends:     distrobox

%description
GTK4 GUI for package, repo, driver, and container management on Oreon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n oreon-system-manager-%{commit}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
install -Dpm 0755 target/release/oreon-system-manager %{buildroot}%{_bindir}/oreon-system-manager
install -Dpm 0644 packaging/oreon-system-manager.desktop %{buildroot}%{_datadir}/applications/oreon-system-manager.desktop
install -Dpm 0644 assets/logo.png %{buildroot}%{_datadir}/icons/hicolor/200x200/apps/oreon-system-manager.png

%files
%license LICENSE
%doc README.md
%{_bindir}/oreon-system-manager
%{_datadir}/applications/oreon-system-manager.desktop
%{_datadir}/icons/hicolor/200x200/apps/oreon-system-manager.png

%changelog
%autochangelog
