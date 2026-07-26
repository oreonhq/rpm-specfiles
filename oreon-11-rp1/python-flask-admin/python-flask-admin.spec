%global source0_hash 24cae2af832b6a611a01d7dc35f42d266c1d6c75a426b869d8cb241b78233369

%global srcname	Flask-Admin
%global pkgname flask-admin
%global sum Simple and extensible admin interface framework for Flask

Name:		python-%{pkgname}
Version:	1.6.1
Release:	12%{?dist}
Summary:	%{sum}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/flask-admin/flask-admin/
Source0:	https://files.pythonhosted.org/packages/source/F/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools

%global _description\
Flask-Admin is advanced, extensible and simple to use administrative interface\
building extension for Flask framework.\
\
It comes with batteries included: model scaffolding for SQLAlchemy,\
MongoEngine, MongoDB and Peewee ORMs, simple file management interface\
and a lot of usage samples.\
\
You're not limited by the default functionality - instead of providing simple\
scaffolding for the ORM models, Flask-Admin provides tools that can be used to\
construct administrative interfaces of any complexity, using a consistent look\
and feel.\

%description %_description

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:	%{sum}
Requires:	python%{python3_pkgversion}-flask
Requires:	python%{python3_pkgversion}-wtforms
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
for f in \
	flask_admin/contrib/pymongo/typefmt.py \
	flask_admin/tests/mock.py \
	flask_admin/tests/fileadmin/files/dummy.txt \
; do
	echo "#Empty file" > $f
done

rm -rf examples
rm flask_admin/translations/README.md

%build
%py3_build

%install
%py3_install

%check
# Tests are not included as they require mongod running

%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst
%license LICENSE
%dir %{python3_sitelib}/flask_admin
%{python3_sitelib}/flask_admin/translations
%{python3_sitelib}/flask_admin/static
%{python3_sitelib}/flask_admin/*.py*
%{python3_sitelib}/flask_admin/__pycache__/
%{python3_sitelib}/flask_admin/tests/
%{python3_sitelib}/flask_admin/contrib/
%{python3_sitelib}/flask_admin/model/
%{python3_sitelib}/flask_admin/templates/
%{python3_sitelib}/flask_admin/form/
%{python3_sitelib}/*.egg-info/

%changelog
%autochangelog
