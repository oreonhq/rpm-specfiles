%global source0_hash 7f7243a114fdb06a2a97dcf6b16c7b1f99168827a5e7ee09ebcd210c76745dee
Name:           python-zope-i18nmessageid
Version:        8.3
Release:        1%{?dist}
Summary:        Message Identifiers for internationalization
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.i18nmessageid
Source0:        https://files.pythonhosted.org/packages/source/z/zope_i18nmessageid/zope_i18nmessageid-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zope-i18nmessageid = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-i18nmessageid+docs
Summary:        Metapackage for python3-zope-i18nmessageid docs extras
Requires:       python3-zope-i18nmessageid = %{version}-%{release}
Provides:       python3dist(zope-i18nmessageid[docs]) = %{version}-%{release}

%description -n python3-zope-i18nmessageid+docs
Metapackage for python3-zope-i18nmessageid docs extras.

%package -n       python3-zope-i18nmessageid+test
Summary:        Metapackage for python3-zope-i18nmessageid test extras
Requires:       python3-zope-i18nmessageid = %{version}-%{release}
Requires:       python3dist(zope.testrunner) >= 6.4
Provides:       python3dist(zope-i18nmessageid[test]) = %{version}-%{release}

%description -n python3-zope-i18nmessageid+test
Metapackage for python3-zope-i18nmessageid test extras.

%package -n       python3-zope-i18nmessageid+testing
Summary:        Metapackage for python3-zope-i18nmessageid testing extras
Requires:       python3-zope-i18nmessageid = %{version}-%{release}
Requires:       python3dist(zope.testrunner) >= 6.4
Provides:       python3dist(zope-i18nmessageid[testing]) = %{version}-%{release}

%description -n python3-zope-i18nmessageid+testing
Metapackage for python3-zope-i18nmessageid testing extras.

%description

%package -n     python3-zope-i18nmessageid
Summary:        Message Identifiers for internationalization
%description -n python3-zope-i18nmessageid

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_i18nmessageid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-i18nmessageid usr/lib/python3*/site-packages/zope_i18nmessageid* usr/lib64/python3*/site-packages/zope_i18nmessageid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_i18nmessageid* usr/lib64/python3*/site-packages/zope_i18nmessageid* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-i18nmessageid -f %{oreon_filedir}/python3-zope-i18nmessageid.list

%changelog

%autochangelog
