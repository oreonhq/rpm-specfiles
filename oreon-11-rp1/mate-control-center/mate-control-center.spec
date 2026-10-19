%global source0_hash e12d34c1c1f11e3d0a2ba2dd41bc1c997bf0d1d56486896756f6edaac5f9a9b2
%global branch 1.28
Name:          mate-control-center
Version:       %{branch}.1
Release:        1%{?dist}
Summary:        MATE Desktop control-center
License:       LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:           https://mate-desktop.org
Source0:        https://github.com/mate-desktop/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch1:        mate-control-center_0001-Fix-libsystemd-auto-detection.patch 
Requires: gsettings-desktop-schemas
Requires: mate-settings-daemon
Requires: gnome-keyring
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  accountsservice-devel
BuildRequires:  dconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libudisks2-devel
BuildRequires:  make
BuildRequires:  marco-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-menus-devel
BuildRequires:  mate-settings-daemon-devel
BuildRequires:  polkit-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description 
MATE Control Center configures system settings such as themes,
keyboards shortcuts, etc.

%package filesystem
Summary:      MATE Control Center directories
%description filesystem
The MATE control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%package devel
Summary:      Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for mate-control-center

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

#Patch 1
NOCONFIGURE=1 ./autogen.sh

%build

%configure                           \
           --disable-static          \
           --disable-schemas-compile \
           --disable-update-mimedb   \
           --enable-appindicator
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
desktop-file-install                                \
    --delete-original                               \
    --dir=%{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop
rm %{buildroot}%{_datadir}/applications/mimeinfo.cache
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-control-center-filesystem -f %{oreon_filedir}/mate-control-center-filesystem.list
%files -n mate-control-center-devel -f %{oreon_filedir}/mate-control-center-devel.list

%changelog

%autochangelog
