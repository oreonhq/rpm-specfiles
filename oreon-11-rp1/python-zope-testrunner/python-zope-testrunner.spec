%global source0_hash 6fef88117314676650829140c2a9038fb7a0b46fd7c01a29dd7f2842bfc614d7
Name:           python-zope-testrunner
Version:        8.3
Release:        1%{?dist}
Summary:        Zope testrunner script.
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testrunner
Source0:        https://files.pythonhosted.org/packages/source/z/zope_testrunner/zope_testrunner-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 82
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-zope-testrunner = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-testrunner+test
Summary:        Metapackage for python3-zope-testrunner test extras
Requires:       python3-zope-testrunner = %{version}-%{release}
Provides:       python3dist(zope-testrunner[test]) = %{version}-%{release}

%description -n python3-zope-testrunner+test
Metapackage for python3-zope-testrunner test extras.

%package -n       python3-zope-testrunner+subunit
Summary:        Metapackage for python3-zope-testrunner subunit extras
Requires:       python3-zope-testrunner = %{version}-%{release}
Requires:       python3dist(python-subunit) >= 1.4.3
Requires:       python3dist(testtools) >= 0.9.30
Provides:       python3dist(zope-testrunner[subunit]) = %{version}-%{release}

%description -n python3-zope-testrunner+subunit
Metapackage for python3-zope-testrunner subunit extras.

%package -n       python3-zope-testrunner+docs
Summary:        Metapackage for python3-zope-testrunner docs extras
Requires:       python3-zope-testrunner = %{version}-%{release}
Provides:       python3dist(zope-testrunner[docs]) = %{version}-%{release}

%description -n python3-zope-testrunner+docs
Metapackage for python3-zope-testrunner docs extras.

%description

%package -n     python3-zope-testrunner
Summary:        Zope testrunner script.
%description -n python3-zope-testrunner

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_testrunner-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-testrunner usr/lib/python3*/site-packages/zope_testrunner* usr/lib64/python3*/site-packages/zope_testrunner* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_testrunner* usr/lib64/python3*/site-packages/zope_testrunner* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-testrunner -f %{oreon_filedir}/python3-zope-testrunner.list

%changelog

%autochangelog
