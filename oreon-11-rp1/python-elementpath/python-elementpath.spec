%global source0_hash 3c912a9c41311ac5244c038867670d7c0b0fec0e444813608e5b846dbb3428ac
Name:           python-elementpath
Version:        5.1.4
Release:        1%{?dist}
Summary:        XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml
License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source0:        https://files.pythonhosted.org/packages/source/e/elementpath/elementpath-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-elementpath = %{version}-%{release}
# /oreon:deps
%package -n       python3-elementpath+dev
Summary:        Metapackage for python3-elementpath dev extras
Requires:       python3-elementpath = %{version}-%{release}
Requires:       python3dist(tox) >= 4.0
Requires:       python3dist(xmlschema) >= 4.0.1
Provides:       python3dist(elementpath[dev]) = %{version}-%{release}

%description -n python3-elementpath+dev
Metapackage for python3-elementpath dev extras.

%package -n       python3-elementpath+docs
Summary:        Metapackage for python3-elementpath docs extras
Requires:       python3-elementpath = %{version}-%{release}
Provides:       python3dist(elementpath[docs]) = %{version}-%{release}

%description -n python3-elementpath+docs
Metapackage for python3-elementpath docs extras.

%description

%package -n     python3-elementpath
Summary:        XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml
%description -n python3-elementpath

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir elementpath-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-elementpath usr/lib/python3*/site-packages/elementpath* usr/lib64/python3*/site-packages/elementpath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/elementpath* usr/lib64/python3*/site-packages/elementpath* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-elementpath -f %{oreon_filedir}/python3-elementpath.list

%changelog

%autochangelog
