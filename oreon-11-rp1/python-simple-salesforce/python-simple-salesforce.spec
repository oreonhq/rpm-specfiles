%global source0_hash 37737e6256a594e9f07b26bba0f1ba6681e8c7622665abd69311a6008a2d5c0e
Name:           python-simple-salesforce
Version:        1.12.10
Release:        1%{?dist}
Summary:        A basic Salesforce.com REST API client.
License:        Apache-2.0
URL:            https://github.com/simple-salesforce/simple-salesforce
Source0:        https://files.pythonhosted.org/packages/source/s/simple_salesforce/simple_salesforce-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-simple-salesforce = %{version}-%{release}
# /oreon:deps
%package -n       python3-simple-salesforce+test
Summary:        Metapackage for python3-simple-salesforce test extras
Requires:       python3-simple-salesforce = %{version}-%{release}
Requires:       python3dist(pytz) >= 2014.1.1
Requires:       python3dist(responses) >= 0.5.1
Requires:       python3dist(cryptography) > 4.0.0
Provides:       python3dist(simple-salesforce[test]) = %{version}-%{release}

%description -n python3-simple-salesforce+test
Metapackage for python3-simple-salesforce test extras.

%package -n       python3-simple-salesforce+lint
Summary:        Metapackage for python3-simple-salesforce lint extras
Requires:       python3-simple-salesforce = %{version}-%{release}
Provides:       python3dist(simple-salesforce[lint]) = %{version}-%{release}

%description -n python3-simple-salesforce+lint
Metapackage for python3-simple-salesforce lint extras.

%package -n       python3-simple-salesforce+format
Summary:        Metapackage for python3-simple-salesforce format extras
Requires:       python3-simple-salesforce = %{version}-%{release}
Provides:       python3dist(simple-salesforce[format]) = %{version}-%{release}

%description -n python3-simple-salesforce+format
Metapackage for python3-simple-salesforce format extras.

%package -n       python3-simple-salesforce+dev
Summary:        Metapackage for python3-simple-salesforce dev extras
Requires:       python3-simple-salesforce = %{version}-%{release}
Provides:       python3dist(simple-salesforce[dev]) = %{version}-%{release}

%description -n python3-simple-salesforce+dev
Metapackage for python3-simple-salesforce dev extras.

%description

%package -n     python3-simple-salesforce
Summary:        A basic Salesforce.com REST API client.
# oreon:reqs
Requires:       python3dist(requests) >= 2.22.0
# /oreon:reqs
%description -n python3-simple-salesforce

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir simple_salesforce-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-simple-salesforce usr/lib/python3*/site-packages/simple_salesforce* usr/lib64/python3*/site-packages/simple_salesforce* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/simple_salesforce* usr/lib64/python3*/site-packages/simple_salesforce* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-simple-salesforce -f %{oreon_filedir}/python3-simple-salesforce.list

%changelog

%autochangelog
