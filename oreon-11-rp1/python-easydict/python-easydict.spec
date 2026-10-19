%global source0_hash b1135dedbc41c8010e2bc1f77ec9744c7faa42bce1a1c87416791449d6c87780
Name:           python-easydict
Version:        1.13
Release:        1%{?dist}
Summary:        Access dict values as attributes _works recursively_.
License:        LGPL-3.0
URL:            https://github.com/makinacorpus/easydict
Source0:        https://files.pythonhosted.org/packages/source/e/easydict/easydict-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-easydict = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-easydict
Summary:        Access dict values as attributes _works recursively_.
%description -n python3-easydict

%prep
%global oreon_srcdir easydict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-easydict usr/lib/python3*/site-packages/easydict* usr/lib64/python3*/site-packages/easydict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/easydict* usr/lib64/python3*/site-packages/easydict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-easydict -f %{oreon_filedir}/python3-easydict.list

%changelog

%autochangelog
