%global source0_hash 434a134456c2ad832c319dee1cf9aa881a3bd1cd8500c2df2a8dd5e513c2fe2b

%global pypi_name XStatic-Angular-UUID

Name:           python-%{pypi_name}
Version:        0.0.4.0
Release:        31%{?dist}
Summary:        Angular-UUID (XStatic packaging standard)

License:        MIT
URL:            https://github.com/munkychop/angular-uuid
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Angular-UUID JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n xstatic-angular-uuid-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-uuid-common
Angular-UUID JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-uuid-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Angular-UUID JavaScript library packaged for setup-tools (easy_install) / pip.

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
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_uuid'|" xstatic/pkg/angular_uuid/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/angular_uuid
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_uuid/data/angular-uuid.js %{buildroot}/%{_jsdir}/angular_uuid
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_uuid/data/

%files -n xstatic-angular-uuid-common
%doc README.txt
%{_jsdir}/angular_uuid

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_uuid
%{python3_sitelib}/XStatic_Angular_UUID-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_Angular_UUID-%{version}-py3.*-nspkg.pth

%changelog
%autochangelog
