%global source0_hash e2194b2bcbc03540c0e44bb681b3365c10b4680c2f8689d130bc5d51cc43950b

%global short_version 2.14

Name:           crystal-dock
Summary:        Modern cross-desktop dock for the Linux Desktop
Version:        2.14.0
Release:        5%{?dist}

License:        GPL-3.0-only
URL:            https://github.com/dangvd/crystal-dock

Source0:        %{url}/archive/refs/tags/v%{short_version}.tar.gz

Patch0:         crystal-dock-fix-build-against-qt-6-10.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  cmake(LayerShellQt)

%description
Crystal Dock is a cool dock (desktop panel) for Linux desktop, with the
focus on attractive user interface, being simple and easy to customize,
and cross-desktop support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{short_version}

%build
cd src
%cmake
%cmake_build

%install
cd src
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/crystal-dock
%{_datadir}/applications/crystal-dock.desktop

%changelog
%autochangelog
