%global source0_hash 99d5059f92f721020998695fd9c85289ccb03ec5a2398ad49c6dbe43f19cfb94
Name:           python-zeep
Version:        4.3.3
Release:        1%{?dist}
Summary:        A Python SOAP client
License:        MIT
URL:            https://github.com/mvantellingen/python-zeep
Source0:        https://files.pythonhosted.org/packages/source/z/zeep/zeep-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-zeep = %{version}-%{release}
# /oreon:deps
%package -n       python3-zeep+docs
Summary:        Metapackage for python3-zeep docs extras
Requires:       python3-zeep = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.4.0
Provides:       python3dist(zeep[docs]) = %{version}-%{release}

%description -n python3-zeep+docs
Metapackage for python3-zeep docs extras.

%package -n       python3-zeep+async
Summary:        Metapackage for python3-zeep async extras
Requires:       python3-zeep = %{version}-%{release}
Requires:       python3dist(httpx) >= 0.15.0
Provides:       python3dist(zeep[async]) = %{version}-%{release}

%description -n python3-zeep+async
Metapackage for python3-zeep async extras.

%package -n       python3-zeep+xmlsec
Summary:        Metapackage for python3-zeep xmlsec extras
Requires:       python3-zeep = %{version}-%{release}
Requires:       python3dist(xmlsec) >= 0.6.1
Provides:       python3dist(zeep[xmlsec]) = %{version}-%{release}

%description -n python3-zeep+xmlsec
Metapackage for python3-zeep xmlsec extras.

%description

%package -n     python3-zeep
Summary:        A Python SOAP client
# oreon:reqs
Requires:       python3dist(attrs) >= 17.2.0
Requires:       python3dist(isodate) >= 0.5.4
Requires:       python3dist(lxml) >= 4.6.0
Requires:       python3dist(platformdirs) >= 1.4.0
Requires:       python3dist(requests) >= 2.7.0
Requires:       python3dist(requests-file) >= 1.5.1
Requires:       python3dist(requests-toolbelt) >= 0.7.1
# /oreon:reqs
%description -n python3-zeep

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zeep-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zeep usr/lib/python3*/site-packages/zeep* usr/lib64/python3*/site-packages/zeep* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zeep* usr/lib64/python3*/site-packages/zeep* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zeep -f %{oreon_filedir}/python3-zeep.list

%changelog

%autochangelog
