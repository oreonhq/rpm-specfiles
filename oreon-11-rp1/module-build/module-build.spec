%global source0_hash f37b09989a0f3ae3b2d1e653458f3268beb36900839772ce5c6bf0e20ffc3394

Name: module-build
Version: 0.2.1
Release: 15%{?dist}
Summary: Tool/library for building module streams locally.
License: MIT
BuildArch: noarch

URL: https://github.com/mcurlej/module-build
Source0: https://github.com/mcurlej/module-build/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: libmodulemd >= 2.13.0
BuildRequires: python3-gobject
BuildRequires: mock

Requires: createrepo_c
Requires: libmodulemd >= 2.13.0
Requires: mock
Requires: mock-scm

%description
A library and a cli tool for building module streams. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/module_build
%{python3_sitelib}/module_build-*.egg-info/
%{_bindir}/module-build

%changelog
%autochangelog
