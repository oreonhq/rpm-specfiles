%global source0_hash d244180c5f427afbbab58409f2d2e5247ffb0624bf33cf45b2488576d9467625

%global forgeurl https://github.com/libretro/libretro-%{corename}
%global commit 65d6b865544cd441ef2bd18cde7bd834c23d0e48
%global corename handy

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.10.%autorelease
Summary:        K. Wilkins' Atari Lynx emulator Handy (http://handy.sourceforge.net/) for libretro

License:        zlib
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

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
%make_install         \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro

%files
%license lynx/license.txt
%doc README.md
%{_libdir}/libretro/

%changelog
%autochangelog
