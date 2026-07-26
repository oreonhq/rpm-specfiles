%global source0_hash 2680524870b43cdcd729edf49b3042612b8a4d2fa089d9f2e9ce32d8d0d5d3ba

%global projectname cached-property
%global modulename  cached_property

Name:           python-%{modulename}
Version:        2.0.1
Release:        7%{?dist}
Summary:        A cached-property for decorating methods in Python classes
License:        BSD-3-Clause
URL:            https://github.com/pydanny/%{projectname}
Source0:        https://github.com/pydanny/%{projectname}/archive/%{version}/%{projectname}-%{version}.tar.gz
# Prepare for deprecation of asyncio.iscoroutinefunction in Python 3.14
# https://github.com/pydanny/cached-property/pull/359
Patch1:         0001-Use-iscoroutinefunction-from-inspect-not-asyncio.patch

BuildArch:      noarch

%description
cached_property allows properties in Python classes to be cached until the cache
is invalidated or expired.

%package -n python3-%{modulename}
Summary:        A cached-property for decorating methods in Python classes.
BuildRequires:  python3-devel
# This package was python3-{projectname} for a long time, but never should've
# been
Provides:       python3-%{projectname} = %{version}-%{release}
Obsoletes:      python3-%{projectname} < 1.3.0-2

%description -n python3-%{modulename}
cached_property allows properties in Python classes to be cached until the cache
is invalidated or expired.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{projectname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modulename}

%check
%tox

%files -n python3-%{modulename} -f %{pyproject_files}
%doc AUTHORS.md HISTORY.md CONTRIBUTING.md README.md

%changelog
%autochangelog
