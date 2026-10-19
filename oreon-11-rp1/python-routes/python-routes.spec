%global source0_hash b6346459a15f0cbab01a45a90c3d25caf980d4733d628b4cc1952b865125d053
Name: python-routes
Version: 2.5.1
Release:        1%{?dist}
Summary:        Routing Recognition and Generation Tools
License: MIT
URL: https://github.com/bbangert/routes
Source0:        https://pypi.io/packages/source/R/Routes/Routes-%{version}.tar.gz
Patch0001: 0001-switch-from-nose-to-pytest.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-routes = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-routes
Summary:        Routing Recognition and Generation Tools
%description -n python3-routes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Routes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-routes usr/lib/python3*/site-packages/routes* usr/lib64/python3*/site-packages/routes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/routes* usr/lib64/python3*/site-packages/routes* usr/bin/*

%check

PYTHONPATH=$(pwd) python3 -m pytest
%files
%files -n python3-routes -f %{oreon_filedir}/python3-routes.list

%changelog

%autochangelog

