%global source0_hash 4b2921931b95c4a5ba81d690f8dc3107a0a1fab04470c146251faf6d6ed1a151
Name:           python-cart
Version:        1.2.3
Release:        1%{?dist}
Summary:        Compressed and RC4 Transport for Python
License:        MIT
URL:            https://github.com/CybercentreCanada/cart
Source0:        https://github.com/CybercentreCanada/cart/archive/v%{version}/cart-%{version}.tar.gz
Patch1:         python-cart-1.2.2-cryptodomex.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cart = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cart
Summary:        Compressed and RC4 Transport for Python
%description -n python3-cart

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cart-%{version}
sed -i '/#!\/usr\/bin\/env python/d' cart/cart.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cart usr/lib/python3*/site-packages/cart* usr/lib64/python3*/site-packages/cart* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cart* usr/lib64/python3*/site-packages/cart* usr/bin/*

%check

%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest
%files
%files -n python3-cart -f %{oreon_filedir}/python3-cart.list

%changelog

%autochangelog
