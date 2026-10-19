%global source0_hash 9c535c4c61193c2df8871222567d7fd7e5014d835f97dc7b7439069e2413d343
Name:           python-ghp-import
Version:        2.1.0
Release:        1%{?dist}
Summary:        GitHub Pages Import
BuildArch:      noarch
License:        Apache-2.0
URL:            https://github.com/c-w/ghp-import
Source0:        https://files.pythonhosted.org/packages/source/g/ghp-import/ghp-import-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ghp-import = %{version}-%{release}
# /oreon:deps
%description
GitHub Pages Import.

%package -n python3-ghp-import
Summary:        GitHub Pages Import
Obsoletes:      python3-ghp-import2 < 1.0.1-12
Provides:       python3-ghp-import2 = %{version}-%{release}
%description -n python3-ghp-import
GitHub Pages Import.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ghp-import-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
sed -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/ghp_import.py
%oreon_autofiles python3-ghp-import usr/lib/python3*/site-packages/ghp_import* usr/lib64/python3*/site-packages/ghp_import* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ghp_import* usr/lib64/python3*/site-packages/ghp_import* usr/bin/*

%check

%py3_check_import ghp_import
%files
%files -n python3-ghp-import -f %{oreon_filedir}/python3-ghp-import.list

%changelog

%autochangelog
