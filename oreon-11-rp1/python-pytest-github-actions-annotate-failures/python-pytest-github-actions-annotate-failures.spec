%global source0_hash 5dd18304512361788bc7b5c5c805db853f03f4950c6be09b088de6bab8e2e6c9
Name:           python-pytest-github-actions-annotate-failures
Version:        0.4.2
Release:        1%{?dist}
Summary:        pytest plugin to annotate failed tests with a workflow command for GitHub Actions
License:        MIT
URL:            https://github.com/pytest-dev/pytest-github-actions-annotate-failures
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_github_actions_annotate_failures/pytest_github_actions_annotate_failures-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.5
Requires:       python3-pytest-github-actions-annotate-failures = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-github-actions-annotate-failures
Summary:        pytest plugin to annotate failed tests with a workflow command for GitHub Actions
# oreon:reqs
Requires:       python3dist(pytest) >= 7.0.0
# /oreon:reqs
%description -n python3-pytest-github-actions-annotate-failures

%prep
%global oreon_srcdir pytest_github_actions_annotate_failures-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-github-actions-annotate-failures usr/lib/python3*/site-packages/pytest_github_actions_annotate_failures* usr/lib64/python3*/site-packages/pytest_github_actions_annotate_failures* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_github_actions_annotate_failures* usr/lib64/python3*/site-packages/pytest_github_actions_annotate_failures* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-github-actions-annotate-failures -f %{oreon_filedir}/python3-pytest-github-actions-annotate-failures.list

%changelog

%autochangelog
