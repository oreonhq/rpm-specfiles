%global source0_hash 99972952ad3251e8a02cd7dfe08f2b99dcd327f94827a498254a86f1343e0340
%global modname http-ece
Name:               python-http-ece
Version:            1.2.1
Release:        1%{?dist}
Summary:        A simple implementation of the encrypted content-encoding
License:            MIT
URL:                https://github.com/web-push-libs/encrypted-content-encoding
Source0:        https://github.com/web-push-libs/encrypted-content-encoding/archive/%{version}/encrypted-content-encoding-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-http-ece = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        A simple implementation of the encrypted content-encoding
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-coverage
BuildRequires:      python%{python3_pkgversion}-cryptography
%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir encrypted-content-encoding-%{version}
%oreon_prep
%build

cd python
%pyproject_wheel
%install
cd python
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/http_ece* usr/lib64/python3*/site-packages/http_ece* usr/bin/*

%check

%pyproject_check_import
cd python
%pytest
%files
%files -n python3-http-ece -f %{oreon_filedir}/python3-http-ece.list

%changelog

%autochangelog
