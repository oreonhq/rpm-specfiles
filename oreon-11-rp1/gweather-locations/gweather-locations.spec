%global source0_hash e7570a3661e0a752a06387b2032585cf588fc56770b1f9f39f1a55d17b2835fe

Name:           gweather-locations
Version:        2026.2
Release:        %autorelease
Summary:        The GWeather locations database

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gweather-locations
Source0:        https://download.gnome.org/sources/gweather-locations/2026/gweather-locations-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3-gobject-base
Requires:       %{name}-common = %{version}-%{release}

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

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%dir %{_libdir}/gweather-locations
%{_libdir}/gweather-locations/Locations.bin

%files devel
%{_datadir}/pkgconfig/gweather-locations.pc

%files common
%dir %{_datadir}/gweather-locations
%{_datadir}/gweather-locations/*

%changelog
%autochangelog
