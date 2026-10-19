%global source0_hash b40ef9b4873afb5d0dec02b8d2dfde1cf18c72337b60c99cb735961e0bac05c0
Name:           python-zope-interface
Version:        8.6
Release:        1%{?dist}
Summary:        Interfaces for Python
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.interface
Source0:        https://files.pythonhosted.org/packages/source/z/zope_interface/zope_interface-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zope-interface = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-interface+docs
Summary:        Metapackage for python3-zope-interface docs extras
Requires:       python3-zope-interface = %{version}-%{release}
Provides:       python3dist(zope-interface[docs]) = %{version}-%{release}

%description -n python3-zope-interface+docs
Metapackage for python3-zope-interface docs extras.

%package -n       python3-zope-interface+test
Summary:        Metapackage for python3-zope-interface test extras
Requires:       python3-zope-interface = %{version}-%{release}
Provides:       python3dist(zope-interface[test]) = %{version}-%{release}

%description -n python3-zope-interface+test
Metapackage for python3-zope-interface test extras.

%package -n       python3-zope-interface+testing
Summary:        Metapackage for python3-zope-interface testing extras
Requires:       python3-zope-interface = %{version}-%{release}
Provides:       python3dist(zope-interface[testing]) = %{version}-%{release}

%description -n python3-zope-interface+testing
Metapackage for python3-zope-interface testing extras.

%description

%package -n     python3-zope-interface
Summary:        Interfaces for Python
%description -n python3-zope-interface

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_interface-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-interface usr/lib/python3*/site-packages/zope_interface* usr/lib64/python3*/site-packages/zope_interface* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_interface* usr/lib64/python3*/site-packages/zope_interface* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-interface -f %{oreon_filedir}/python3-zope-interface.list

%changelog

%autochangelog
