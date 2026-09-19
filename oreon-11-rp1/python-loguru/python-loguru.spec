%global source0_hash 1cad8860aa0ecf9567125381e4430046526246e075224350a6a624addac05f5e

%bcond tests 1

Name:           python-loguru
Version:        0.7.3
Release:        %autorelease
Summary:        Python logging made (stupidly) simple

License:        MIT
URL:            https://github.com/Delgan/loguru
# The GitHub archive contains CHANGELOG.rst, which the PyPI sdist lacks.
Source:         %{url}/archive/%{version}/loguru-%{version}.tar.gz

# Fix deprecation warning raised by tests with Python 3.14
# https://github.com/Delgan/loguru/pull/1298
# Cherry-picked to 0.7.3
Patch:          0001-Fix-deprecation-warning-raised-by-tests-with-Python-.patch
# Fix failing "exception_modern" unit test with Python 3.14 (#1331)
# https://github.com/Delgan/loguru/commit/84023e2bd8339de95250470f422f096edcb8f7b7
Patch:          %{url}/commit/84023e2bd8339de95250470f422f096edcb8f7b7.patch

BuildArch:      noarch

BuildSystem:            pyproject
BuildOption(install):   -l loguru

# The dev extra pins exact versions and includes unwanted coverage tools etc.
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters), 
# and developer tools, so we enumerate test dependencies manually:
BuildRequires:  %{py3_dist colorama}
BuildRequires:  %{py3_dist freezegun}
BuildRequires:  %{py3_dist pytest}

# Normally we should not depend on typecheckers or linters, but the test that
# uses mypy is simply confirming that the stub file is valid and usable. That
# seems OK. Alternatively, we could pass --ignore=tests/test_type_hinting.py to
# %%pytest.
BuildRequires:  %{py3_dist mypy}

%global common_description %{expand:
Loguru is a library which aims to bring enjoyable logging in Python.}

%description %{common_description}

%package -n     python3-loguru
Summary:        %{summary}

%description -n python3-loguru %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n loguru-%{version} -p1

%check -a
%if %{with tests}
# Make sure we don’t run the detailed typing tests; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/typesafety/test_logger.yml"

%pytest ${ignore-} -k "${k-}" -rs
%endif

%files -n python3-loguru -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.md

%changelog
%autochangelog
