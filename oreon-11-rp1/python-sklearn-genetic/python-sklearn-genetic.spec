%global source0_hash 36b080a1691d58bdeeaccb9c43553e33a40f3cb2048b48615cd155768b10d14b
%bcond tests 1
Name:           python-sklearn-genetic
Version:        0.6.0
Release:        1%{?dist}
Summary:        A genetic feature selection module for scikit-learn
License:        LGPL-3.0-only
URL:            https://github.com/manuel-calzolari/sklearn-genetic
Source0:        https://github.com/manuel-calzolari/sklearn-genetic/archive/%{version}/sklearn-genetic-%{version}.tar.gz
Patch:          %{url}/pull/49.patch
Patch:          %{url}/pull/50.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sklearn-genetic = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-sklearn-genetic
Summary:        A genetic feature selection module for scikit-learn
Obsoletes:      python-sklearn-genetic-doc < 0.6.0-5
BuildRequires:  make
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
%description -n python3-sklearn-genetic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sklearn-genetic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sklearn-genetic usr/lib/python3*/site-packages/sklearn_genetic* usr/lib64/python3*/site-packages/sklearn_genetic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sklearn_genetic* usr/lib64/python3*/site-packages/sklearn_genetic* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-sklearn-genetic -f %{oreon_filedir}/python3-sklearn-genetic.list

%changelog

%autochangelog
