%global source0_hash 4ed7cdadaaa4c99efffc0282b8411703bb76e072c41c4b57989f8c5b40611a3a
%global branch 1.28
%global bootstrap 0
Name:          mate-settings-daemon
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        MATE Desktop settings daemon
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-settings-daemon_0001-build-escape-newline.patch
Patch2:        mate-settings-daemon_0002-plugins-add-missing-x11-linker-flags.patch
Patch3:        mate-settings-daemon_0003-configure.ac-don-t-link-plugins-with-no-undefined.patch
Patch4:        mate-settings-daemon_0004-Add-a-keyboard-shortcut-to-start-a-screen-reader-416.patch
Patch5:        mate-settings-daemon_0005-Remove-remaining-unused-references-to-dbus-glib.patch
Requires:       libmatekbd%{?_isa} >= 0:1.6.1-1
%if !0%{?bootstrap}
Requires:       mate-control-center-filesystem
%endif
# oreon:deps
BuildRequires:  dconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  nss-devel
BuildRequires:  polkit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%package devel
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build

%configure                             \
   --enable-pulse                      \
   --disable-static                    \
   --disable-schemas-compile           \
   --enable-polkit                     \
   --with-x                            \
   --with-nssdb
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-settings-daemon-devel -f %{oreon_filedir}/mate-settings-daemon-devel.list

%changelog

%autochangelog
