%global source0_hash fdc30c2efdb03104912d1d607197b5e06108f15e16eaa3a8e93833f1ae2b17a1
%global require_ibus_version 1.4.0
Name:       ibus-m17n
Version:    1.4.39
Release:        1%{?dist}
Summary:        The M17N engine for IBus platform
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus-m17n
Source0:        https://github.com/ibus/%{name}/archive/%{version}/%{name}-%{version}.tar.gz#/ibus-m17n-1.4.39.tar.gz
Requires:   ibus >= %{require_ibus_version}
Requires:   m17n-lib
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gtk4-devel
BuildRequires:  ibus-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  m17n-lib-devel
BuildRequires:  make
# /oreon:deps
%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
autoreconf -fi

%build

%configure --disable-static --with-gtk=4.0
%{make_build}
%install
%{make_install}
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-m17n.desktop
make check
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.39-1
- Import
