# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6fdef854115f413e5d8a0241e1e67e93f0bd29c1d1317a742f3fdb189e1d57b5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname hyperlink

%global common_description %{expand:
The humble, but powerful, URL runs everything around us. Chances are you've
used several just to read this text. Hyperlink is a featureful, pure-Python
implementation of the URL, with an emphasis on correctness.}

Name:           python-%{srcname}
Version:        21.0.0
Release:        %{autorelease}
Summary:        A featureful, immutable, and correct URL for Python

License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-OFL
URL:            https://github.com/python-hyper/hyperlink
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

PYTHONPATH=%{pyproject_build_lib} sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
