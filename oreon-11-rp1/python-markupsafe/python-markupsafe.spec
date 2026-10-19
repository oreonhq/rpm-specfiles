%global source0_hash 722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698
Name:           python-markupsafe
Version:        3.0.3
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup.
License:        BSD-3-Clause
URL:            https://github.com/pallets/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-markupsafe = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-markupsafe
Summary:        Safely add untrusted strings to HTML/XML markup.
%description -n python3-markupsafe

%prep
%global oreon_srcdir markupsafe-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markupsafe usr/lib/python3*/site-packages/markupsafe* usr/lib64/python3*/site-packages/markupsafe* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markupsafe* usr/lib64/python3*/site-packages/markupsafe* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-markupsafe -f %{oreon_filedir}/python3-markupsafe.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.2-1
- Prepare for Oreon 11 (RP1)
