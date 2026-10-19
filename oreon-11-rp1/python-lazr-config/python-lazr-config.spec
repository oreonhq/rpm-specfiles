%global source0_hash 8fd6611ecf2787d68edac9baa6a07bf9a72321b5456f43e7555c59fa947da1de
Name:           python-lazr-config
Version:        4.0.0
Release:        1%{?dist}
Summary:        Create configuration schemas, and process and validate configurations.
License:        ...
URL:            https://launchpad.net/lazr.config
Source0:        https://files.pythonhosted.org/packages/source/l/lazr_config/lazr_config-%{version}.tar.gz
BuildArch:      noarch
Patch:          lazr.config-avoid-python-sP.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-lazr-config = %{version}-%{release}
# /oreon:deps
%package -n       python3-lazr-config+docs
Summary:        Metapackage for python3-lazr-config docs extras
Requires:       python3-lazr-config = %{version}-%{release}
Provides:       python3dist(lazr-config[docs]) = %{version}-%{release}

%description -n python3-lazr-config+docs
Metapackage for python3-lazr-config docs extras.

%package -n       python3-lazr-config+test
Summary:        Metapackage for python3-lazr-config test extras
Requires:       python3-lazr-config = %{version}-%{release}
Requires:       python3dist(zope.testing) >= 4.6.0
Requires:       python3dist(zope.testrunner) >= 6.6.1
Provides:       python3dist(lazr-config[test]) = %{version}-%{release}

%description -n python3-lazr-config+test
Metapackage for python3-lazr-config test extras.

%description

%package -n     python3-lazr-config
Summary:        Create configuration schemas, and process and validate configurations.
%description -n python3-lazr-config

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lazr_config-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lazr-config usr/lib/python3*/site-packages/lazr_config* usr/lib64/python3*/site-packages/lazr_config* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lazr_config* usr/lib64/python3*/site-packages/lazr_config* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lazr-config -f %{oreon_filedir}/python3-lazr-config.list

%changelog

%autochangelog
