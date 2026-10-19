%global source0_hash 58961e8b853fec98a0c24697ac5bb5352b4b58e4a4a82f51f037f6c04accd58f
Name:           python-openant
Version:        1.3.4
Release:        1%{?dist}
Summary:        ANT, ANT-FS and ANT+ Python Library
License:        ...
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/o/openant/openant-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.7.2
Requires:       python3-openant = %{version}-%{release}
# /oreon:deps
%package -n       python3-openant+serial
Summary:        Metapackage for python3-openant serial extras
Requires:       python3-openant = %{version}-%{release}
Provides:       python3dist(openant[serial]) = %{version}-%{release}

%description -n python3-openant+serial
Metapackage for python3-openant serial extras.

%package -n       python3-openant+influx
Summary:        Metapackage for python3-openant influx extras
Requires:       python3-openant = %{version}-%{release}
Provides:       python3dist(openant[influx]) = %{version}-%{release}

%description -n python3-openant+influx
Metapackage for python3-openant influx extras.

%package -n       python3-openant+mqtt
Summary:        Metapackage for python3-openant mqtt extras
Requires:       python3-openant = %{version}-%{release}
Provides:       python3dist(openant[mqtt]) = %{version}-%{release}

%description -n python3-openant+mqtt
Metapackage for python3-openant mqtt extras.

%package -n       python3-openant+test
Summary:        Metapackage for python3-openant test extras
Requires:       python3-openant = %{version}-%{release}
Provides:       python3dist(openant[test]) = %{version}-%{release}

%description -n python3-openant+test
Metapackage for python3-openant test extras.

%package -n       python3-openant+docs
Summary:        Metapackage for python3-openant docs extras
Requires:       python3-openant = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.2.3
Requires:       python3dist(furo) >= 2021.3.20b30
Provides:       python3dist(openant[docs]) = %{version}-%{release}

%description -n python3-openant+docs
Metapackage for python3-openant docs extras.

%description

%package -n     python3-openant
Summary:        ANT, ANT-FS and ANT+ Python Library
# oreon:reqs
Requires:       python3dist(pyusb) >= 1.1.1
# /oreon:reqs
%description -n python3-openant

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir openant-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openant usr/lib/python3*/site-packages/openant* usr/lib64/python3*/site-packages/openant* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openant* usr/lib64/python3*/site-packages/openant* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openant -f %{oreon_filedir}/python3-openant.list

%changelog

%autochangelog
