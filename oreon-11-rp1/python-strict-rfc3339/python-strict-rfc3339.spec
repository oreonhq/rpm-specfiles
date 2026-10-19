%global source0_hash 5cad17bedfc3af57b399db0fed32771f18fc54bbd917e85546088607ac5e1277
Name:           python-strict-rfc3339
Version:        0.7
Release:        1%{?dist}
Summary:        Strict, simple, lightweight RFC3339 functions
License:        GPL-3.0-only
URL:            https://github.com/danielrichman/strict-rfc3339
Source0:        https://files.pythonhosted.org/packages/source/s/strict-rfc3339/strict-rfc3339-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-strict-rfc3339 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-strict-rfc3339
Summary:        Strict, simple, lightweight RFC3339 functions
%description -n python3-strict-rfc3339

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir strict-rfc3339-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-strict-rfc3339 usr/lib/python3*/site-packages/strict_rfc3339* usr/lib64/python3*/site-packages/strict_rfc3339* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/strict_rfc3339* usr/lib64/python3*/site-packages/strict_rfc3339* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-strict-rfc3339 -f %{oreon_filedir}/python3-strict-rfc3339.list

%changelog

%autochangelog
