%global source0_hash a27df6835de352b6ad06e0781c83105037069b99350c0ed294e8a5c7fd379aba
Name:           python-productmd
Version:        1.50
Release:        2%{?dist}
Summary:        Library providing parsers for metadata related to OS installation
License:        LGPL-2.1-only
URL:            https://github.com/release-engineering/productmd
Source0:        https://files.pythonhosted.org/packages/source/p/productmd/productmd-1.50.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-productmd = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-productmd
Summary:        Library providing parsers for metadata related to OS installation
%description -n python3-productmd

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir productmd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-productmd usr/lib/python3*/site-packages/productmd* usr/lib64/python3*/site-packages/productmd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/productmd* usr/lib64/python3*/site-packages/productmd* usr/bin/*

%check

%pytest
%files
%files -n python3-productmd -f %{oreon_filedir}/python3-productmd.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.50-2
- Prepare for Oreon 11 (RP1)
