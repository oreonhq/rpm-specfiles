%global source0_hash 8ebdcb74b607e868336ba9a8146cdef8f97bce535c2b0cb3bf650c58f71eee21
%global branch 1.28
Name:          mate-power-manager
Version:       %{branch}.1
Release:        1%{?dist}
Summary:        MATE power management service
License:       GPL-2.0-or-later
URL:           http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-power-manager_0001-Keyboard-backlight-handling-improvements-404.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libsecret-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-panel-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  polkit-devel
BuildRequires:  popt-devel
BuildRequires:  upower-devel
# /oreon:deps
%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
     --disable-schemas-compile
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%find_lang %{name} --with-gnome --all-name
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
