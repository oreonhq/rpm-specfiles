%global source0_hash b97d5d6327067ee6b9dfcbdf606ade9ade70991e19c162e808ea39e5fcf0f8d3
Name:           python-zope-event
Version:        6.2
Release:        1%{?dist}
Summary:        Very basic event publishing system
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.event
Source0:        https://files.pythonhosted.org/packages/source/z/zope_event/zope_event-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 82
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-zope-event = %{version}-%{release}
# /oreon:deps
%package -n       python3-zope-event+docs
Summary:        Metapackage for python3-zope-event docs extras
Requires:       python3-zope-event = %{version}-%{release}
Provides:       python3dist(zope-event[docs]) = %{version}-%{release}

%description -n python3-zope-event+docs
Metapackage for python3-zope-event docs extras.

%package -n       python3-zope-event+test
Summary:        Metapackage for python3-zope-event test extras
Requires:       python3-zope-event = %{version}-%{release}
Requires:       python3dist(zope.testrunner) >= 6.4
Provides:       python3dist(zope-event[test]) = %{version}-%{release}

%description -n python3-zope-event+test
Metapackage for python3-zope-event test extras.

%description

%package -n     python3-zope-event
Summary:        Very basic event publishing system
%description -n python3-zope-event

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_event-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-event usr/lib/python3*/site-packages/zope_event* usr/lib64/python3*/site-packages/zope_event* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_event* usr/lib64/python3*/site-packages/zope_event* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-event -f %{oreon_filedir}/python3-zope-event.list

%changelog

%autochangelog
