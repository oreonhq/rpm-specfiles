%global source0_hash 53a6fb2b190ad37c5986caed3e98bede7c3c602399ee4f93c8fc054303d76dab
%global nm_version            1:1.8.0
%global mbp_version           0.20090602
%global old_libnma_version    1.10.4
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%bcond_without libnma_gtk4
%else
%bcond_with libnma_gtk4
%endif
Name:           libnma
Summary:        NetworkManager GUI library
Version:        1.10.6
Release:        11%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libnma/
Source0:        https://download.gnome.org/sources/libnma/1.10/%{name}-%{version}.tar.xz
Patch1:         0001-nm-applet-no-notifications.patch
Requires:       mobile-broadband-provider-info >= %{mbp_version}
Conflicts:      libnma < %{old_libnma_version}
Conflicts:      nm-connection-editor < 1.30.0
%if %{with libnma_gtk4}
%endif
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  ModemManager-glib-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  gcc
BuildRequires:  gcr-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  iso-codes-devel
BuildRequires:  meson
BuildRequires:  mobile-broadband-provider-info-devel
BuildRequires:  pkgconfig
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libnma-common -f %{oreon_filedir}/libnma-common.list
%files -n libnma-devel -f %{oreon_filedir}/libnma-devel.list
%files -n libnma-gtk4 -f %{oreon_filedir}/libnma-gtk4.list
%files -n libnma-gtk4-devel -f %{oreon_filedir}/libnma-gtk4-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.6-11
- Prepare for Oreon 11 (RP1)
