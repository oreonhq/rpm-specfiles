%global source0_hash 91dba1187e4c35fd37380a56ac228bbd54c6c649b2351829f3bf033718277537
%bcond_with developer_tools
Name:           python-sphinx-tabs
Version:        3.5.0
Release:        1%{?dist}
Summary:        Tabbed views for Sphinx
License:        MIT
URL:            https://github.com/executablebooks/sphinx-tabs
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_tabs/sphinx_tabs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-tabs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-tabs
Summary:        Tabbed views for Sphinx
%description -n python3-sphinx-tabs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%if %{with developer_tools}
%endif

%prep
%global oreon_srcdir sphinx_tabs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-tabs usr/lib/python3*/site-packages/sphinx_tabs* usr/lib64/python3*/site-packages/sphinx_tabs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_tabs* usr/lib64/python3*/site-packages/sphinx_tabs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-tabs -f %{oreon_filedir}/python3-sphinx-tabs.list

%changelog

%autochangelog
