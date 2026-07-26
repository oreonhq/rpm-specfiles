%global source0_hash 5cb56f0090cb6489d643730de57c68d8a6714f2b9fe526ac89bb68f5d77dfe10

%global pypi_name XStatic-Bootstrap-SCSS

Name:           python-%{pypi_name}
Version:        3.4.1.0
Release:        %autorelease
Summary:        Bootstrap-SCSS (XStatic packaging standard)

License:        MIT
URL:            https://getbootstrap.com/
Source0:        %{pypi_source}
Source1:        halflings-license.eml

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-XStatic
Requires:       xstatic-bootstrap-scss-common

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%package -n xstatic-bootstrap-scss-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-bootstrap-scss-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/bootstrap_scss'|" xstatic/pkg/bootstrap_scss/__init__.py

# Include email identifying the license for the Glyphicons Halflings font
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_jsdir}/bootstrap_scss
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/bootstrap_scss/data/* %{buildroot}%{_jsdir}/bootstrap_scss
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/bootstrap_scss/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/bootstrap_scss/js/*.js
chmod 644 %{buildroot}%{_jsdir}/bootstrap_scss/js/bootstrap/*.js

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/
%{python3_sitelib}/XStatic_Bootstrap_SCSS-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/xstatic_bootstrap_scss-%{version}.dist-info/

%files -n xstatic-bootstrap-scss-common
%doc README.txt
%license halflings-license.eml
%{_jsdir}/bootstrap_scss

%changelog
%autochangelog
