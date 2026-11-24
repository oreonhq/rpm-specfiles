# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2082ad2c38f438aa89ddc3028d52b312e8242ad9e678b63c0af107746264c11d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond tests 0
%else
%bcond tests 1
%endif

Name:           python-soupsieve
Version:        2.8.3
Release:        %{autorelease}
Summary:        CSS selector library

License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://github.com/facelessuser/soupsieve/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some
are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is. Soup Sieve
can also be imported in order to use its API directly for more controlled,
specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.}

%description %_description

%package -n python3-soupsieve
Summary:        %{summary}

%description -n python3-soupsieve %_description

%prep
%oreon_sha256
%autosetup -n soupsieve-%{version}

sed -i -e '/coverage/d' -e '/pytest-cov/d' requirements/tests.txt

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-r requirements/tests.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files soupsieve

%if %{with tests}
%check
%pytest -v
%endif

%files -n python3-soupsieve -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
