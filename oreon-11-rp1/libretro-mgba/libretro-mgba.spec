%global source0_hash 85bc2c015d60021250d9c923d56a38e096d339a2513f483e549eeb2d2857b097

%global forgeurl https://github.com/libretro/%{corename}
%global commit b2564482c86378581a7a43ef4e254b2a75167bc7
%global corename mgba

Name:           libretro-%{corename}
Version:        0.1.1
%forgemeta
Release:        0.9.%autorelease
Summary:        mGBA Game Boy Advance Emulator

License:        MPL-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and
more accurate than many existing Game Boy Advance emulators, as well as adding
features that other emulators lack. It also supports Game Boy and Game Boy Color
games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}

%install
%make_install         \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro

%files
%license LICENSE
%doc README.md PORTING.md CONTRIBUTING.md CHANGES
%{_libdir}/libretro/

%changelog
%autochangelog
