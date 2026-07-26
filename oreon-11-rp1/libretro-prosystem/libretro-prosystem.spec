%global source0_hash 7ede172f560ae79b0a5420f7be388d2c99f6cd1585547b021e85de6f32ccc87f

%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 4202ac5bdb2ce1a21f84efc0e26d75bb5aa7e248
%global corename prosystem

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.10.%autorelease
Summary:        Port of ProSystem to the libretro API

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
%license License.txt
%doc README.md
%{_libdir}/libretro/

%changelog
%autochangelog
