%global source0_hash cc6ec7f2fbf43d875d0fe59f4f0450b95370108b4e1764ab94a645d252679ba5
Name:           python-flask-mailman
Version:        1.1.1
Release:        1%{?dist}
Summary:        Porting Django's email implementation to your Flask applications
License:        BSD-3-Clause
URL:            https://github.com/waynerv/flask-mailman
Source0:        https://github.com/waynerv/flask-mailman/archive/v%{version}/flask-mailman-%{version}.tar.gz
Patch0:         flask-mailman_deps.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-flask-mailman = %{version}-%{release}
# /oreon:deps
%description
Flask-Mailman is a Flask extension providing simple email sending capabilities.

%package -n python3-flask-mailman
Summary:        Porting Django's email implementation to your Flask applications
BuildRequires:  python3-devel
%description -n python3-flask-mailman
Flask-Mailman is a Flask extension providing simple email sending capabilities.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir flask-mailman-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-mailman usr/lib/python3*/site-packages/flask_mailman* usr/lib64/python3*/site-packages/flask_mailman* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_mailman* usr/lib64/python3*/site-packages/flask_mailman* usr/bin/*

%check

%tox
%files
%files -n python3-flask-mailman -f %{oreon_filedir}/python3-flask-mailman.list

%changelog

%autochangelog
