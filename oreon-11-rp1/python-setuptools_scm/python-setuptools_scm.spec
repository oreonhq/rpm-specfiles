# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4fa7dd82cf8c800df59c9a288c90299b1657ff1ecfc3f5cc00287c5dbf5e27a9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 1

Name:           python-setuptools_scm
Version:        10.2.1
Release:        %{autorelease}
Summary:        Blessed package to manage your versions by SCM tags

License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source0:        %{pypi_source setuptools_scm}

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  git-core
%if %{undefined rhel}
BuildRequires:  mercurial
%endif
%endif

%description
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.

%package -n python%{python3_pkgversion}-setuptools_scm
Summary:        %{summary}
%py_provides    python%{python3_pkgversion}-setuptools-scm

%description -n python%{python3_pkgversion}-setuptools_scm
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.

%pyproject_extras_subpkg -n python%{python3_pkgversion}-setuptools_scm simple,toml%{!?rhel:,rich}

%prep
%oreon_sha256
%autosetup -p1 -n setuptools_scm-%{version}
%pyproject_patch_dependency griffe:ignore
%pyproject_patch_dependency griffe-public-wildcard-imports:ignore
%pyproject_patch_dependency griffecli:ignore
%pyproject_patch_dependency mypy:ignore
%pyproject_patch_dependency ruff:ignore
%pyproject_patch_dependency flake8:ignore
%if %{defined rhel}
%pyproject_patch_dependency rich:ignore:br_only
%pyproject_patch_dependency pytest-timeout:ignore
%pyproject_patch_dependency pytest-xdist:ignore
sed -Ei '/^\[tool.pytest.ini_options\]/,/^\[/ { /^timeout/d }' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g test %{!?rhel:-x rich}} -x simple,toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files setuptools_scm

mv %{buildroot}%{_bindir}/setuptools-scm %{buildroot}%{_bindir}/setuptools-scm-%{python3_version}
%if "%{python3_pkgversion}" == "3"
ln -s ./setuptools-scm-%{python3_version} %{buildroot}%{_bindir}/setuptools-scm
%endif

%if %{with tests}
%check
%pytest -v %{!?rhel:-n auto} -k 'not test_pip_download and not test_xmlsec_download_regression and not test_get_version_blank_tag_regex and not test_setuptools_version_keyword_ensures_regex'
%endif

%files -n python%{python3_pkgversion}-setuptools_scm -f %{pyproject_files}
%doc README.md
%{_bindir}/setuptools-scm-%{python3_version}
%if "%{python3_pkgversion}" == "3"
%{_bindir}/setuptools-scm
%endif

%changelog
%autochangelog
