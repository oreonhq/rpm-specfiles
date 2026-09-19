%global source0_hash 60665f31c2c612891db68ff801e93ed3a0881c6c8ec346abc64d2a9923f562e1

%global pkg_name flask-gravatar

Name:           python-%{pkg_name}
Version:        0.5.0
Release:        32%{?dist}
Summary:        Small extension for Flask to make usage of Gravatar service easy

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/zzzsochi/Flask-Gravatar/
BuildArch:      noarch
Source0:        %{pypi_source Flask-Gravatar}
# Don't test pep8 as python-pytest-pep8 is obsolete
# Don't run linting tests
# Don't add flask_gravatar src folder to test path, buildroot path is already added by %%pytest
Patch0:         python-flask-gravatar_tests.patch
# Compatibility with Flask 2.3
# https://github.com/zzzsochi/Flask-Gravatar/pull/29
Patch1:         flask-3-support.patch
# Downstream-only: remove pytest-runner dependency
#
# pytest-runner not required
# https://github.com/zzzsochi/Flask-Gravatar/issues/27
#
# This patch was not offered upstream because it does not fully migrate away
# from pytest-runner; tox.ini, README.rst, and run-tests.sh are still based on
# "setup.py test". The patch only changes what is needed downstream.
#
# Furthermore, upstream appears to be inactive (last release in 2018, with only
# one commit since then), so a more complete PR probably would not be reviewed.
Patch2:         0001-Downstream-only-remove-pytest-runner-dependency.patch

BuildRequires:  python3-devel

%description
Small extension for Flask to make usage of Gravatar service easy.

%package -n python3-%{pkg_name}
Summary: Small extension for Flask to make usage of Gravatar service easy

%description -n python3-%{pkg_name}
Small extension for Flask to make usage of Gravatar service easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Flask-Gravatar-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_gravatar

%check
%pytest

%files -n python-%{pkg_name} -f %{pyproject_files}
%doc README.rst CHANGES.rst RELEASE-NOTES.rst AUTHORS
%license LICENSE

%changelog
%autochangelog
