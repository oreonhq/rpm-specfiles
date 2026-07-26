%global source0_hash f5703bfde461172687f615a31d862fc6193f0329a737b2f92f5696a3bc704f66

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
%bcond doc %[ %{defined fc43} || %{defined fc42} ]

Name:           python-dictdiffer
Version:        0.9.0
Release:        19%{?dist}
Summary:        Dictdiffer is a module that helps you to diff and patch dictionaries

License:        MIT
URL:            https://github.com/inveniosoftware/dictdiffer
Source:         %{url}/archive/v%{version}/dictdiffer-%{version}.tar.gz

# tests: remove pytest-runner / setup.py test support
# https://github.com/inveniosoftware/dictdiffer/pull/192
# rebased on v0.9.0
Patch:          0001-tests-remove-pytest-runner-setup.py-test-support.patch
# Downstream-only: remove linting/coverage options for pytest
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0002-Downstream-only-remove-linting-coverage-options-for-.patch

# List test dependencies manually since the test extra has various unwanted
# dependencies, including linting/coverage tools:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

BuildArch:      noarch

%global common_description %{expand:
%{summary}.}

%description %{common_description}

%package -n python3-dictdiffer
Summary:        %{summary}

%if %{without doc} && %{defined fedora}
Obsoletes:      python-dictdiffer-doc < 0.9.0-18
%endif

%global common_description %{expand:
%{summary}.}

%description -n python3-dictdiffer %{common_description}

%pyproject_extras_subpkg -n python3-dictdiffer numpy

%if %{with doc}
%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dictdiffer-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x numpy %{?with_doc:-x docs}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dictdiffer

%if %{with doc}
PYTHONPATH='%{buildroot}%{python3_sitelib}' sphinx-build docs/ html
rm -rf html/.buildinfo html/.doctrees
%endif

%check
%pyproject_check_import

# Since this project does not use src layout, we must make sure pytest does not
# see both the “local” module and the one installed in the buildroot. The
# easiest thing to do is to explicitly test the local copy rather than the
# installed one by setting PYTHONPATH.
PYTHONPATH="${PWD}" %pytest

%files -n python3-dictdiffer -f %{pyproject_files}

%if %{with doc}
%files doc
%license LICENSE
%doc html/
%endif

%changelog
%autochangelog
