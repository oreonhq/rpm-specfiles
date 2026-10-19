%global source0_hash e0bd1b533ddf2f7369cdf0d2b1457c6eaec31225e56ad11a9ae2bbc68319e6de
Name:           python-xstatic-angular-uuid
Version:        0.0.4.1
Release:        1%{?dist}
Summary:        Angular-UUID 0.0.4 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/munkychop/angular-uuid
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_angular_uuid/xstatic_angular_uuid-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-angular-uuid = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-angular-uuid
Summary:        Angular-UUID 0.0.4 _XStatic packaging standard_
%description -n python3-xstatic-angular-uuid

%prep
%global oreon_srcdir xstatic_angular_uuid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-angular-uuid usr/lib/python3*/site-packages/xstatic_angular_uuid* usr/lib64/python3*/site-packages/xstatic_angular_uuid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_angular_uuid* usr/lib64/python3*/site-packages/xstatic_angular_uuid* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-angular-uuid -f %{oreon_filedir}/python3-xstatic-angular-uuid.list

%changelog

%autochangelog
