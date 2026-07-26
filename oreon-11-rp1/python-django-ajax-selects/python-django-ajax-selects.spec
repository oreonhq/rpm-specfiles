%global source0_hash 539298874b2d26ce9e778a5173d312f55340c887a126c7e2d3460b9a5b4593a2

%global pkgname django-ajax-selects

Name:           python-django-ajax-selects
Version:        2.2.0
Release:        16%{?dist}
Summary:        Enables editing of ForeignKey, ManyToMany and simple text fields

# Automatically converted from old format: MIT or GPL+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR GPL-1.0-or-later
URL:            https://github.com/crucialfelix/django-ajax-selects
Source:         http://pypi.python.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
Enables editing of ForeignKey, ManyToMany and simple text fields using the\
Autocomplete - jQuery plugin.\
django-ajax-selects will work in any normal form as well as in the admin.\
The user is presented with a text field. They type a search term or a few\
letters of a name they are looking for, an ajax request is sent to the server,\
a search channel returns possible results. Results are displayed as a drop\
down menu. When an item is selected it is added to a display area just below\
the text field.

%description %_description

%package -n python3-django-ajax-selects
Summary:        Intelligent schema migrations for Django apps

%{?python_provide:%python_provide python3-django-ajax-selects}

Requires:       python3-django

Obsoletes:      python2-django-ajax-selects < 1.3.4-14
Obsoletes:      python-django-ajax-selects < 1.3.4-14

%description -n python3-django-ajax-selects %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-django-ajax-selects
%license ajax_select/LICENSE.txt
%doc README.md CHANGELOG.md
%{python3_sitelib}/ajax_select
%{python3_sitelib}/django_ajax_selects-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
