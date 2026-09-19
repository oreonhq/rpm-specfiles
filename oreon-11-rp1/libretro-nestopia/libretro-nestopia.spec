%global source0_hash f38b99c25d7359582031b15731fcc5a0876144dd2189983a69357c370e54979b

%global forgeurl https://github.com/libretro/%{corename}
%global commit b99ede358b2219602443e7f414eabf81e17da244
%global corename nestopia

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.9.%autorelease
Summary:        Nestopia emulator with libretro interface

License:        GPL-2.0-only
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
%make_build -C libretro GIT_VERSION=%{shortcommit}

%install
%make_install         \
    -C libretro       \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro

%files
%license COPYING
%{_libdir}/libretro/

%changelog
%autochangelog
