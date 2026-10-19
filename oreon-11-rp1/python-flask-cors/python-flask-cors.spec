%global source0_hash 30c5031552cd59f620ac0c8211dac45b345d3b2df310e7721879e4f46ef9c601
Name:           python-flask-cors
Version:        6.0.5
Release:        1%{?dist}
Summary:        A Flask extension simplifying CORS support
License:        MIT
URL:            https://corydolphin.github.io/flask-cors/
Source0:        https://files.pythonhosted.org/packages/source/f/flask_cors/flask_cors-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-flask-cors = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flask-cors
Summary:        A Flask extension simplifying CORS support
# oreon:reqs
Requires:       python3dist(flask) >= 0.9
Requires:       python3dist(typing-extensions) >= 4.6.0
Requires:       python3dist(werkzeug) >= 0.7
# /oreon:reqs
%description -n python3-flask-cors

%prep
%global oreon_srcdir flask_cors-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-cors usr/lib/python3*/site-packages/flask_cors* usr/lib64/python3*/site-packages/flask_cors* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_cors* usr/lib64/python3*/site-packages/flask_cors* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-cors -f %{oreon_filedir}/python3-flask-cors.list

%changelog

%autochangelog
