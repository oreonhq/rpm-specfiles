%global source0_hash 79d2ee1e436cf570bccb7d916533fa18757a2f18c290accffab1b9a0b684666b

%global mod_name flask_wtf

Name:           python-flask-wtf
Version:        1.2.2
Release:        7%{?dist}
Summary:        Simple integration of Flask and WTForms

License:        BSD-3-Clause
URL:            https://github.com/lepture/flask-wtf
Source0:        %{pypi_source %mod_name}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Flask-WTF offers simple integration with WTForms. This integration
includes optional CSRF handling for greater security.

%package -n python3-flask-wtf
Summary:        Simple integration of Flask and WTForms

%description -n python3-flask-wtf
Flask-WTF offers simple integration with WTForms. This integration 
includes optional CSRF handling for greater security.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_wtf

 
%check
%py3_check_import flask_wtf

%files -n python3-flask-wtf -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst docs/

%changelog
%autochangelog
