%global source0_hash none

# RHEL does not include all the test dependencies
%bcond tests %{undefined rhel}

%global srcname requests-ftp

Name:           python-%{srcname}
Version:        0.3.1
Release:        43%{?dist}
Summary:        FTP transport adapter for python-requests

License:        Apache-2.0
URL:            https://github.com/Lukasa/requests-ftp

# the last pypi release was 0.3.1, from commit 20ce5bf5388ae9b9edfdd9bf6d381a399e5bcad0 but without test data
%global commit d959118dbfc1f04c9726dfff48d5a2a64c1a01f2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/Lukasa/requests-ftp/archive/d959118dbfc1f04c9726dfff48d5a2a64c1a01f2/requests-ftp-%(c=d959118dbfc1f04c9726dfff48d5a2a64c1a01f2;.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Remove use of the cgi module, which is only used to implement STOR
Patch6:         0001-Remove-use-of-the-cgi-module.patch

Patch7:         0001-Relax-the-test-requirement-versions.patch
Patch8:         0001-Add-explicit-schemes-to-the-proxy-URLs.patch

%description
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

%package -n python3-%{srcname}
Summary:        FTP transport adapter for python3-requests

%description -n python3-requests-ftp
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

This is the Python 3 version of the transport adapter module.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:test_requirements.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requests_ftp

%check
%pyproject_check_import
%if %{with tests}
%pytest tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.1-43
- Prepare for Oreon 11 (RP1)
