%global source0_hash 6a0f24a8f84a2f95e10114ab53e63fd4aca688a55fdc503ed650e0a410e3ea70
%global branch 1.28
Name:          mate-screensaver
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        MATE Screensaver
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-screensaver_0001-add-the-number-of-minutes-for-GUI-settings-to-lock-t.patch
Patch2:        mate-screensaver_0002-mate-screensaver-preferences-Add-mnemonic-for-backgr.patch
Patch3:        mate-screensaver_0003-mate-screensaver-preferences-Cleanup-UI-file-after-l.patch
Patch4:        mate-screensaver_0004-mate-screensaver-preferences-Add-missing-mnemonic.patch
Patch5:        mate-screensaver_0005-mate-screensaver-preferences-Add-tooltip-for-lock-de.patch
Patch6:        mate-screensaver_0006-mate-screensaver-preferences-Improve-and-cleanup-tim.patch
Requires:      redhat-menus
Requires:      system-logos
Requires:      gnome-keyring-pam
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-menus-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pam-devel
BuildRequires:  systemd-devel
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%package devel
Summary: Development files for mate-screensaver
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for mate-screensaver

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                          \
            --with-x                \
            --disable-schemas-compile \
            --enable-docbook-docs   \
            --with-mit-ext          \
            --with-xf86gamma-ext    \
            --with-libgl            \
            --with-shadow           \
            --enable-locking        \
            --with-systemd          \
            --enable-pam            \
            --without-console-kit
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install --delete-original             \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop
desktop-file-install                                          \
   --delete-original                                          \
   --dir %{buildroot}%{_datadir}/applications/screensavers    \
%{buildroot}%{_datadir}/applications/screensavers/*.desktop
mkdir -p %{buildroot}%{_docdir}/mate-screensaver
mv %{buildroot}%{_docdir}/mate-screensaver-%{version}/mate-screensaver.html %{buildroot}%{_docdir}/mate-screensaver/mate-screensaver.html
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mate-screensaver-devel -f %{oreon_filedir}/mate-screensaver-devel.list

%changelog

%autochangelog
