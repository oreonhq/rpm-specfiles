%global source0_hash 4a89468778e47a35ee413f83070188f47a1842f367de6dfb511cc390d635cf11

%bcond check 0
%global pypi_name filecheck
%global commit a630efd71cc5ad791162a6809334364b8a1c9e8f
%global shortcommit %%(c=%{commit}; echo ${c:0:7})

%global desc Python port of LLVM's FileCheck, flexible pattern matching file verifier.

Name: python-%{pypi_name}
Version: 0.0.24
Release: 10%{?dist}
Summary: Flexible pattern matching file verifier
License: Apache-2.0
URL: https://github.com/mull-project/FileCheck.py
Source0: https://github.com/mull-project/FileCheck.py/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# upstream testsuite includes only x86_64 reference binaries and Fedora llvm9.0 package doesn't include FileCheck
# https://bugzilla.redhat.com/show_bug.cgi?id=1939414
Patch0: %{name}-tests-x86_64.patch
# upstream testsuite measures code coverage
# that is discouraged in the packaging guidelines
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch1: %{name}-no-coverage.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: sed
%if %{with check}
BuildRequires: %{_bindir}/invoke
BuildRequires: %{_bindir}/lit
BuildRequires: %{_bindir}/python
BuildRequires: python3-pytest
BuildRequires: gcc
%endif

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n FileCheck.py-%{version}
sed -i -e '/#!.*python3/d' filecheck/filecheck.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
%pyproject_check_import
# lit seems to overwrite PYTHONPATH, so inject the buildroot paths directly
if ! grep -q %{buildroot} tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg ; then
cat << __EOF__ >> tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg

config.environment['PYTHONPATH'] = '%{buildroot}%{python3_sitelib}'
config.environment['PATH'] = '${PATH}:%{buildroot}%{_bindir}'
__EOF__
fi
%{_bindir}/invoke -e test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
