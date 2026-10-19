%global source0_hash 2d26ce2c427661e7120af50c210f00366e3eb97c5979890cbe810b381ed57586
Name:           python-xstatic-js-yaml
Version:        3.13.1.2
Release:        1%{?dist}
Summary:        JS-Yaml 3.13.1 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/nodeca/js-yaml
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_js_yaml/xstatic_js_yaml-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-js-yaml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-js-yaml
Summary:        JS-Yaml 3.13.1 _XStatic packaging standard_
%description -n python3-xstatic-js-yaml

%prep
%global oreon_srcdir xstatic_js_yaml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-js-yaml usr/lib/python3*/site-packages/xstatic_js_yaml* usr/lib64/python3*/site-packages/xstatic_js_yaml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_js_yaml* usr/lib64/python3*/site-packages/xstatic_js_yaml* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-js-yaml -f %{oreon_filedir}/python3-xstatic-js-yaml.list

%changelog

%autochangelog
