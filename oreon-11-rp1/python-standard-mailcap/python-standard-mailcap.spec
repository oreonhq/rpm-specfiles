%global source0_hash bde43692d5a1de2a33777ff99f4c4344f7cca3a49362b2484a13870706194613
Name:           python-standard-mailcap
Version:        3.13.0
Release:        1%{?dist}
Summary:        Standard library mailcap redistribution, "dead battery"
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source0:        https://github.com/youknowone/python-deadlib/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.7
Requires:       python3-standard-mailcap = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-standard-mailcap
Summary:        Standard library mailcap redistribution, "dead battery"
%description -n python3-standard-mailcap

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

tar -x -f %{SOURCE0} --strip-components=2 python-deadlib-%{version}/mailcap/
sed -i -e "s/setuptools>=75.0/setuptools>=69.0/" pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-standard-mailcap usr/lib/python3*/site-packages/standard_mailcap* usr/lib64/python3*/site-packages/standard_mailcap* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/standard_mailcap* usr/lib64/python3*/site-packages/standard_mailcap* usr/bin/*

%check

%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest
%files
%files -n python3-standard-mailcap -f %{oreon_filedir}/python3-standard-mailcap.list

%changelog

%autochangelog
