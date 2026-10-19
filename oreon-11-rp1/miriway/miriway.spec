%global source0_hash e80b763bbb3fde8c8a98c13f6380d6d64e9702816733fa1bd733ca4aa353a3b6
Name:           miriway
Version:        26.08.1
Release:        1%{?dist}
Summary:        Simple Wayland compositor built on Mir
License:        GPL-3.0-only
URL:            https://miriway.github.io/
Source0:        https://github.com/Miriway/Miriway/archive/v%{version}/Miriway-%{version}.tar.gz
Source1:        anaconda-initial-setup-run-gui-backend
Requires:       inotify-tools
Requires:       swaybg
Requires:       xkeyboard-config
Requires:       xorg-x11-server-Xwayland
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(miral)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Miriway is a starting point for creating a Wayland based
desktop environment using Mir.

%package        session
Summary:        Miriway desktop session
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    session
This package contains configuration and dependencies for
the basic Miriway session.

%package -n sddm-wayland-%{name}
Summary:        Miriway SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver
Requires:       %{name} = %{version}-%{release}
Requires:       layer-shell-qt
Requires:       sddm
Supplements:    (sddm and %{name})
BuildArch:      noarch
%description -n sddm-wayland-%{name}
This package contains configuration and dependencies for SDDM
to use Miriway for the Wayland compositor for the greeter.

%package -n initial-setup-gui-wayland-%{name}
Summary:        Run initial-setup GUI on Miriway
Provides:       firstboot(gui-backend)
Conflicts:      firstboot(gui-backend)
Requires:       %{name} = %{version}-%{release}
Requires:       initial-setup-gui >= 0.3.99
Supplements:    ((initial-setup or initial-setup-gui) and %{name})
Enhances:       (initial-setup-gui and %{name})
BuildArch:      noarch
%description -n initial-setup-gui-wayland-%{name}
This package contains configuration and dependencies for
the initial-setup GUI to use Miriway for the Wayland
compositor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Miriway-%{version} -S git_am

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt

%build

%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DSDDM=ON
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_bindir}/%{name}-{unconfine,unsnap}
mkdir -p %{buildroot}%{_prefix}/lib/sddm
mv %{buildroot}%{_sysconfdir}/sddm.conf.d %{buildroot}%{_prefix}/lib/sddm
mkdir -p %{buildroot}%{_libexecdir}/initial-setup
install -pm 0755 %{S:1} %{buildroot}%{_libexecdir}/initial-setup/run-gui-backend
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n miriway-session -f %{oreon_filedir}/miriway-session.list
%files -n sddm-wayland-miriway -f %{oreon_filedir}/sddm-wayland-miriway.list
%files -n initial-setup-gui-wayland-miriway -f %{oreon_filedir}/initial-setup-gui-wayland-miriway.list

%changelog

%autochangelog
