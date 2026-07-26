%global source0_hash 906d88cfe52a1561fb7b026beba96467a4a827ed538a069fbba9249db11ac81a

%global forgeurl https://github.com/libretro/%{corename}
%global commit 60c204ca17941704110885a815a65c740572326f
%global corename bsnes-mercury

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.12.%autorelease
Summary:        Fork of bsnes with various performance improvements

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/bsnes_mercury_balanced.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
bsnes-mercury is a fork of higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%set_build_flags
%make_build \
    core_installdir=%{_libdir}/libretro \
    DEBUG=1

%install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro
sed -i 's!Balanced!performance!' %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro
sed -i 's!balanced!performance!' %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro

install -D -p -m 0755 bsnes_mercury_performance_libretro.so -t %{buildroot}%{_libdir}/libretro

%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/

%changelog
%autochangelog
