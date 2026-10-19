%global source0_hash c5f486f5f54420729f84b3c3850cd63f96e8b033a9629bee66c524ea363797ff
Name:           python-flask-talisman
Version:        1.1.0
Release:        1%{?dist}
Summary:        HTTP security headers for Flask.
License:        ...
URL:            https://github.com/wntrblm/flask-talisman
Source0:        https://files.pythonhosted.org/packages/source/f/flask-talisman/flask-talisman-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flask-talisman = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flask-talisman
Summary:        HTTP security headers for Flask.
%description -n python3-flask-talisman

%prep
%global oreon_srcdir flask-talisman-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-talisman usr/lib/python3*/site-packages/flask_talisman* usr/lib64/python3*/site-packages/flask_talisman* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_talisman* usr/lib64/python3*/site-packages/flask_talisman* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-talisman -f %{oreon_filedir}/python3-flask-talisman.list

%changelog

%autochangelog
