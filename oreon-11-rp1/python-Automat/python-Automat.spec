# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b34227cf63f6325b8ad2399ede780675083e439b20c323d376373d8ee6306d88
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond doc 0
%else
%bcond doc %{undefined rhel}
%endif

%global srcname Automat
%global libname automat

%global common_description %{expand:
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).}

Name:           python-%{srcname}
Version:        24.8.1
Release:        %{autorelease}
Summary:        Self-service finite-state machines for the programmer on the go

License:        MIT
URL:            https://github.com/glyph/automat
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
%if %{with doc}
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-pydoctor
%endif

Patch:          sphinx-no-git.patch

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       python3-%{libname}

%description -n python3-%{srcname} %{common_description}

%if %{with doc}
%package -n python-%{srcname}-doc
Summary:        Automat documentation

%description -n python-%{srcname}-doc
Documentation for Automat
%endif

%prep
%oreon_sha256
%autosetup  -p1 -n %{libname}-%{version}

sed -i "s/py\.test/pytest/g" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%if %{with doc}
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/automat-visualize

%if %{with doc}
%files -n python-%{srcname}-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
