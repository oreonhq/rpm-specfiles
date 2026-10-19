%global source0_hash bfaab019ab2ea4e93550f6150c0a49fe8590b2505cb9bd09793ff3aa894ffe20
%bcond old_setuptools 0
Name:           python-merge3
Version:        0.0.16
Release:        1%{?dist}
Summary:        Python implementation of 3-way merge
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org
Source0:        https://github.com/breezy-team/merge3/archive/v%{version}/merge3-%{version}.tar.gz
Patch:          merge3-verbose-testlog.diff
Patch1000:      merge3-revert-setuptools-bump.diff
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-merge3 = %{version}-%{release}
# /oreon:deps
%package -n       python3-merge3+dev
Summary:        Metapackage for python3-merge3 dev extras
Requires:       python3-merge3 = %{version}-%{release}
Requires:       python3dist(ruff) == 0.14.0
Requires:       python3dist(mypy) >= 1.0.0
Provides:       python3dist(merge3[dev]) = %{version}-%{release}

%description -n python3-merge3+dev
Metapackage for python3-merge3 dev extras.

%description

%package -n python3-merge3
Summary:        Python implementation of 3-way merge
%description -n python3-merge3

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n merge3-%{version} -N
%autopatch -p1 -M 999
%if %{with old_setuptools}
%autopatch -p1 1000
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-merge3 usr/lib/python3*/site-packages/merge3* usr/lib64/python3*/site-packages/merge3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/merge3* usr/lib64/python3*/site-packages/merge3* usr/bin/*

%check

%tox
%files
%files -n python3-merge3 -f %{oreon_filedir}/python3-merge3.list

%changelog

%autochangelog
