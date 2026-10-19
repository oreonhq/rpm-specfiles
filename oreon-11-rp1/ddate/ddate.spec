%global source0_hash d53c3f0af845045f39d6d633d295fd4efbe2a792fd0d04d25d44725d11c678ad
Name:       ddate   
Version:    0.2.2
Release:        1%{?dist}
Summary:        Convert Gregorian dates to Discordian dates
License:    LicenseRef-Fedora-Public-Domain
URL:        https://github.com/bo0ts/%{name}
Source0:        https://github.com/bo0ts/%{name}/archive/v%{version}.tar.gz
Patch0:     ddate-0.2.2-Fix-building-with-CMake-4.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gzip
# /oreon:deps
%description
This tool prints a date in the Discordian date format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{cmake}
%{cmake_build}
%install
%{cmake_install}
%oreon_autofiles main

%check

%{ctest}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
