%global source0_hash ce5cf0e7c111742af687251ba67c25a7992d2d4c16896fa29a8426bb5bfa14b6
Name:           python-xstatic-angular-vis
Version:        4.16.0.1
Release:        1%{?dist}
Summary:        Angular-Vis 4.16.0 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/visjs/angular-visjs
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_angular_vis/xstatic_angular_vis-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-angular-vis = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-angular-vis
Summary:        Angular-Vis 4.16.0 _XStatic packaging standard_
%description -n python3-xstatic-angular-vis

%prep
%global oreon_srcdir xstatic_angular_vis-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-angular-vis usr/lib/python3*/site-packages/xstatic_angular_vis* usr/lib64/python3*/site-packages/xstatic_angular_vis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_angular_vis* usr/lib64/python3*/site-packages/xstatic_angular_vis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-angular-vis -f %{oreon_filedir}/python3-xstatic-angular-vis.list

%changelog

%autochangelog
