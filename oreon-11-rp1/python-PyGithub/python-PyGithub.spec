%global source0_hash 6c50af579b1512d724e9f14bdbfb49e15f6e575f2221d8d685c7132cfebcec81

Name:           python-PyGithub
Version:        2.7.0
Release:        %autorelease
Summary:        Python library to work with the Github API
License:        LGPL-3.0-or-later
URL:            https://github.com/PyGithub/PyGithub
# github tarball (unlike PyPI one) contains tests
Source:         %{url}/archive/v%{version}/PyGithub-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
A Python library implementing the full Github API v3.}

%description %{_description}

%package -n     python3-pygithub
Summary:        %{summary}
BuildRequires:  python3-devel

Provides:       python3-github = %{version}-%{release}
Obsoletes:      python3-github < 1.25.2-2
Provides:       python3-PyGithub = %{version}-%{release}
Obsoletes:      python3-PyGithub < 1.29-8

%description -n python3-pygithub %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n PyGithub-%{version}

# Remove linter(s) from test requirements
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# Also remove other unnecessary pytest add-ons
sed \
    -e '/pytest-cov/d' \
    -e '/pytest-github-actions-annotate-failures/d' \
    -e '/pytest-subtests/d' \
    -i requirements/test.txt

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires requirements/test.txt

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l github

%check
%pytest -v

%files -n python3-pygithub -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
