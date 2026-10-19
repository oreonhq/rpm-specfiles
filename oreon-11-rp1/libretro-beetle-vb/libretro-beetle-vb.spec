%global source1_hash 968c296fffefabc7c1128ada95f7b26945a3b2f7a0e81d03d043bbde33e23698
%global source0_hash d2733026bde2b8049b8258f68d49954687ab43e2639d6a879c79cca68e91dea6
%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 8f837ebc077afdd6652efb2827fd8308a07113ca
%global corename beetle-vb
Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        1%{?dist}
Summary:        Standalone port of Mednafen VB to libretro
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{corename}-libretro-%{commit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_vb.libretro
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
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_vb.libretro
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
