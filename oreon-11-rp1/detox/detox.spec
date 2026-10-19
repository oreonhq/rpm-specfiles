%global source0_hash b3dac4f7fcfaa621c6fc5950a2c7e5747cdc9d78aacb9041875fad916b838e60
Name:		detox
Version:	3.0.1
Release:        1%{?dist}
Summary:        Utility to replace problematic characters in file names
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/dharple/detox
Source0:        https://github.com/dharple/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Detox is a utility designed to clean up file names. It replaces difficult to
work with characters, such as spaces, with standard equivalents. It will also
clean up file names with UTF-8 or Latin-1 (or CP-1252) characters in them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
