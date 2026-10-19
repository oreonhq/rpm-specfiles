%global source0_hash e7570a3661e0a752a06387b2032585cf588fc56770b1f9f39f1a55d17b2835fe
Name:           gweather-locations
Version:        2026.2
Release:        1%{?dist}
Summary:        The GWeather locations database
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gweather-locations
Source0:        https://download.gnome.org/sources/gweather-locations/2026/gweather-locations-%{version}.tar.xz
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
The GWeather locations database used by GWeather library.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development files for %{name}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        common
BuildArch:      noarch
Summary:        Data files in non-binary format for %{name}
%description common
The %{name}-common contains data files in non-binary format.

%global debug_package %{nil}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gweather-locations-devel -f %{oreon_filedir}/gweather-locations-devel.list
%files -n gweather-locations-common -f %{oreon_filedir}/gweather-locations-common.list

%changelog

%autochangelog
