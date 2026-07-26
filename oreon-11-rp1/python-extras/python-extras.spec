%global source0_hash 132e36de10b9c91d5d4cc620160a476e0468a88f16c9431817a6729611a81b4e

%bcond bootstrap 0

Name:           python-extras
Version:        1.0.0
Release:        43%{?dist}
Summary:        Useful extra bits for Python

License:        MIT
URL:            https://github.com/testing-cabal/extras
Source:         %{pypi_source extras}

BuildArch:      noarch

%global _description %{expand:
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.}

%description %_description

%package -n python3-extras
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{without bootstrap}
BuildRequires:  python3-testtools
%endif

%description -n python3-extras %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n extras-%{version}
# don't include extras.tests
sed -e '/extras\.tests/d' -i setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l extras

%check
%if %{with bootstrap}
%pyproject_check_import
%else
%{py3_test_envvars} %{python3} -m testtools.run extras.tests.test_suite
%endif

%files -n python3-extras -f %{pyproject_files}
%doc NEWS README.rst

%changelog
%autochangelog
