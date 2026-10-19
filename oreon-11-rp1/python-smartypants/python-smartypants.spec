%global source0_hash 39d64ce1d7cc6964b698297bdf391bc12c3251b7f608e6e55d857cd7c5f800c6
Name:           python-smartypants
Version:        2.0.2
Release:        1%{?dist}
Summary:        Python with the SmartyPants
License:        ...
URL:            https://github.com/justinmayer/smartypants.py
Source0:        https://files.pythonhosted.org/packages/source/s/smartypants/smartypants-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-smartypants = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-smartypants
Summary:        Python with the SmartyPants
%description -n python3-smartypants

%prep
%global oreon_srcdir smartypants-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-smartypants usr/lib/python3*/site-packages/smartypants* usr/lib64/python3*/site-packages/smartypants* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/smartypants* usr/lib64/python3*/site-packages/smartypants* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-smartypants -f %{oreon_filedir}/python3-smartypants.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-28
- Prepare for Oreon 11 (RP1)
