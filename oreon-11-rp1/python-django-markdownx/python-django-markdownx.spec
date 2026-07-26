%global source0_hash b2b8452c319ae786476992011ac7c0655a63697e529292b3ca78116795c9ca66

%global pypi_name django-markdownx

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        24%{?dist}
Summary:        A comprehensive Markdown editor built for Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/neutronX/django-markdownx
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

%description
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(django)
Requires:       python3dist(markdown)
Requires:       python3dist(pillow)
Requires:       python3dist(pip)

%description -n python3-%{pypi_name}
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -rf markdownx/static/.DS_Store
rm -rf markdownx/static/markdownx/.DS_Store
rm -rf markdownx/static/markdownx/admin/.DS_Store
rm -rf markdownx/templates/.DS_Store
rm -rf markdownx/templates/markdownx/.DS_Store

chmod 0644 README.rst

%build
%py3_build

%install
%py3_install

%find_lang django
%files -n python3-%{pypi_name} -f django.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/markdownx
%exclude %{python3_sitelib}/markdownx/locale
%{python3_sitelib}/django_markdownx-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
