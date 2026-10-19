%global source1_hash f0595712debf5a29487f6ec998e8973a1cb5bbf95ba943b1059fdf19165f5cbc
%global source0_hash 08976546ed707e7d83a1e4b1204bba8e854f41c0a0a9d8d5d8447c4489fb1fe0
%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 8ab051edd4816f33a5631d230d54059eeed52c5f
%global corename stella2014
Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        1%{?dist}
Summary:        Port of Stella to libretro
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{corename}-libretro-%{commit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro
Suggests:       gnome-games
Suggests:       retroarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
