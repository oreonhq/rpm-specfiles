%global source0_hash 6ffaaab864083a9502455d1bebccb2b558e0e3637e33f7f69003e132f06ec9b3

%global pypi_name XStatic-Angular-Vis

Name:           python-%{pypi_name}
Version:        4.16.0.0
Release:        28%{?dist}
Summary:        Angular-Vis (XStatic packaging standard)

License:        MIT
URL:            https://github.com/visjs/angular-visjs
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n xstatic-angular-vis-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-vis-common
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-vis-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_vis'|" xstatic/pkg/angular_vis/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/angular_vis
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_vis/data/angular-vis.js %{buildroot}/%{_jsdir}/angular_vis
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_vis/data/

%files -n xstatic-angular-vis-common
%doc README.txt
%{_jsdir}/angular_vis

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_vis
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py3.*-nspkg.pth

%changelog
%autochangelog
