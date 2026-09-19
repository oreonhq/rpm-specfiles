%global source0_hash e1f4630b2f8aea0edb76676afbfba9b92c819c6df5da68eb5b89da9c330e2fcd

Name:           afetch
Version:        2.2.0
Release:        11%{?dist}
Summary:        Simple system info written in C

License:        GPL-3.0-only
URL:            https://github.com/13-CF/afetch
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

# https://github.com/13-CF/afetch/pull/94
Patch:          use_our_build_flags.patch

%description
Fast and simple system info (for UNIX based operating systems)
written in POSIX compliant C99

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%if 0%{?rhel} || 0%{?fedora} < 36
%set_build_flags
%endif
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
