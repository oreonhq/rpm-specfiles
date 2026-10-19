%global source0_hash 330062455ead40d0603151df7b84359daf2ce2958a932f96f92c1226370fa1e4
%global pypi_name op1repacker
%global common_description %{expand:
OP-1 Firmware Repacker is the tool for unpacking and repacking OP-1 synthesizer
firmware. This allows you to access and modify the files within the firmware as
well as repacking the files into a valid installable firmware file. Ready made
mods are also included in the tool. Lastly it is also possible to analyze
unpacked firmware to get information such as build version, build time and
date, bootloader version etc.}
Name:           python-%{pypi_name}
Version:        0.2.6
Release:        19%{?dist}
Summary:        Tool for unpacking, modding and repacking OP-1 firmware
License:        MIT
URL:            https://github.com/op1hacks/op1repacker
Source0:        https://github.com/op1hacks/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed
# /oreon:deps
%description
%{common_description}

%package -n     %{pypi_name}
Summary:        Tool for unpacking, modding and repacking OP-1 firmware
%description -n %{pypi_name}
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n op1repacker -f %{oreon_filedir}/op1repacker.list

%changelog

%autochangelog
