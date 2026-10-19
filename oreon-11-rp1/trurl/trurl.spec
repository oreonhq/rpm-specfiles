%global source0_hash aac947d4fb421a58abc19a3771e87942cd4721b8f855c433478c94c11a8203ba
Name:           trurl
Version:        0.16.1
Release:        1%{?dist}
Summary:        Command line tool for URL parsing and manipulation
License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch:          uppercase-hex.patch
Patch:          fix-discarded-qualifiers.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel
# /oreon:deps
%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%check

make test
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
