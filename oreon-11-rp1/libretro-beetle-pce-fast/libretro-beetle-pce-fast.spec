%global source1_hash 94fd01c88775810cce0222fc6df8be15277d13045a69cc0b9193e874bd2d13c5
%global source0_hash 8a82f29a13c53fec049c8aeef2ddccba90830d4a6a341ce8c94772a643bac19f
%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 7e9b257b8a591cb7e00f9e55371edba19db9799c
%global corename beetle-pce-fast
Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        1%{?dist}
Summary:        Standalone port of Mednafen PCE Fast to libretro
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{corename}-libretro-%{commit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_pce_fast.libretro
Supplements:    gnome-games
Supplements:    retroarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Beetle PC Engine Fast is a port/fork of Mednafen's PC Engine Fast "pce_fast"
module to the libretro API. This libretro core contains CD-ROM2 support but
unlike Mednafen's PCE Fast module, lacks SuperGrafx support. SuperGrafx support
is available in the Beetle SuperGrafx core or the Beetle PC Engine "pce" core.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%set_build_flags
%make_build GIT_VERSION=%{shortcommit}
%install
%make_install \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -m0644 -Dp %{SOURCE1} \
    %{buildroot}%{_libdir}/libretro/mednafen_pce_fast.libretro
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
