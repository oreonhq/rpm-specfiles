%global source0_hash 3b88dc0f73ba14bf9f363b7369da5ceba76484b4dca018fcc5d606a79dea54ef

Name:           oreon-system-manager
Version:        0.1.0
Release:        1%{?dist}
Summary:        Oreon system management GUI
License:        GPL-3.0-or-later
URL:            https://github.com/oreonhq/oreon-system-manager
Source0:        https://github.com/oreonhq/oreon-system-manager/archive/refs/tags/v%{version}.tar.gz#/oreon-system-manager-%{version}.tar.gz
Source1:        oreon-system-manager.desktop

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)

Requires:       qt6-qtbase%{?_isa}
Requires:       dnf
Requires:       polkit
Recommends:     docker
Recommends:     distrobox

%description
Qt6 GUI for package, repo, driver, and container management on Oreon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n oreon-system-manager-%{version}

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/oreon-system-manager.desktop
install -Dpm 0644 assets/logo.png %{buildroot}%{_datadir}/pixmaps/oreon-system-manager.png

%files
%license LICENSE
%doc README.md
%{_bindir}/oreon-system-manager
%{_datadir}/applications/oreon-system-manager.desktop
%{_datadir}/pixmaps/oreon-system-manager.png

%changelog
%autochangelog
