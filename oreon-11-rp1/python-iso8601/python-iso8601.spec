%global source0_hash 40e7aedd2232b8c3b58dac6aa365199359cf04bcee9127cafa441308690d504b
%global srcname iso8601
%global pkgdesc \
This module parses the most common forms of ISO 8601 date strings \
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.
%bcond tests %[%{undefined rhel} || %{defined epel}]
Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Simple module to parse ISO 8601 dates
License:        MIT
URL:            https://github.com/micktwomey/pyiso8601
Source0:        https://github.com/micktwomey/pyiso8601/archive/refs/tags/2.1.0.tar.gz#/python-iso8601-2.1.0.tar.gz
Patch:          0001-Add-docs-and-test-extras.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-iso8601 = %{version}-%{release}
# /oreon:deps
%description %{pkgdesc}

%package -n python3-%{srcname}
Summary:        Simple module to parse ISO 8601 dates
BuildRequires:  python3-devel
%description -n python3-%{srcname} %{pkgdesc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyiso8601-2.1.0
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/iso8601* usr/lib64/python3*/site-packages/iso8601* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import -e iso8601.test_iso8601
%endif
%files
%files -n python3-iso8601 -f %{oreon_filedir}/python3-iso8601.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-8
- Import
