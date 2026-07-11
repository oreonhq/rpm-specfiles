%global source0_hash 27283b046942d369132966e5cdb0cdfb0bf64e32859b6d8028925d9fbf9cc946
%global gitcommit 930171a34e1de1e84f62c49beaa3eaeb8644915e

Name:           oreon-defense
Version:        0.1.0
Release:        1%{?dist}
Summary:        Oreon security app
License:        GPL-3.0-or-later
URL:            https://github.com/oreonhq/oreon-defense-cpp
Source0:        https://github.com/oreonhq/oreon-defense-cpp/archive/refs/tags/v%{version}.tar.gz
Source1:        oreon-defense.desktop

BuildRequires:  clamav-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libclamav)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)

Requires:       qt6-qtbase%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
Requires:       clamav-lib%{?_isa}
Requires:       clamav-data
Recommends:     firewalld

%description
Qt6 GUI for ClamAV, firewalld, and other Oreon security tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n oreon-defense-cpp-%{gitcommit}

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
install -Dpm 0755 %{__cmake_builddir}/oreon-defense %{buildroot}%{_bindir}/oreon-defense
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/oreon-defense.desktop

%files
%license LICENSE
%doc README.md TODO.md
%{_bindir}/oreon-defense
%{_datadir}/applications/oreon-defense.desktop

%changelog
%autochangelog
