%global source0_hash 890313320280455daeaa11100e8b765093fee7839ae946de38333601fe544a16
Name:           python-pretend
Version:        1.0.9
Release:        1%{?dist}
Summary:        A library for stubbing in Python
License:        BSD-3-Clause
URL:            https://github.com/alex/pretend
Source0:        https://github.com/alex/pretend/archive/refs/tags/v1.0.9.tar.gz#/pretend-1.0.9.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pretend = %{version}-%{release}
# /oreon:deps
%description
Pretend is a library to make stubbing with Python easier.

%package -n python3-pretend
Summary:        A library for stubbing in Python
%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pretend-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pretend usr/lib/python3*/site-packages/pretend* usr/lib64/python3*/site-packages/pretend* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pretend* usr/lib64/python3*/site-packages/pretend* usr/bin/*

%check

%pyproject_check_import
%pytest -v
%files
%files -n python3-pretend -f %{oreon_filedir}/python3-pretend.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.9-1
- Prepare for Oreon 11 (RP1)
