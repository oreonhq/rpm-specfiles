%global source0_hash 18743bd5a0621bfe2cf8d519e4c3bfdf57a269c15d1ced3fb4b64e0ff4600656
Name:           python-flexcache
Version:        0.3
Release:        1%{?dist}
Summary:        Cache on disk the result of expensive calculations
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexcache
Source0:        https://files.pythonhosted.org/packages/source/f/flexcache/flexcache-%{version}.tar.gz
Patch:          %{url}/pull/5.patch
BuildArch:      noarch
%global common_description %{expand:
A robust and extensible package to cache on disk the result of expensive
calculations.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-flexcache = %{version}-%{release}
# /oreon:deps
%package -n       python3-flexcache+test
Summary:        Metapackage for python3-flexcache test extras
Requires:       python3-flexcache = %{version}-%{release}
Provides:       python3dist(flexcache[test]) = %{version}-%{release}

%description -n python3-flexcache+test
Metapackage for python3-flexcache test extras.

%description %{common_description}

%package -n python3-flexcache
Summary:        Cache on disk the result of expensive calculations
%description -n python3-flexcache %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir flexcache-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rvf '%{buildroot}%{python3_sitelib}/flexcache/testsuite'
sed -r -i '/\/flexcache\/testsuite/d' %{pyproject_files}
%oreon_autofiles python3-flexcache usr/lib/python3*/site-packages/flexcache* usr/lib64/python3*/site-packages/flexcache* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flexcache* usr/lib64/python3*/site-packages/flexcache* usr/bin/*

%check

%pytest
%files
%files -n python3-flexcache -f %{oreon_filedir}/python3-flexcache.list

%changelog

%autochangelog
