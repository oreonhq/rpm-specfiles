%global source0_hash 53a6fb2b190ad37c5986caed3e98bede7c3c602399ee4f93c8fc054303d76dab

%global nm_version            1:1.8.0
%global mbp_version           0.20090602
%global old_libnma_version    1.10.4

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 10
%bcond_without libnma_gtk4
%else
%bcond_with libnma_gtk4
%endif

Name:           libnma
Summary:        NetworkManager GUI library
Version:        1.10.6
Release:        11%{?dist}
# The entire source code is GPLv2+ except some files in shared/ which are LGPLv2+
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libnma/
Source0:        https://download.gnome.org/sources/libnma/1.10/%{name}-%{version}.tar.xz

Patch1:         0001-nm-applet-no-notifications.patch

Requires:       mobile-broadband-provider-info >= %{mbp_version}

Conflicts:      libnma < %{old_libnma_version}
Conflicts:      nm-connection-editor < 1.30.0

BuildRequires:  gcc
BuildRequires:  NetworkManager-libnm-devel >= %{nm_version}
BuildRequires:  ModemManager-glib-devel >= 1.0
BuildRequires:  glib2-devel >= 2.38
BuildRequires:  gtk3-devel >= 3.12
%if %{with libnma_gtk4}
BuildRequires:  gtk4-devel >= 4.0
%endif
BuildRequires:  gobject-introspection-devel >= 0.10.3
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  iso-codes-devel
BuildRequires:  gcr-devel
BuildRequires:  mobile-broadband-provider-info-devel >= %{mbp_version}

Requires:       %{name}-common = %{version}-%{release}

%description
This package contains the library used for integrating GUI tools with
NetworkManager.


%package common
Summary:        Common files for NetworkManager GUI library
Conflicts:      libnma < %{version}-%{release}
BuildArch:      noarch

%description common
This package contains common files for the NetworkManager GUI library.


%package devel
Summary:        Header files for NetworkManager GUI library
Requires:       NetworkManager-libnm-devel >= %{nm_version}
Obsoletes:      NetworkManager-gtk-devel < 1:0.9.7
Requires:       libnma%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Conflicts:      libnma < %{old_libnma_version}

%description devel
This package contains header and pkg-config files to be used for integrating
GUI tools with NetworkManager.


%if %{with libnma_gtk4}
%package gtk4
Summary:        Experimental GTK 4 version of NetworkManager GUI library
Requires:       mobile-broadband-provider-info >= %{mbp_version}
Requires:       %{name}-common = %{version}-%{release}
Conflicts:      libnma < %{old_libnma_version}

%description gtk4
This package contains the experimental GTK4 version of library used for
integrating GUI tools with NetworkManager.


%package gtk4-devel
Summary:        Header files for experimental GTK4 version of NetworkManager GUI library
Requires:       NetworkManager-libnm-devel >= %{nm_version}
Requires:       libnma-gtk4%{?_isa} = %{version}-%{release}
Requires:       gtk4-devel%{?_isa}
Conflicts:      libnma < %{old_libnma_version}

%description gtk4-devel
This package contains the experimental GTK4 version of header and pkg-config
files to be used for integrating GUI tools with NetworkManager.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%meson \
        -Dgcr=true \
        -Dvapi=false \
%if %{with libnma_gtk4}
        -Dlibnma_gtk4=true \
%else
        -Dlibnma_gtk4=false \
%endif
%meson_build


%install
%meson_install
%find_lang %{name}


%check
%meson_test


%files
%{_libdir}/libnma.so.*
%{_libdir}/girepository-1.0/NMA-1.0.typelib


%files common -f %{name}.lang
%exclude %{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.eap.gschema.xml
%doc NEWS CONTRIBUTING
%license COPYING


%files devel
%{_includedir}/libnma
%{_libdir}/pkgconfig/libnma.pc
%{_libdir}/libnma.so
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_datadir}/gtk-doc


%if %{with libnma_gtk4}
%files gtk4
%{_libdir}/libnma-gtk4.so.*
%{_libdir}/girepository-1.0/NMA4-1.0.typelib


%files gtk4-devel
%{_includedir}/libnma
%{_libdir}/pkgconfig/libnma-gtk4.pc
%{_libdir}/libnma-gtk4.so
%{_datadir}/gir-1.0/NMA4-1.0.gir
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.6-11
- Prepare for Oreon 11 (RP1)
