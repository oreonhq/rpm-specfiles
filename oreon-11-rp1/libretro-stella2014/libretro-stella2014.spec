%global source0_hash 08976546ed707e7d83a1e4b1204bba8e854f41c0a0a9d8d5d8447c4489fb1fe0

%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 8ab051edd4816f33a5631d230d54059eeed52c5f
%global corename stella2014

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.7.%autorelease
Summary:        Port of Stella to libretro

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

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
%license stella/license.txt
%doc README.md
%{_libdir}/libretro/

%changelog
%autochangelog
