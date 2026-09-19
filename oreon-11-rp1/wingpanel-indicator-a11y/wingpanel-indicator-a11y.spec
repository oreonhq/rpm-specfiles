%global source0_hash 8cd18c2a13eb5ec91e7fc12628349cc1980f234b61bd5b5ea81340b06f8a6999

%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-a11y
%global appname io.elementary.wingpanel.a11y

Name:           wingpanel-indicator-a11y
Summary:        Wingpanel Universal Access Indicator
Version:        1.0.2
Release:        5%{?dist}
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-a11y
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang a11y-indicator

%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml

%files -f a11y-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/liba11y.so
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.a11y.gschema.xml
%{_metainfodir}/%{appname}.metainfo.xml

%changelog
%autochangelog
