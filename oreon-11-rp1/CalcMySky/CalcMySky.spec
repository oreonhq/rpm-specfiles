%global source0_hash 1096f3c6067e05dd8c4df601b745cca5e88b843ad1328938e5dba69c1fcfb84f
Name: CalcMySky
Version:  0.4.0
Release:        4%{?dist}
Summary:        Simulator of light scattering by planetary atmospheres
License: GPL-2.0-or-later
URL: https://github.com/10110111/CalcMySky
Source0:        https://github.com/10110111/CalcMySky/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%package devel
Summary: Development files for CalcMySky
Requires: %{name}%{?_isa} = %{version}-%{release}
%description
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

%description devel
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

These are the development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DQT_VERSION=6
%cmake_build
%install
%cmake_install
%oreon_autofiles CalcMySky-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n CalcMySky-devel -f %{oreon_filedir}/CalcMySky-devel.list

%changelog

%autochangelog
