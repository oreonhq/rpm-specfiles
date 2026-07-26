%global source0_hash a9b69a53fdd8d8fda042b9ed7bbb09969d6e3aa22243459958891cb7e9ce3524

%global pypi_name XStatic-Json2yaml

Name:           python-%{pypi_name}
Version:        0.1.1.0
Release:        28%{?dist}
Summary:        Json2yaml (XStatic packaging standard)

License:        MIT
URL:            https://github.com/jeffsu/json2yaml
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n xstatic-json2yaml-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-json2yaml-common
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-json2yaml-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Json2yaml JavaScript library packaged for setup-tools (easy_install) / pip.

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
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/json2yaml'|" xstatic/pkg/json2yaml/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/json2yaml
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/json2yaml/data/json2yaml.js %{buildroot}/%{_jsdir}/json2yaml
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/json2yaml/data/

%files -n xstatic-json2yaml-common
%doc README.txt
%{_jsdir}/json2yaml

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/json2yaml
%{python3_sitelib}/XStatic_Json2yaml-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_Json2yaml-%{version}-py3.*-nspkg.pth

%changelog
%autochangelog
