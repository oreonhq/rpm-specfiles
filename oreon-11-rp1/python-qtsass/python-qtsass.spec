%global source0_hash b7dd08549744f4e8ffee74af8517c662010e8d9153225253c65d26fbc5ef697b
%bcond qt 0
Name:           python-qtsass
Version:        0.4.0
Release:        1%{?dist}
Summary:        Compile SCSS files to valid Qt stylesheets
License:        MIT
URL:            https://github.com/spyder-ide/qtsass
Source0:        https://github.com/spyder-ide/qtsass/archive/v%{version}/qtsass-%{version}.tar.gz
%if %{without qt}
%endif
BuildArch:      noarch
Patch:          %{url}/pull/76.patch
Patch:          %{url}/pull/77.patch
%if %{with qt}
%endif
%global common_description %{expand:
SASS brings countless amazing features to CSS. Besides being used in web
development, CSS is also the way to stylize Qt-based desktop applications.
However, Qt’s CSS has a few variations that prevent the direct use of SASS
compiler.
The purpose of this tool is to fill the gap between SASS and Qt-CSS by handling
those variations.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-qtsass = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-qtsass
Summary:        Compile SCSS files to valid Qt stylesheets
%description -n python3-qtsass %{common_description}

%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/qtsass.1' \
    '%{buildroot}%{_bindir}/qtsass'
%oreon_autofiles python3-qtsass usr/lib/python3*/site-packages/qtsass* usr/lib64/python3*/site-packages/qtsass* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qtsass* usr/lib64/python3*/site-packages/qtsass* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -v
%files
%files -n python3-qtsass -f %{oreon_filedir}/python3-qtsass.list

%changelog

%autochangelog
