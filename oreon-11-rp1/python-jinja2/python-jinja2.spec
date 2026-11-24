# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname jinja2

Name:           python-jinja2
Version:        3.1.6
Release:        1%{?dist}
Summary:        General purpose template engine
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        %{pypi_source %srcname}

%if 0%{?rhel} || 0%{?flatpak} || 0%{?oreon}
%bcond_with docs
%else
%bcond_without docs
%endif
%if 0%{?oreon}
%bcond asyncio_tests 0
%else
%bcond asyncio_tests %{undefined rhel}
%endif

BuildArch:      noarch

%global _description %{expand:
Jinja2 is a template engine written in pure Python. It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.}

%description %_description

%package -n python3-jinja2
Summary:        %{summary}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{with asyncio_tests}
BuildRequires:  python3-trio
%endif
%if %{with docs}
BuildRequires:  %{_bindir}/sphinx-build-3
BuildRequires:  make
BuildRequires:  python3-Pallets-Sphinx-Themes >= 2
BuildRequires:  python3-sphinxcontrib-log-cabinet
BuildRequires:  python3-sphinx-issues
%endif

%description -n python3-jinja2 %_description

%pyproject_extras_subpkg -n python3-jinja2 i18n

%prep
%oreon_sha256
%autosetup -p1 -n %{srcname}-%{version}

%pyproject_patch_dependency flit_core:set_upper:5

%generate_buildrequires
%pyproject_buildrequires -x i18n

%build
%pyproject_wheel
%if %{with docs}
make -C docs html PYTHONPATH=$(pwd)/src SPHINXBUILD=sphinx-build-3
rm -rvf docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files jinja2

%check
%pytest tests -k "not test_elif_deep" %{!?with_asyncio_tests:--ignore tests/test_async.py --ignore tests/test_async_filters.py}

%files -n python3-jinja2 -f %{pyproject_files}
%doc README.md
%doc docs/examples
%license LICENSE.txt
%if %{with docs}
%doc docs/_build/html
%endif

%changelog
%autochangelog
