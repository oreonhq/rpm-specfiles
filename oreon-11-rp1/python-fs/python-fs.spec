%global source0_hash c06b2570fe8cb425d0bda70c518becfc97b6e49bab289edae9359a4fb606d43e

%global srcname fs

# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

Name:           python-%{srcname}
Version:        2.4.16
Release:        17%{?dist}
Summary:        Python's Filesystem abstraction layer

# https://spdx.org/licenses/MIT.html
License:        MIT
URL:            https://pypi.org/project/fs/
Source0:        https://github.com/PyFilesystem/pyfilesystem2/archive/v%{version}/%{srcname}-%{version}.tar.gz#/python-fs-2.4.16.tar.gz

# Replace TestCase method aliases removed in Python 3.12
# https://github.com/PyFilesystem/pyfilesystem2/pull/570
# changelog fragment removed to avoid conflict
Patch:          570.patch

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(six)
%if %{with tests}
# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3-parameterized
%endif

%global _description %{expand:
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pyfilesystem2-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
%pyproject_check_import

# Almost all tests in tests/test_ftpfs.py need python3dist(pyftpdlib), which is
# packaged, but this imports from pyftpdlib.tests, which is not packaged.
ignore="${ignore-} --ignore=tests/test_ftpfs.py"

# Regressions related to URL formation in Python 3.14
# https://github.com/PyFilesystem/pyfilesystem2/issues/596
k="${k-}${k+ and }not test_complex_geturl"
# Matches test_geturl_for_fs but not test_geturl_for_fs_but_file_is_binaryio
k="${k-}${k+ and }not (test_geturl_for_fs and not binary)"

%pytest -k "${k-}" ${ignore-}
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md examples

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.16-17
- Import
