%global source0_hash 2ae308d2f4f1e9145f5f4ba57f840fbfd1c2983ee26e4824347789649d3ae298
Name:           python-domdf-python-tools
Version:        3.10.0
Release:        1%{?dist}
Summary:        Helpful functions for Python 🐍 🛠️
License:        MIT
URL:            https://github.com/domdfcoding/domdf_python_tools
Source0:        https://files.pythonhosted.org/packages/source/d/domdf_python_tools/domdf_python_tools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-domdf-python-tools = %{version}-%{release}
# /oreon:deps
%package -n       python3-domdf-python-tools+dates
Summary:        Metapackage for python3-domdf-python-tools dates extras
Requires:       python3-domdf-python-tools = %{version}-%{release}
Requires:       python3dist(pytz) >= 2019.1
Provides:       python3dist(domdf-python-tools[dates]) = %{version}-%{release}

%description -n python3-domdf-python-tools+dates
Metapackage for python3-domdf-python-tools dates extras.

%package -n       python3-domdf-python-tools+testing
Summary:        Metapackage for python3-domdf-python-tools testing extras
Requires:       python3-domdf-python-tools = %{version}-%{release}
Provides:       python3dist(domdf-python-tools[testing]) = %{version}-%{release}

%description -n python3-domdf-python-tools+testing
Metapackage for python3-domdf-python-tools testing extras.

%package -n       python3-domdf-python-tools+all
Summary:        Metapackage for python3-domdf-python-tools all extras
Requires:       python3-domdf-python-tools = %{version}-%{release}
Requires:       python3dist(pytz) >= 2019.1
Provides:       python3dist(domdf-python-tools[all]) = %{version}-%{release}

%description -n python3-domdf-python-tools+all
Metapackage for python3-domdf-python-tools all extras.

%description

%package -n     python3-domdf-python-tools
Summary:        Helpful functions for Python 🐍 🛠️
%description -n python3-domdf-python-tools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir domdf_python_tools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-domdf-python-tools usr/lib/python3*/site-packages/domdf_python_tools* usr/lib64/python3*/site-packages/domdf_python_tools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/domdf_python_tools* usr/lib64/python3*/site-packages/domdf_python_tools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-domdf-python-tools -f %{oreon_filedir}/python3-domdf-python-tools.list

%changelog

%autochangelog
