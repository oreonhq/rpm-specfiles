%global source0_hash e59f90fc632da6d7438cd3acbd0b7a4e583a1ffa5e2fac4929c79b48913a71a6

%global pypi_name XStatic-Patternfly-Bootstrap-Treeview

Name:           python-%{pypi_name}
Version:        2.1.3.2
Release:        34%{?dist}
Summary:        Patternfly Bootstrap Treeview CSS/JS framework (XStatic packaging standard)

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://www.patternfly.org/
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-patternfly-bootstrap-treeview-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%package -n xstatic-patternfly-bootstrap-treeview-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-patternfly-bootstrap-treeview-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/patternfly_bootstrap_treeview'|" xstatic/pkg/patternfly_bootstrap_treeview/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_jsdir}/patternfly_bootstrap_treeview
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/patternfly_bootstrap_treeview/data/* %{buildroot}%{_jsdir}/patternfly_bootstrap_treeview
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/patternfly_bootstrap_treeview/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/patternfly_bootstrap_treeview/js/*.js

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/xstatic/pkg/patternfly_bootstrap_treeview
%{python3_sitelib}/XStatic_Patternfly_Bootstrap_Treeview-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Patternfly_Bootstrap_Treeview-%{version}-py%{python3_version}-nspkg.pth

%files -n xstatic-patternfly-bootstrap-treeview-common
%doc README.rst
%{_jsdir}/patternfly_bootstrap_treeview

%changelog
%autochangelog
