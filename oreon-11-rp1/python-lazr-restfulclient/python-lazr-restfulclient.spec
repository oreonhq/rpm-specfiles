%global source0_hash 79577938dabce496675454105c37c5aa06deed7928818a98411adfb22f9e294b
Name:           python-lazr-restfulclient
Version:        4.0.0
Release:        1%{?dist}
Summary:        A programmable client library that takes advantage of the commonalities among lazr.restful web services.
License:        ...
URL:            https://launchpad.net/lazr.restfulclient
Source0:        https://files.pythonhosted.org/packages/source/l/lazr_restfulclient/lazr_restfulclient-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-lazr-restfulclient = %{version}-%{release}
# /oreon:deps
%package -n       python3-lazr-restfulclient+docs
Summary:        Metapackage for python3-lazr-restfulclient docs extras
Requires:       python3-lazr-restfulclient = %{version}-%{release}
Provides:       python3dist(lazr-restfulclient[docs]) = %{version}-%{release}

%description -n python3-lazr-restfulclient+docs
Metapackage for python3-lazr-restfulclient docs extras.

%package -n       python3-lazr-restfulclient+test
Summary:        Metapackage for python3-lazr-restfulclient test extras
Requires:       python3-lazr-restfulclient = %{version}-%{release}
Requires:       python3dist(fixtures) >= 1.3.0
Requires:       python3dist(lazr.restful) >= 0.11.0
Requires:       python3dist(zope.testing) >= 4.6.0
Requires:       python3dist(zope.testrunner) >= 6.6.1
Provides:       python3dist(lazr-restfulclient[test]) = %{version}-%{release}

%description -n python3-lazr-restfulclient+test
Metapackage for python3-lazr-restfulclient test extras.

%description

%package -n     python3-lazr-restfulclient
Summary:        A programmable client library that takes advantage of the commonalities among lazr.restful web services.
# oreon:reqs
Requires:       python3dist(httplib2) >= 0.7.7
Requires:       python3dist(wadllib) >= 1.1.4
# /oreon:reqs
%description -n python3-lazr-restfulclient

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lazr_restfulclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lazr-restfulclient usr/lib/python3*/site-packages/lazr_restfulclient* usr/lib64/python3*/site-packages/lazr_restfulclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lazr_restfulclient* usr/lib64/python3*/site-packages/lazr_restfulclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lazr-restfulclient -f %{oreon_filedir}/python3-lazr-restfulclient.list

%changelog

%autochangelog
