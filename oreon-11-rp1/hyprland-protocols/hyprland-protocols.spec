%global source0_hash ab3525d8bad576db911d4ba1b586f303dd988660b3b8980022c1795fd574b165

Name:           hyprland-protocols
Version:        0.4.0
Release:        %autorelease
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

%description
%{summary}.

%package        devel
Summary:        Wayland protocol extensions for Hyprland

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files devel
%license LICENSE
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/

%changelog
%autochangelog
