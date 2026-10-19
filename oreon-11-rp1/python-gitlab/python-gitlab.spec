%global source0_hash 628529ec4ce1f9a7ba2c145b2cf5e4eeca3015418e504b2e6fba70171b6b1b59
%global pypi_name gitlab
Name:           python-%{pypi_name}
Version:        8.5.0
Release:        1%{?dist}
Summary:        Interact with GitLab API
License:        LGPL-3.0-only
URL:            https://github.com/python-gitlab/python-gitlab
Source0:        https://files.pythonhosted.org/packages/source/p/python_gitlab/python_gitlab-%{version}.tar.gz
BuildArch:      noarch
Provides:  python-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python-%{pypi_name}-doc <= 3.3.0
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-gitlab = %{version}-%{release}
# /oreon:deps
%package -n       python3-gitlab+autocompletion
Summary:        Metapackage for python3-gitlab autocompletion extras
Requires:       python3-gitlab = %{version}-%{release}
Requires:       python3dist(argcomplete) >= 1.10.0
Requires:       python3dist(argcomplete) < 4
Provides:       python3dist(gitlab[autocompletion]) = %{version}-%{release}

%description -n python3-gitlab+autocompletion
Metapackage for python3-gitlab autocompletion extras.

%package -n       python3-gitlab+yaml
Summary:        Metapackage for python3-gitlab yaml extras
Requires:       python3-gitlab = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.1
Provides:       python3dist(gitlab[yaml]) = %{version}-%{release}

%description -n python3-gitlab+yaml
Metapackage for python3-gitlab yaml extras.

%package -n       python3-gitlab+graphql
Summary:        Metapackage for python3-gitlab graphql extras
Requires:       python3-gitlab = %{version}-%{release}
Requires:       python3dist(gql[httpx]) >= 3.5.0
Requires:       python3dist(gql[httpx]) < 5
Provides:       python3dist(gitlab[graphql]) = %{version}-%{release}

%description -n python3-gitlab+graphql
Metapackage for python3-gitlab graphql extras.

%description
Interact with GitLab API

%package -n     python3-%{pypi_name}
Summary:        Interact with GitLab API
%description -n python3-%{pypi_name}
Interact with GitLab API

%package -n python-%{pypi_name}-doc
Summary:        Python gitlab documentation
%description -n python-%{pypi_name}-doc
Documentation for gitlab

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python_%{pypi_name}-%{version}

# Relax some dependencies
sed -i 's/pytest==9\.*/pytest>=8.4.2,<10/'             requirements-lint.txt requirements-test.txt
sed -i 's/wheel==0\.*/wheel>=0.45.0,<1.0/'             requirements-test.txt

# not available in rawhide 11 Aug 2022
sed -i 's/pytest-console-scripts.*//'                  requirements-test.txt
sed -i 's/pytest-github-actions-annotate-failures.*//' requirements-test.txt

# coverage disabled
sed -i 's/pytest-cov.*//'                              requirements-test.txt
sed -i 's/coverage.*//'                                requirements-test.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/gitlab* usr/lib64/python3*/site-packages/gitlab* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%files
%files -n python3-gitlab -f %{oreon_filedir}/python3-gitlab.list
%files -n python-gitlab-doc -f %{oreon_filedir}/python-gitlab-doc.list

%changelog

%autochangelog
