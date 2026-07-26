%global source0_hash 004ac5ec08e9aba19fe11e82b6c64e124a0c729e25798847865d35c503032a19

%global qt6_minver 6.5

Name:           waycheck
Version:        1.7.0
Release:        3%{?dist}
Summary:        Simple GUI that displays protocols implemented by a Wayland compositor

# Icon is CC0, rest is Apache-2.0
License:        Apache-2.0 and CC0-1.0
URL:            https://gitlab.freedesktop.org/serebit/waycheck
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Core) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Gui) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6WaylandClient) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  pkgconfig(wayland-client)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%if 0%{?rhel} && 0%{?rhel} < 10
# Drop unsupported attribute
sed -e '/<url type="vcs-browser">.*/d' -i resources/dev.serebit.Waycheck.metainfo.xml
%endif

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSES/*
%doc README.md
%{_bindir}/waycheck
%{_datadir}/applications/dev.serebit.Waycheck.desktop
%{_metainfodir}/dev.serebit.Waycheck.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/dev.serebit.Waycheck.svg

%changelog
%autochangelog
