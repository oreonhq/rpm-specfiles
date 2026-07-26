%global source0_hash bbb8b52b7c5721114ed230efbd97dbdc78c06097d1f8b16dddc9295d7bd09618

%global pypi_name sphinx-press-theme

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        26%{?dist}
Summary:        A Sphinx-doc theme based on Vuepress

# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://schettino72.github.io/sphinx_press_site/
Source0:        %{pypi_source sphinx_press_theme}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A modern responsive theme for python's Sphinx documentation generator.
See it in action on Press Theme own website.
This theme is based on VuePress.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A modern responsive theme for python's Sphinx documentation generator.
See it in action on Press Theme own website.
This theme is based on VuePress.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx_press_theme-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/sphinx_press_theme
%{python3_sitelib}/sphinx_press_theme-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
