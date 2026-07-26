%global source0_hash 3c2d3b108eb70240afa48ed7efcdc24a304e1f974e06f9e91c7aeb020653d882

Name: did
Version: 0.22
Release: 7%{?dist}

Summary: What did you do last week, month, year?
License: GPL-2.0-or-later

URL: https://github.com/psss/did
Source0: %{url}/releases/download/%{version}/did-%{version}.tar.bz2

BuildArch: noarch
BuildRequires: git-core
BuildRequires: python3-bodhi-client
BuildRequires: python3-bugzilla
BuildRequires: python3-dateutil
BuildRequires: python3-devel
BuildRequires: python3-httplib2
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-requests-gssapi
BuildRequires: python3-setuptools
BuildRequires: python3-nitrate
Requires: python3-bugzilla
Requires: python3-httplib2
Requires: python3-nitrate
Requires: python3-requests-gssapi
Requires: python3-feedparser
Requires: python3-tenacity

%description
Comfortably gather status report data (e.g. list of committed
changes) for given week, month, quarter, year or selected date
range. By default all available stats for this week are reported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files did
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 did.1.gz %{buildroot}%{_mandir}/man1

%check
export LANG=en_US.utf-8
%pytest -vv tests/test*.py -k 'not smoke'

%files -f %{pyproject_files}
%{_mandir}/man1/*
%{_bindir}/did
%doc README.rst examples
%license LICENSE

%changelog
%autochangelog
