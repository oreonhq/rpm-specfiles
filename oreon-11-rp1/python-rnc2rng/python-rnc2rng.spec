%global source0_hash dd9ffbbd69d09cb07e6e7a8cf80fd28703fdc6d3b9026f8756b49cbe3314676b
%bcond_without tests
Name:           python-rnc2rng
Version:        2.7.0
Release:        9%{?dist}
Summary:        RELAX NG Compact to regular syntax conversion library
License:        MIT
URL:            https://github.com/djc/rnc2rng
Source0:        https://files.pythonhosted.org/packages/source/r/rnc2rng/rnc2rng-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rnc2rng = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-rnc2rng
Summary:        RELAX NG Compact to regular syntax conversion library
BuildRequires:  python3-devel
%description -n python3-rnc2rng

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rnc2rng-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rnc2rng usr/lib/python3*/site-packages/rnc2rng* usr/lib64/python3*/site-packages/rnc2rng* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rnc2rng* usr/lib64/python3*/site-packages/rnc2rng* usr/bin/*

%check

%if %{with tests}
%{__python3} test.py
%endif
%pyproject_check_import
%files
%files -n python3-rnc2rng -f %{oreon_filedir}/python3-rnc2rng.list

%changelog

%autochangelog
