%global source0_hash e1f4630b2f8aea0edb76676afbfba9b92c819c6df5da68eb5b89da9c330e2fcd
Name:           afetch
Version:        2.2.0
Release:        11%{?dist}
Summary:        Simple system info written in C
License:        GPL-3.0-only
URL:            https://github.com/13-CF/afetch
Source0:        https://github.com/13-CF/%{name}/archive/V%{version}/%{name}-%{version}.tar.gz
Patch:          use_our_build_flags.patch
# oreon:deps
BuildRequires:  gcc
# /oreon:deps
%description
Fast and simple system info (for UNIX based operating systems)
written in POSIX compliant C99

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
