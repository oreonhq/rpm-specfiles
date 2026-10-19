%global source0_hash 0de47f3c1a96cbec15ae7a1607d5a142ec39e501728055434358c2f4cf0f21a9
Name:           python-zope-testing
Version:        6.2
Release:        1%{?dist}
Summary:        Zope testing helpers
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testing
Source0:        https://files.pythonhosted.org/packages/source/z/zope_testing/zope_testing-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 82
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-zope-testing = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-testing+test
Summary:        Metapackage for python3-zope-testing test extras
Requires:       python3-zope-testing = %{version}-%{release}
Requires:       python3dist(zope.testrunner) >= 6.4
Provides:       python3dist(zope-testing[test]) = %{version}-%{release}

%description -n python3-zope-testing+test
Metapackage for python3-zope-testing test extras.

%package -n       python3-zope-testing+docs
Summary:        Metapackage for python3-zope-testing docs extras
Requires:       python3-zope-testing = %{version}-%{release}
Provides:       python3dist(zope-testing[docs]) = %{version}-%{release}

%description -n python3-zope-testing+docs
Metapackage for python3-zope-testing docs extras.

%description

%package -n     python3-zope-testing
Summary:        Zope testing helpers
%description -n python3-zope-testing

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_testing-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-testing usr/lib/python3*/site-packages/zope_testing* usr/lib64/python3*/site-packages/zope_testing* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_testing* usr/lib64/python3*/site-packages/zope_testing* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-testing -f %{oreon_filedir}/python3-zope-testing.list

%changelog

%autochangelog
