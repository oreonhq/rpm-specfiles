%global source0_hash 2ce5acf5a438b8f6dc1d14fd777a911be5eeb2f7ab9a7c4600166205b15d6536
%global _hardened_build 1
%define gtk3_version 2.99.2
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
%bcond x11 1
Name:           gdm
Epoch:          1
Version:        51.0
Release:        1%{?dist}
Summary:        The GNOME Display Manager
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GDM
Source0:        https://download.gnome.org/sources/%{name}/5%{_hardened_build}/%{name}-%{version}.tar.xz
Source1:        org.gnome.login-screen.gschema.override
Source2:        gdm.sysusers
Patch:          0001-Honor-initial-setup-being-disabled-by-distro-install.patch
Patch:          0001-data-add-system-dconf-databases-to-gdm-profile.patch
Patch:          0001-Add-headless-session-files.patch
%if %{with x11}
%endif
Provides: service(graphical-login) = %{name}
Requires: accountsservice
Requires: dbus-common
Requires: dconf
Requires: gnome-keyring-pam
Requires: gnome-session >= 50~alpha
Requires: gnome-session-wayland-session >= 50~alpha
Requires: gnome-settings-daemon >= 3.27.90
Requires: gnome-shell
Requires: iso-codes
Requires: libXau >= 1.0.4-4
Requires: pam
Requires: /sbin/nologin
Requires: systemd >= 186
Requires: system-logos
Requires: python3-pam
%if %{with x11}
Requires: xorg-x11-xinit
%endif
Provides: gdm-libs%{?_isa} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  dconf
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ply-boot-client)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  systemd-rpm-macros
BuildRequires:  which
BuildRequires:  yelp-tools
# /oreon:deps
%description
GDM, the GNOME Display Manager, handles authentication-related backend
functionality for logging in a user and unlocking the user's session after
it's been locked. GDM also provides functionality for initiating user-switching,
so more than one user can be logged in at the same time. It handles
graphical session registration with the system for both local and remote
sessions (in the latter case, via GNOME Remote Desktop and the RDP protocol).

%package devel
Summary: Development files for gdm
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gdm-pam-extensions-devel = %{epoch}:%{version}-%{release}
%description devel
The gdm-devel package contains headers and other
files needed to build custom greeters.

%package pam-extensions-devel
Summary: Macros for developing GDM extensions to PAM
Requires: pam-devel
%description pam-extensions-devel
The gdm-pam-extensions-devel package contains headers and other
files that are helpful to PAM modules wishing to support
GDM specific authentication features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -S git -p1 -n gdm-%{tarball_version}

%build

%meson -Ddbus-sys=%{_datadir}/dbus-1/system.d \
       -Ddefault-path=/usr/local/bin:/usr/bin \
       -Ddefault-pam-config=redhat \
       -Ddistro=redhat \
%if %{with x11}
       -Dx11-support=true \
%else
       -Dx11-support=false \
%endif
%meson_build
%install
%meson_install
cp -a %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/dconf/db/gdm.d/locks
%if %{with x11}
ln -sf ../X11/xinit/Xsession %{buildroot}%{_sysconfdir}/gdm/
%endif
%find_lang gdm --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post gdm.service
%preun

%systemd_preun gdm.service
%postun

%systemd_postun gdm.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
