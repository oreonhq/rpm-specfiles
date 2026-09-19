%global source0_hash ed8c58943460d7d54c29463e2fe98ae4969d3818c0f59b36e9b2649128db96c9

%global pkg_name flask-principal

Name:           python-flask-principal
Version:        0.4.0
Release:        45%{?dist}
Summary:        Identity management for Flask applications
License:        MIT

BuildArch:      noarch
URL:            https://pythonhosted.org/Flask-Principal/
Source0:        https://github.com/mattupstate/%{pkg_name}/archive/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
Flask-Principal provides a very loose framework to tie in authentication
and user information providers, often located in different parts of a web
application.

%package -n python3-flask-principal
Summary:        Identity management for Flask applications

%description -n python3-flask-principal
Flask-Principal provides a very loose framework to tie in authentication
and user information providers, often located in different parts of a web
application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_principal

%check
%pyproject_check_import
%pytest

%files -n python3-flask-principal -f %{pyproject_files}
%doc README.rst CHANGES
%license LICENSE

%changelog
%autochangelog
