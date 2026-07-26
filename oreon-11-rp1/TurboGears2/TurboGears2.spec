%global source0_hash d21aeab942263423b9bdf4949f5db28d0485c4f6b82a0c241c256aa9d90ab63a

Name:           TurboGears2
Version:        2.5.0
Release:        8%{?dist}
Summary:        Next generation front-to-back web development megaframework

License:        MIT
URL:            http://www.turbogears.org
Source0:        %pypi_source turbogears2

BuildArch:      noarch

BuildRequires:  python3-backlash
BuildRequires:  python3-chameleon
BuildRequires:  python3-crank >= 0.8.0
BuildRequires:  python3-devel
BuildRequires:  python3-formencode
BuildRequires:  python3-genshi >= 0.5.1
BuildRequires:  python3-jinja2
BuildRequires:  python3-kajiki >= 0.2.2
BuildRequires:  python3-mako
BuildRequires:  python3-repoze-tm2 >= 1.0-0.4.a4
BuildRequires:  python3-repoze-who
BuildRequires:  python3-repoze-who-plugins-sa >= 1.0.1
BuildRequires:  python3-tw2-forms
BuildRequires:  python3-webtest
BuildRequires:  python3-zope-sqlalchemy >= 0.4

%global _description \
TurboGears brings together a best of breed python tools to create a flexible,\
full featured, and easy to use web framework.\
\
TurboGears 2 provides and integrated and well tested set of tools for\
everything you need to build dynamic, database driven applications.  It\
provides a full range of tools for front end javascript develeopment, back\
database development and everything in between:\
\
 * dynamic javascript powered widgets ToscaWidgets\
 * automatic JSON generation from your controllers\
 * powerful, designer friendly XHTML basted templating (Genshi)\
 * object or route based URL dispatching\
 * powerful Object Relational Mappers (SQLAlchemy)\

%description %{_description}

%package -n python3-%{name}
Summary:        %{summary}

Requires:       python3-backlash
Requires:       python3-chameleon
Requires:       python3-crank >= 0.8.0
Requires:       python3-decorator
Requires:       python3-formencode
Requires:       python3-genshi >= 0.5.1
Requires:       python3-jinja2
Requires:       python3-kajiki > 0.2.2
Requires:       python3-mako
Requires:       python3-markupsafe
Requires:       python3-paste-deploy
Requires:       python3-repoze-lru
Requires:       python3-repoze-tm2 >= 1.0-0.a4
Requires:       python3-repoze-who
Requires:       python3-repoze-who-plugins-sa >= 1.0.1
Requires:       python3-tw2-forms
Requires:       python3-webob >= 1.2
Requires:       python3-zope-sqlalchemy >= 0.4

%description -n python3-%{name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n turbogears2-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tg
rm -fr %{buildroot}%{python3_sitelib}/tests

# Tests cannot be included because some test dependencies
# are not available in Fedora repositories
#%check
#PYTHONPATH=$(pwd) %{__python3} setup.py test

%check
%pyproject_check_import

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
