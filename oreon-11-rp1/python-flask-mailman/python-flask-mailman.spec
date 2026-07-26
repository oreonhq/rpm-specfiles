%global source0_hash cc6ec7f2fbf43d875d0fe59f4f0450b95370108b4e1764ab94a645d252679ba5

Name:           python-flask-mailman
Version:        1.1.1
Release:        8%{?dist}
Summary:        Porting Django's email implementation to your Flask applications

License:        BSD-3-Clause
URL:            https://github.com/waynerv/flask-mailman
Source0:        https://github.com/waynerv/flask-mailman/archive/v%{version}/flask-mailman-%{version}.tar.gz
# Drop mkdocs-material-extensions dependency which is not packages
# (all mkdocs dependencies are unused as docs are not built)
# Relax test dependencies
Patch0:         flask-mailman_deps.patch

BuildArch:      noarch

%description
Flask-Mailman is a Flask extension providing simple email sending capabilities.

%package -n python3-flask-mailman
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-flask-mailman
Flask-Mailman is a Flask extension providing simple email sending capabilities.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flask-mailman-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_mailman

%check
%tox

%files -n python3-flask-mailman -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
