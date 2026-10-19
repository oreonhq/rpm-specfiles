%global source0_hash 28dfcce0162b9211413e26dfbfdf1d24317fbeba18fc93c12400a1856b2a0bc7
%global         srcname     pyopenssl
Name:           pyOpenSSL
Version:        26.4.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
URL:            https://pyopenssl.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pyopenssl/pyopenssl-26.4.0.tar.gz
Patch:          0001-Limit-list-of-elliptic-curves-tested-to-those-in-Fed.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyOpenSSL = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pyOpenSSL
Summary: Python 3 wrapper module around the OpenSSL library
Obsoletes: pyOpenSSL < 19.0.0-5
Provides: pyOpenSSL = %{version}-%{release}
%description -n python3-pyOpenSSL

%package doc
Summary: Documentation for pyOpenSSL
BuildArch: noarch
%description doc
Documentation for pyOpenSSL

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

%build

%pyproject_wheel
%{__make} -C doc html SPHINXBUILD=sphinx-build-3
%install
%pyproject_install
rm doc/_build/html/.buildinfo
%oreon_autofiles python3-pyOpenSSL usr/lib/python3*/site-packages/pyOpenSSL* usr/lib64/python3*/site-packages/pyOpenSSL* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyOpenSSL* usr/lib64/python3*/site-packages/pyOpenSSL* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%pytest -k "not test_sign_verify_with_text" -k "not test_sign_verify"
%files
%files -n python3-pyOpenSSL -f %{oreon_filedir}/python3-pyOpenSSL.list
%files -n pyOpenSSL-doc -f %{oreon_filedir}/pyOpenSSL-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.3.0-1
- Prepare for Oreon 11 (RP1)
