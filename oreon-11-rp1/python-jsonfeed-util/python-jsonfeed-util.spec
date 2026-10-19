%global source0_hash 1aa4123307059a1a522033f00c17fa492bf7c2d0dc1eb877e518f5c30438e0fc
%bcond tests 1
Name:           python-jsonfeed-util
Version:        1.2.0
Release:        1%{?dist}
Summary:        Python package for parsing and generating JSON feeds
License:        MIT
URL:            https://github.com/lukasschwab/jsonfeed
Source0:        https://github.com/lukasschwab/jsonfeed/archive/%{version}/jsonfeed-%{version}.tar.gz
Patch:          %{url}/pull/13.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jsonfeed-util = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jsonfeed-util
Summary:        Python package for parsing and generating JSON feeds
%description -n python3-jsonfeed-util

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jsonfeed-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}/tests
%oreon_autofiles python3-jsonfeed-util usr/lib/python3*/site-packages/jsonfeed_util* usr/lib64/python3*/site-packages/jsonfeed_util* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonfeed_util* usr/lib64/python3*/site-packages/jsonfeed_util* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-jsonfeed-util -f %{oreon_filedir}/python3-jsonfeed-util.list

%changelog

%autochangelog
