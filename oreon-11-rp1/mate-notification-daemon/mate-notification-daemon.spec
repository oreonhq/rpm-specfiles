%global source0_hash d3090ea9d1a859e2def9c4d2319f9ac96a79b7a33598a97784db40be2508f668
%global branch 1.28
Name:          mate-notification-daemon
Version:       %{branch}.5
Release:        1%{?dist}
Summary:        Notification daemon for MATE Desktop
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Provides:      desktop-notification-daemon
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-panel-devel
# /oreon:deps
%description
Notification daemon for MATE Desktop

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-schemas-compile \
           --enable-x11 \
           --enable-wayland \
           --enable-in-process
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/mate-notification-properties.desktop
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
rm -f  %{buildroot}%{_datadir}/applications/mate-notification-daemon.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-notification-daemon.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
