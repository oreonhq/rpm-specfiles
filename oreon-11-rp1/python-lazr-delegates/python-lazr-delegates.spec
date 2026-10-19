%global source0_hash bb15c21a01b577ab5fac73da61b154dd6fcd377f3af02e522077b4ae11feed37
Name:           python-lazr-delegates
Version:        4.0.0
Release:        1%{?dist}
Summary:        Easily write objects that delegate behavior
License:        ...
URL:            https://launchpad.net/lazr.delegates
Source0:        https://files.pythonhosted.org/packages/source/l/lazr_delegates/lazr_delegates-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-lazr-delegates = %{version}-%{release}
# /oreon:deps
%package -n       python3-lazr-delegates+docs
Summary:        Metapackage for python3-lazr-delegates docs extras
Requires:       python3-lazr-delegates = %{version}-%{release}
Provides:       python3dist(lazr-delegates[docs]) = %{version}-%{release}

%description -n python3-lazr-delegates+docs
Metapackage for python3-lazr-delegates docs extras.

%package -n       python3-lazr-delegates+test
Summary:        Metapackage for python3-lazr-delegates test extras
Requires:       python3-lazr-delegates = %{version}-%{release}
Requires:       python3dist(zope.testing) >= 4.6.0
Requires:       python3dist(zope.testrunner) >= 6.6.1
Provides:       python3dist(lazr-delegates[test]) = %{version}-%{release}

%description -n python3-lazr-delegates+test
Metapackage for python3-lazr-delegates test extras.

%description

%package -n     python3-lazr-delegates
Summary:        Easily write objects that delegate behavior
%description -n python3-lazr-delegates

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lazr_delegates-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lazr-delegates usr/lib/python3*/site-packages/lazr_delegates* usr/lib64/python3*/site-packages/lazr_delegates* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lazr_delegates* usr/lib64/python3*/site-packages/lazr_delegates* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lazr-delegates -f %{oreon_filedir}/python3-lazr-delegates.list

%changelog

%autochangelog
