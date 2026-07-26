%global source0_hash d53c3f0af845045f39d6d633d295fd4efbe2a792fd0d04d25d44725d11c678ad

Name:       ddate   
Version:    0.2.2
Release:    25%{?dist}
Summary:    Convert Gregorian dates to Discordian dates
License:    LicenseRef-Fedora-Public-Domain
URL:        https://github.com/bo0ts/%{name}
Source0:    %{url}/archive/v%{version}.tar.gz
# Fix building with CMake 4, bug #2380534, in upstream after 0.2.2,
# <https://github.com/bo0ts/ddate/pull/25>
Patch0:     ddate-0.2.2-Fix-building-with-CMake-4.patch
BuildRequires:  cmake   
BuildRequires:  gcc
BuildRequires:  gzip

%description
This tool prints a date in the Discordian date format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%check
%{ctest}

%files
%doc README.org
%{_bindir}/ddate
%{_mandir}/man1/ddate.*

%changelog
%autochangelog
