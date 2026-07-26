%global source0_hash 2cbf3d7e00ab2e9fe24b754a102644f6f334244980464c38233b18127f1deaec

Name:           python-testresources
Version:        2.0.2
Release:        %autorelease
Summary:        Testresources, a pyunit extension for managing expensive test resources
# mostly Apache-2.0 or BSD-3-Clause
# testresources/tests/TestUtil.py is GPL-2.0-or-later
License:        (Apache-2.0 OR BSD-3-Clause) AND GPL-2.0-or-later
URL:            https://github.com/testing-cabal/testresources
Source:         %{pypi_source testresources}
BuildArch:      noarch

%global _description %{expand:
testresources: extensions to python unittest to allow declarative use
of resources by test cases.}

%description %{_description}

%package -n python3-testresources
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-testresources %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n testresources-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l testresources

%check
%{python3} -m testtools.run testresources.tests.test_suite

%files -n python3-testresources -f %{pyproject_files}
# AUTHORS and COPYING are already included and marked as licenses, but
# Apache-2.0 and BSD are not.
%license Apache-2.0 BSD
%doc README.rst NEWS doc

%changelog
%autochangelog
