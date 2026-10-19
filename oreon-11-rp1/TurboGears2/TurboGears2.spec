%global source0_hash d21aeab942263423b9bdf4949f5db28d0485c4f6b82a0c241c256aa9d90ab63a
Name:           TurboGears2
Version:        2.5.0
Release:        8%{?dist}
Summary:        Next generation front-to-back web development megaframework
License:        MIT
URL:            http://www.turbogears.org
Source0:        https://files.pythonhosted.org/packages/source/t/turbogears2/turbogears2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-TurboGears2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-TurboGears2+testing
Summary:        Metapackage for python3-TurboGears2 testing extras
Requires:       python3-TurboGears2 = %{version}-%{release}
Requires:       python3dist(zope.sqlalchemy) >= 0.4
Requires:       python3dist(Genshi) >= 0.5.1
Requires:       python3dist(backlash) >= 0.3.0
Requires:       python3dist(ming) >= 0.8.0
Requires:       python3dist(Kajiki) >= 0.4.4
Requires:       python3dist(formencode) >= 1.3.0a1
Provides:       python3dist(TurboGears2[testing]) = %{version}-%{release}

%description -n python3-TurboGears2+testing
Metapackage for python3-TurboGears2 testing extras.

%description

%package -n python3-%{name}
Summary:        Next generation front-to-back web development megaframework
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
%description -n python3-%{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir turbogears2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -fr %{buildroot}%{python3_sitelib}/tests
%oreon_autofiles main usr/lib/python3*/site-packages/TurboGears2* usr/lib64/python3*/site-packages/TurboGears2* usr/bin/*

%check

%pyproject_check_import
%files

%changelog

%autochangelog
