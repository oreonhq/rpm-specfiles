%global source0_hash 60665f31c2c612891db68ff801e93ed3a0881c6c8ec346abc64d2a9923f562e1
%global pkg_name flask-gravatar
Name:           python-%{pkg_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Small extension for Flask to make usage of Gravatar service easy
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/zzzsochi/Flask-Gravatar/
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/F/Flask-Gravatar/Flask-Gravatar-%{version}.tar.gz
Patch0:         python-flask-gravatar_tests.patch
Patch1:         flask-3-support.patch
Patch2:         0001-Downstream-only-remove-pytest-runner-dependency.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flask-gravatar = %{version}-%{release}
# /oreon:deps
%description
Small extension for Flask to make usage of Gravatar service easy.

%package -n python3-%{pkg_name}
Summary: Small extension for Flask to make usage of Gravatar service easy
%description -n python3-%{pkg_name}
Small extension for Flask to make usage of Gravatar service easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Flask-Gravatar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/flask_gravatar* usr/lib64/python3*/site-packages/flask_gravatar* usr/bin/*

%check

%pytest
%files
%files -n python3-flask-gravatar -f %{oreon_filedir}/python3-flask-gravatar.list

%changelog

%autochangelog
