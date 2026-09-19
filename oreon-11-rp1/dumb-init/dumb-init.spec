%global source0_hash 3eda470d8a4a89123f4516d26877a727c0945006c8830b7e3bad717a5f6efc4e

Name:           dumb-init
Version:        1.2.5
Release:        15%{?dist}
Summary:        Entry-point for containers that proxies signals

License:        MIT
URL:            https://github.com/Yelp/dumb-init
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# pytest 7.2.0+ no longer installs the "py" library,
# which is used by dumb-init's test suite.
# Backported from upstream commit: https://github.com/Yelp/dumb-init/commit/b1a2551ad3c909384d97bca914f7c42cfdcdbf05
Patch0:         0000-update-for-pytest-7.2.0.patch

BuildRequires: gcc
BuildRequires: help2man
BuildRequires: make

BuildRequires: python3
BuildRequires: python3-pytest

%description
dumb-init is a simple process supervisor and init system designed to run as
PID 1 inside minimal container environments (such as Podman and Docker).

* It can handle orphaned zombie processes.
* It can pass signals properly for simple containers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
gcc -std=gnu99 %{optflags} -o %{name} dumb-init.c
help2man --no-discard-stderr --include debian/help2man --no-info --name '%{summary}' ./%{name} > %{name}.1

%check
PATH=.:$PATH timeout --signal=KILL 60 pytest-3 -vv tests/

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
