%global source0_hash 88499b22f1353893743c3cd68f2ca561c4ad9ef75cd6bcc7f621161cd0e80744
Name:           python-flask-httpauth
Version:        4.8.1
Release:        1%{?dist}
Summary:        HTTP authentication for Flask routes
License:        MIT
URL:            https://github.com/miguelgrinberg/flask-httpauth
Source0:        https://files.pythonhosted.org/packages/source/f/flask_httpauth/flask_httpauth-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-flask-httpauth-toml.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-flask-httpauth = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-httpauth+dev
Summary:        Metapackage for python3-flask-httpauth dev extras
Requires:       python3-flask-httpauth = %{version}-%{release}
Provides:       python3dist(flask-httpauth[dev]) = %{version}-%{release}

%description -n python3-flask-httpauth+dev
Metapackage for python3-flask-httpauth dev extras.

%package -n       python3-flask-httpauth+docs
Summary:        Metapackage for python3-flask-httpauth docs extras
Requires:       python3-flask-httpauth = %{version}-%{release}
Provides:       python3dist(flask-httpauth[docs]) = %{version}-%{release}

%description -n python3-flask-httpauth+docs
Metapackage for python3-flask-httpauth docs extras.

%description

%package -n     python3-flask-httpauth
Summary:        HTTP authentication for Flask routes
%description -n python3-flask-httpauth

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir flask_httpauth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-httpauth usr/lib/python3*/site-packages/flask_httpauth* usr/lib64/python3*/site-packages/flask_httpauth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_httpauth* usr/lib64/python3*/site-packages/flask_httpauth* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-httpauth -f %{oreon_filedir}/python3-flask-httpauth.list

%changelog

%autochangelog
