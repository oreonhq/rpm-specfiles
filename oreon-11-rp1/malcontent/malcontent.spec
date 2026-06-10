%global source0_hash 951c2732106254b2f4d22c06061d1a813d8b6310a045afc638c1e1a0c97e4e69
%global source1_hash 32673cfe72e0527b086af92a288add310166f7363a118191f64059e22d45dd0a
%global source2_hash 14f082f122eb4e495e2ac96f235efb01525ae5d4a1f0fd98148b4f7c7f95ccd2
%global source3_hash 469de2d445bf54880f652f4b6dc95c7cdf6f5502c35524a45b2122d70d47ebc2

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           malcontent
Version:        0.14.0
Release:        1%{?dist}
Summary:        Parental controls implementation
License:        LGPL-2.1-only AND CC-BY-3.0
URL:            https://gitlab.freedesktop.org/pwithnall/malcontent/
Source0:        https://tecnocode.co.uk/downloads/malcontent/malcontent-%{tarball_version}.tar.xz
Source1:        https://gitlab.gnome.org/pwithnall/libgsystemservice/-/archive/0.3.0/libgsystemservice-0.3.0.tar.bz2
Source2:        https://github.com/GNOME/gvdb/archive/c6f2359cc1d00f16e0a0e2527fa0bc1882b8b5ab.tar.gz
Source3:        http://www.corpit.ru/mjt/tinycdb/tinycdb-0.81.tar.gz

BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-testing-0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pam-devel
BuildRequires:  gtk-doc
BuildRequires:  libsoup3-devel

Provides:       bundled(gvdb)
Provides:       bundled(libgsystemservice)
Provides:       bundled(tinycdb)

Requires: polkit

%description
libmalcontent implements parental controls support which can be used by
applications to filter or limit the access of child accounts to inappropriate
content.

%package control
Summary:        Parental Controls UI
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description control
Parental controls UI for malcontent.

%package pam
Summary:        Parental Controls PAM Module

%description pam
PAM module for malcontent time limits.

%package tools
Summary:        Parental Controls Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
CLI tools for malcontent.

%package ui-devel
Summary:        Development files for libmalcontent-ui
Requires:       %{name}-ui-libs%{?_isa} = %{version}-%{release}

%description ui-devel
Development files for libmalcontent-ui.

%package ui-libs
Summary:        Libraries for %{name}

%description ui-libs
libmalcontent-ui.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for libmalcontent.

%package libs
Summary:        Libraries for %{name}

%description libs
libmalcontent runtime library.

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for libmalcontent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n malcontent-%{tarball_version} -S git
tar -xf %{SOURCE1} -C subprojects
mv subprojects/libgsystemservice-0.3.0 subprojects/libgsystemservice
mkdir -p subprojects/gvdb
tar -xf %{SOURCE2} -C subprojects/gvdb --strip-components=1
tar -xf %{SOURCE3} -C subprojects
cp subprojects/packagefiles/tinycdb/meson.build subprojects/tinycdb-0.81

%build
%meson -Dui=enabled -Dinstalled_tests=false
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.freedesktop.MalcontentControl.metainfo.xml

%files -f malcontent.lang
%license COPYING COPYING-DOCS
%doc README.md
%{_datadir}/accountsservice/interfaces/
%{_datadir}/dbus-1/interfaces/
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/com.endlessm.ParentalControls.rules
%{_libexecdir}/malcontent-timer-extension-agent
%{_libexecdir}/malcontent-timerd
%{_libexecdir}/malcontent-webd
%{_libexecdir}/malcontent-webd-update
%{_datadir}/dbus-1/services/org.freedesktop.MalcontentControl.service
%{_datadir}/dbus-1/system-services/org.freedesktop.MalcontentTimer1.ExtensionAgent.service
%{_datadir}/dbus-1/system-services/org.freedesktop.MalcontentTimer1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.MalcontentWeb1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.MalcontentTimer1.ExtensionAgent.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.MalcontentTimer1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.MalcontentWeb1.conf
%{_mandir}/man8/malcontent-timer-extension-agent.8*
%{_mandir}/man8/malcontent-timerd.8*
%{_mandir}/man8/malcontent-webd.8*
%{_unitdir}/malcontent-timer-extension-agent.service
%{_unitdir}/malcontent-timerd.service
%{_unitdir}/malcontent-webd-update.service
%{_unitdir}/malcontent-webd-update.timer
%{_unitdir}/malcontent-webd.service
%{_sysusersdir}/malcontent-timer-extension-agent.conf
%{_sysusersdir}/malcontent-timerd.conf
%{_sysusersdir}/malcontent-webd.conf
%exclude %{_libexecdir}/installed-tests/malcontent-webd-update-1/malcontent-webd-template.py

%files control
%license COPYING
%doc README.md
%{_bindir}/malcontent-control
%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.MalcontentControl.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.freedesktop.MalcontentControl-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.MalcontentControl.metainfo.xml

%files pam
%license COPYING
%{_libdir}/security/pam_malcontent.so

%files tools
%license COPYING
%{_bindir}/malcontent-client
%{_mandir}/man8/malcontent-client.8.*

%files ui-devel
%license COPYING
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MalcontentUi-1.gir
%{_libdir}/libmalcontent-ui-1.so
%{_includedir}/malcontent-ui-1/
%{_libdir}/pkgconfig/malcontent-ui-1.pc

%files ui-libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/MalcontentUi-1.typelib
%{_libdir}/libmalcontent-ui-1.so.*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Malcontent-0.gir
%{_includedir}/malcontent-0/
%{_libdir}/libmalcontent-0.so
%{_libdir}/pkgconfig/malcontent-0.pc

%files libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Malcontent-0.typelib
%{_libdir}/libmalcontent-0.so.*
%{_libdir}/libnss_malcontent.so*

%files doc
%{_docdir}/libmalcontent-0
%{_docdir}/libmalcontent-ui-1

%changelog
* Tue Jun 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.0-1
- import for oreon 11 iso
