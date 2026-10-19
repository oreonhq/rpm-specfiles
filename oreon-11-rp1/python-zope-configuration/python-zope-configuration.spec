%global source0_hash 5af51cefb4dcc66053e54cfece38483fb593a81be1010c38587dba91c9d154ac
Name:           python-zope-configuration
Version:        7.1
Release:        1%{?dist}
Summary:        Zope Configuration Markup Language _ZCML_
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.configuration
Source0:        https://files.pythonhosted.org/packages/source/z/zope_configuration/zope_configuration-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 81
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-zope-configuration = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-configuration+docs
Summary:        Metapackage for python3-zope-configuration docs extras
Requires:       python3-zope-configuration = %{version}-%{release}
Provides:       python3dist(zope-configuration[docs]) = %{version}-%{release}

%description -n python3-zope-configuration+docs
Metapackage for python3-zope-configuration docs extras.

%package -n       python3-zope-configuration+test
Summary:        Metapackage for python3-zope-configuration test extras
Requires:       python3-zope-configuration = %{version}-%{release}
Requires:       python3dist(zope.testrunner) >= 6.4
Provides:       python3dist(zope-configuration[test]) = %{version}-%{release}

%description -n python3-zope-configuration+test
Metapackage for python3-zope-configuration test extras.

%description

%package -n     python3-zope-configuration
Summary:        Zope Configuration Markup Language _ZCML_
# oreon:reqs
Requires:       python3dist(zope.schema) >= 4.9
# /oreon:reqs
%description -n python3-zope-configuration

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_configuration-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-configuration usr/lib/python3*/site-packages/zope_configuration* usr/lib64/python3*/site-packages/zope_configuration* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_configuration* usr/lib64/python3*/site-packages/zope_configuration* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-configuration -f %{oreon_filedir}/python3-zope-configuration.list

%changelog

%autochangelog
