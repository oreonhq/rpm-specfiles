%global source0_hash 329b9810d66988f48e127a6bd18cc8efbbd1cd20b8deb4691a35738af49ad88d

%global pypi_name sphinxcontrib-apidoc

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        %autorelease
Summary:        A Sphinx extension for running 'sphinx-apidoc' on each build

License:        LicenseRef-Callaway-BSD
URL:            http://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_apidoc/sphinxcontrib_apidoc-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-sphinx

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%global common_desc \
This package contains Sphinx extension for running sphinx-apidoc_ \
on each build.Overview *sphinx-apidoc* is a tool for automatic generation \
of Sphinx sources that, using the autodoc <sphinx_autodoc>_ extension, \
documents a whole package in the style of other automatic API documentation \
tools. *sphinx-apidoc* does not actually build documentation - rather it \
simply generates it.

%description
%common_desc

%package -n python3-%{pypi_name}
Summary:    %{summary}
Requires:   python3-pbr
Requires:   python3-sphinx

%description -n python3-%{pypi_name}
%common_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinxcontrib_apidoc-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sphinxcontrib

%check
%pyproject_check_import
%{pytest}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{python3_sitelib}/sphinxcontrib_apidoc*nspkg.pth

%changelog
%autochangelog
