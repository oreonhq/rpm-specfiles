%global source0_hash 489ec477174b67dbb9f1f76f9ae4745ede3290010c4af02af7ec6e01b5452dc0
Name:           python-xstatic-bootstrap-scss
Version:        3.4.1.1
Release:        1%{?dist}
Summary:        Bootstrap-SCSS 3.4.1 _XStatic packaging standard_
License:        MIT
URL:            https://github.com/twbs/bootstrap-sass
Source0:        https://files.pythonhosted.org/packages/source/x/xstatic_bootstrap_scss/xstatic_bootstrap_scss-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xstatic-bootstrap-scss = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xstatic-bootstrap-scss
Summary:        Bootstrap-SCSS 3.4.1 _XStatic packaging standard_
%description -n python3-xstatic-bootstrap-scss

%prep
%global oreon_srcdir xstatic_bootstrap_scss-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xstatic-bootstrap-scss usr/lib/python3*/site-packages/xstatic_bootstrap_scss* usr/lib64/python3*/site-packages/xstatic_bootstrap_scss* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xstatic_bootstrap_scss* usr/lib64/python3*/site-packages/xstatic_bootstrap_scss* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xstatic-bootstrap-scss -f %{oreon_filedir}/python3-xstatic-bootstrap-scss.list

%changelog

%autochangelog
