%global source0_hash 5f0122405b18e0a95f4a5da2ef2f57b4bf1895a691370e65cc19fd5854a50412

%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 139fe34c8dfc5585d6ee1793a7902bca79d544de
%global corename beetle-ngp

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.10.%autorelease
Summary:        Standalone port of Mednafen NGP to the libretro API, itself a fork of Neopop

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_ngp.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}

%install
%make_install \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_ngp.libretro

%files
%license COPYING
%doc readme.md
%{_libdir}/libretro/

%changelog
%autochangelog
