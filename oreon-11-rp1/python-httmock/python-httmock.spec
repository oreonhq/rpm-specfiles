%global source1_hash d85768965b07a7cc58f8fe7a868ba8309e97f70c9912c2965bc934576b0bac63
%global source0_hash 44eaf4bb59cc64cd6f5d8bf8700b46aa3097cc5651b9bc85c527dfbc71792f41
Name:           python-httmock
Version:        1.4.0
Release:        1%{?dist}
Summary:        A mocking library for requests
License:        Apache-2.0
URL:            https://github.com/patrys/httmock
Source0:        https://files.pythonhosted.org/packages/source/h/httmock/httmock-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/patrys/httmock/%{version}/tests.py
Patch0:         https://patch-diff.githubusercontent.com/raw/patrys/httmock/pull/64.diff
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httmock = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-httmock
Summary:        A mocking library for requests
BuildRequires:  python3-devel
%description -n python3-httmock

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n httmock-%{version}
cp %{SOURCE1} .

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httmock usr/lib/python3*/site-packages/httmock* usr/lib64/python3*/site-packages/httmock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httmock* usr/lib64/python3*/site-packages/httmock* usr/bin/*

%check

%{tox}
%files
%files -n python3-httmock -f %{oreon_filedir}/python3-httmock.list

%changelog

%autochangelog
