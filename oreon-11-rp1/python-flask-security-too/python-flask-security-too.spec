%global source0_hash 5a48b9165146a02cb86a8073832df4ca177fbf4a7dbd707909279fbfad8a4032

%global pkg_name flask-security-too

Name:           python-%{pkg_name}
Version:        5.6.2
Release:        6%{?dist}
Summary:        Simple security for Flask apps
License:        MIT

BuildArch:      noarch
URL:            https://github.com/Flask-Middleware/flask-security
Source0:        %{pypi_source flask_security_too}
# Drop missing test deps
Patch0:         python-flask-security-too_testdeps.patch
# Use phonenumbers instead of phonenumberslite
Patch1:         python-flask-security-too_phonenumbers.patch
# FIXME Temporarily drop sqlalchemy-utils dependency and bundle required functions
# (fedora package requires flask-sqlalchemy-1.x which conflicts with required flask-sqlalchemy-3.x)
Patch2:         python-flask-security-too_no-sqla-utils.patch
# Relax flask-sqlalchemy version requirement
Patch3:         python-flask-security-too_flask-sqla.patch
# libpass is not packaged
Patch4:         python-flask-security-too_no-libpass.patch

BuildRequires:  python3-devel

%description
Flask-Security quickly adds security features to your Flask application.

%package -n python3-%{pkg_name}
Summary:        Simple security for Flask apps

%description -n python3-%{pkg_name}
Flask-Security quickly adds security features to your Flask application.

# Skip mfa extra, webauthn is not packaged
%pyproject_extras_subpkg -n python3-%{pkg_name} babel fsqla common

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flask_security_too-%{version}
ln -sf pyproject-too.toml pyproject.toml

%generate_buildrequires
# Skip mfa extra, webauthn is not packaged
%pyproject_buildrequires -x babel,fsqla,common -r requirements/tests.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_security

%check
# Expected fail in DNS resolve (requires network)
%pytest -k "not test_login_email_whatever"

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst AUTHORS

%changelog
%autochangelog
