%global source0_hash b4ad7448a83679a9c255700bd28979c685e66f89dd7c2eca7de8f4a52e5bd89f
Name:           python-flask-security-too
Version:        5.8.2
Release:        1%{?dist}
Summary:        Quickly add security features to your Flask application.
License:        MIT
URL:            https://github.com/pallets-eco/flask-security
Source0:        https://files.pythonhosted.org/packages/source/f/flask_security_too/flask_security_too-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-flask-security-too_testdeps.patch
Patch1:         python-flask-security-too_phonenumbers.patch
Patch2:         python-flask-security-too_no-sqla-utils.patch
Patch3:         python-flask-security-too_flask-sqla.patch
Patch4:         python-flask-security-too_no-libpass.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.8
Requires:       python3-flask-security-too = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-security-too+babel
Summary:        Metapackage for python3-flask-security-too babel extras
Requires:       python3-flask-security-too = %{version}-%{release}
Requires:       python3dist(babel) >= 2.17.0
Requires:       python3dist(flask-babel) >= 4.0.0
Provides:       python3dist(flask-security-too[babel]) = %{version}-%{release}

%description -n python3-flask-security-too+babel
Metapackage for python3-flask-security-too babel extras.

%package -n       python3-flask-security-too+fsqla
Summary:        Metapackage for python3-flask-security-too fsqla extras
Requires:       python3-flask-security-too = %{version}-%{release}
Requires:       python3dist(flask-sqlalchemy) >= 3.1.1
Requires:       python3dist(sqlalchemy) >= 2.0.41
Provides:       python3dist(flask-security-too[fsqla]) = %{version}-%{release}

%description -n python3-flask-security-too+fsqla
Metapackage for python3-flask-security-too fsqla extras.

%package -n       python3-flask-security-too+common
Summary:        Metapackage for python3-flask-security-too common extras
Requires:       python3-flask-security-too = %{version}-%{release}
Requires:       python3dist(argon2-cffi) >= 25.1.0
Requires:       python3dist(bcrypt) >= 4.2.1
Requires:       python3dist(flask-mail) >= 0.10.0
Requires:       python3dist(bleach) >= 6.0.0
Provides:       python3dist(flask-security-too[common]) = %{version}-%{release}

%description -n python3-flask-security-too+common
Metapackage for python3-flask-security-too common extras.

%package -n       python3-flask-security-too+mfa
Summary:        Metapackage for python3-flask-security-too mfa extras
Requires:       python3-flask-security-too = %{version}-%{release}
Requires:       python3dist(cryptography) >= 45.0.7
Requires:       python3dist(qrcode) >= 7.4.2
Requires:       python3dist(phonenumberslite) >= 8.13.11
Requires:       python3dist(webauthn) >= 2.6.0
Provides:       python3dist(flask-security-too[mfa]) = %{version}-%{release}

%description -n python3-flask-security-too+mfa
Metapackage for python3-flask-security-too mfa extras.

%package -n       python3-flask-security-too+low
Summary:        Metapackage for python3-flask-security-too low extras
Requires:       python3-flask-security-too = %{version}-%{release}
Requires:       python3dist(flask) == 3.1.1
Requires:       python3dist(flask-sqlalchemy) == 3.1.1
Requires:       python3dist(flask-sqlalchemy-lite) == 0.1.0
Requires:       python3dist(flask-babel) == 4.0.0
Requires:       python3dist(flask-mail) == 0.10.0
Requires:       python3dist(flask-login) == 0.6.3
Requires:       python3dist(flask-wtf) == 1.1.2
Requires:       python3dist(peewee) == 3.17.9
Requires:       python3dist(argon2-cffi) == 21.3.0
Requires:       python3dist(authlib) == 1.2.0
Requires:       python3dist(babel) == 2.16.0
Requires:       python3dist(bcrypt) == 4.0.1
Requires:       python3dist(bleach) == 6.0.0
Requires:       python3dist(jinja2) == 3.1.2
Requires:       python3dist(itsdangerous) == 2.2.0
Requires:       python3dist(markupsafe) == 2.1.2
Requires:       python3dist(mongoengine) == 0.29.1
Requires:       python3dist(mongomock) == 4.3.0
Requires:       python3dist(pony) == 0.7.16
Requires:       python3dist(phonenumberslite) == 8.13.11
Requires:       python3dist(qrcode) == 7.4.2
Requires:       python3dist(sqlalchemy) == 2.0.41
Requires:       python3dist(sqlalchemy-utils) == 0.42.0
Requires:       python3dist(webauthn) == 2.0.0
Requires:       python3dist(werkzeug) == 3.1.3
Requires:       python3dist(zxcvbn) == 4.4.28
Provides:       python3dist(flask-security-too[low]) = %{version}-%{release}

%description -n python3-flask-security-too+low
Metapackage for python3-flask-security-too low extras.

%description

%package -n     python3-flask-security-too
Summary:        Quickly add security features to your Flask application.
# oreon:reqs
Requires:       python3dist(email-validator) >= 2.3.0
Requires:       python3dist(flask) >= 3.1.1
Requires:       python3dist(flask-login) >= 0.6.3
Requires:       python3dist(flask-principal) >= 0.4.0
Requires:       python3dist(flask-wtf) >= 1.1.2
Requires:       python3dist(libpass) >= 1.9.3
Requires:       python3dist(markupsafe) >= 2.1.0
Requires:       python3dist(wtforms) >= 3.0.0
# /oreon:reqs
%description -n python3-flask-security-too

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir flask_security_too-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-security-too usr/lib/python3*/site-packages/flask_security_too* usr/lib64/python3*/site-packages/flask_security_too* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_security_too* usr/lib64/python3*/site-packages/flask_security_too* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-security-too -f %{oreon_filedir}/python3-flask-security-too.list

%changelog

%autochangelog
