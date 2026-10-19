%global source0_hash f6a7578b00a8458e5edd38431d3ea4037b928a21ba1f82469ec2015127955c34
Name:           python-sphinxcontrib-jquery
Version:        4.1
Release:        15%{?dist}
Summary:        Extension to include jQuery on newer Sphinx releases
License:        0BSD AND BSD-2-Clause AND MIT
URL:            https://github.com/sphinx-contrib/jquery/
Source0:        https://github.com/sphinx-contrib/jquery//archive/refs/tags/v4.1/sphinxcontrib-jquery-4.1.tar.gz#/python-sphinxcontrib-jquery-4.1.tar.gz
Patch:          Fix-tests-failures-with-Sphinx-7.2.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-sphinxcontrib-jquery = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinxcontrib-jquery
Summary:        Extension to include jQuery on newer Sphinx releases
# oreon:reqs
Requires:       python3dist(sphinx) >= 1.8
# /oreon:reqs
%description -n python3-sphinxcontrib-jquery

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jquery-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-jquery usr/lib/python3*/site-packages/sphinxcontrib_jquery* usr/lib64/python3*/site-packages/sphinxcontrib_jquery* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_jquery* usr/lib64/python3*/site-packages/sphinxcontrib_jquery* usr/bin/*

%check

%pytest
%files
%files -n python3-sphinxcontrib-jquery -f %{oreon_filedir}/python3-sphinxcontrib-jquery.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1-15
- Prepare for Oreon 11 (RP1)
