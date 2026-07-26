%global source0_hash e69a5e1c5626921a52951d19ce52d435ead0745951c1bff8b96516e1e20af80e

Name:       appmenu-qt5
Version:    0.3.0+16.10.20160628.1
Release:    41%{?dist}
Summary:    Support for global DBus-exported application menu in Qt5

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:    LGPL-3.0-only
URL:        https://launchpad.net/%{name}
Source0:    http://archive.ubuntu.com/ubuntu/pool/main/a/%{name}/%{name}_%{version}.orig.tar.gz

Patch1:     appmenu-qt5-0.3.0-fix-qt-compatibility.patch

BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  systemd-devel
BuildRequires: make

%description
This is a different, Qt5-compatible approach of the existing appmenu-qt
(https://launchpad.net/appmenu-qt).

%{name} is a Qt5 QPA theme plugin that adds support for application
menus to Qt5 applications.  This only works for Qt5 versions >= 5.2
currently.  To enable the support, set QT_QPA_PLATFORMTHEME=%{name}
in your environment or install the %{name}-profile.d package to
enable system-wide, see README.fedora *BEFORE* for further information.

%package profile.d
Summary:    Profile.d-config for %{name}

BuildArch:  noarch

Requires:   %{name}		== %{version}-%{release}
Requires:   setup

%description profile.d
This package contains profile.d-config-files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
%{__mkdir} -p %{_target_platform}

# Set permissions on integration-file.
%{__chmod} 0644 data/%{name}.sh

# Create %%{name}.csh for profile.d.
%{__cat} << EOF > data/%{name}.csh
setenv QT_QPA_PLATFORMTHEME %{name}
EOF
%{_bindir}/touch -r data/%{name}.sh data/%{name}.csh

# Create README.fedora
%{__cat} << EOF > README.fedora
This package contains a script named %{name}.sh, which activates
the global menu for Qt5 applications.

To activate it globally for all users, install %{name}-profile.d.
This is not recommended, because it works currently only with plasma-
widget-menubar in KDE SC4, all other desktops are not affected. It
would cause that the menubar of Qt5 applications is not visible there.
Unfortunately %{name} is its own Qt5-"platform", which means
enabling it breaks all other platform integration in Qt 5.  There is
not much you can do about that, but not enabling it.

To activate it for a certain user, integrate the contenst of the same
file located in %%doc into the appropriate autostart.
EOF

%build
pushd %{_target_platform}
%{qmake_qt5} CONFIG+=enable-by-default ../appmenu.pro
%make_build
popd

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%{__install} -pm 0644 data/%{name}.csh %{buildroot}%{_sysconfdir}/profile.d
# for some reason a cmake config gets pulled into the install
rm -fr %{buildroot}%{_libdir}/cmake

%files
%license COPYING
%doc data/%{name}.csh data/%{name}.sh README README.fedora
%{_libdir}/qt5/plugins/platformthemes/lib%{name}.so

%files profile.d
%{_sysconfdir}/profile.d/%{name}.*

%changelog
%autochangelog
