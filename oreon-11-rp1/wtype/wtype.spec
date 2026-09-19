%global source0_hash da91786d828b6a6e29b884bc510473939eda052658ebef87d7bdeafa6a8746f9

Name:           wtype
Version:        0.4
Release:        %autorelease
Summary:        xdotool type for Wayland
License:        MIT

%global         forgeurl    https://github.com/atx/%{name}
%global         tag         v%{version}
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wtype
%{_mandir}/man1/wtype.1*

%changelog
%autochangelog
