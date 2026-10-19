%global source0_hash 42d663d6b90fb5361ebc13f6547983d6f1e2ac75dc2ae4f1cac6ea6329965a25
Name:           mate-system-monitor
Version:        1.28.1
Release:        1%{?dist}
Summary:        Process and resource monitor
License:        GPL-2.0-or-later
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Requires: mate-desktop
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libgtop2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  polkit-devel
# /oreon:deps
%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-systemd \
        --enable-wnck
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
