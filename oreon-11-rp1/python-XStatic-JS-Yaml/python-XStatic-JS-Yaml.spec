%global source0_hash d3a73dd4d56f5b9dc4d11045ca524a224822de530fdf0ab3cd203c2f32d14ad0

%global pypi_name XStatic-JS-Yaml

Name:           python-%{pypi_name}
Version:        3.8.1.0
Release:        29%{?dist}
Summary:        JS-Yaml (XStatic packaging standard)

License:        MIT
URL:            https://github.com/nodeca/js-yaml
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n xstatic-js-yaml-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-js-yaml-common
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-js-yaml-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Patch to use webassets directory
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/js_yaml'|" xstatic/pkg/js_yaml/__init__.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}/%{_jsdir}/js_yaml
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/js_yaml/data/js-yaml.js %{buildroot}/%{_jsdir}/js_yaml
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/js_yaml/data/

%files -n xstatic-js-yaml-common
%doc README.txt
%{_jsdir}/js_yaml

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/js_yaml
%{python3_sitelib}/XStatic_JS_Yaml-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_JS_Yaml-%{version}-py3.*-nspkg.pth

%changelog
%autochangelog
