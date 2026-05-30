%global source0_hash 40e7aedd2232b8c3b58dac6aa365199359cf04bcee9127cafa441308690d504b

%global srcname iso8601
%global pkgdesc \
This module parses the most common forms of ISO 8601 date strings \
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

# Disable tests when building for RHEL to avoid test dependencies, unless
# building for EPEL.
%bcond tests %[%{undefined rhel} || %{defined epel}]

Name:           python-%{srcname}
Version:        2.1.0
Release:        8%{?dist}
Summary:        Simple module to parse ISO 8601 dates

License:        MIT
URL:            https://github.com/micktwomey/pyiso8601
Source:        https://github.com/micktwomey/pyiso8601/archive/refs/tags/2.1.0.tar.gz
# https://github.com/micktwomey/pyiso8601/pull/19
Patch:          0001-Add-docs-and-test-extras.patch
BuildArch:      noarch

%description %{pkgdesc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{pkgdesc}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import -e iso8601.test_iso8601
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license %{python3_sitelib}/%{srcname}-%{version}.dist-info/LICENSE
%doc README.rst

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-8
- Import
