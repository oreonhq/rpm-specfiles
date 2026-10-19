%global source0_hash ef6c8906270a82f062bfbd5dd5af1b14c7d6e4c77aa436cae483e28be6942383
Name:           jello
Version:        1.6.1
Release:        1%{?dist}
Summary:        Query JSON at the command line with Python syntax
License:        MIT
URL:            https://github.com/kellyjonbrazil/jello
Source0:        https://github.com/kellyjonbrazil/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jello = %{version}-%{release}
# /oreon:deps
%description
Query, filter, and transform JSON and JSON Lines at the command line with
Python syntax.

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 man/*
%oreon_autofiles main

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%{py3_test_envvars} ./runtests.sh
%files

%changelog

%autochangelog
