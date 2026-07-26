%global source0_hash 5e23d14a607ef12806c699590b89d0f0e0d67baeec599d75947bf9c147330333

%global pypi_name Flask-Login

Name:           python-flask-login
Version:        0.6.3
Release:        11%{?dist}
Summary:        User session management for Flask

License:        MIT
URL:            https://github.com/maxcountryman/flask-login
Source0:        %{pypi_source %pypi_name}
BuildArch:      noarch

%description
Flask-Login provides user session management for Flask. It handles the common\
tasks of logging in, logging out, and remembering your users' sessions over\
extended periods of time.

%package -n     python3-flask-login
Summary:        User session management for Flask
BuildRequires:  python3-devel
# Test deps
BuildRequires:  python3-pytest
BuildRequires:  python3-asgiref
BuildRequires:  python3-blinker
BuildRequires:  python3-flask
BuildRequires:  python3-semantic_version

%description -n python3-flask-login
Flask-Login provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users' sessions over
extended periods of time.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_login

%check
%pytest -Wdefault

%files -n python3-flask-login -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
