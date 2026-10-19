%global source0_hash d4a4e44b7c87269ab6c01dfd4c460b8f0492e2377c4215157c285929888efe5c
Name:           python-lazr-uri
Version:        4.0.0
Release:        1%{?dist}
Summary:        A self-contained, easily reusable library for parsing, manipulating, and generating URIs.
License:        ...
URL:            https://launchpad.net/lazr.uri
Source0:        https://files.pythonhosted.org/packages/source/l/lazr_uri/lazr_uri-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-lazr-uri = %{version}-%{release}
# /oreon:deps
%package -n       python3-lazr-uri+docs
Summary:        Metapackage for python3-lazr-uri docs extras
Requires:       python3-lazr-uri = %{version}-%{release}
Provides:       python3dist(lazr-uri[docs]) = %{version}-%{release}

%description -n python3-lazr-uri+docs
Metapackage for python3-lazr-uri docs extras.

%package -n       python3-lazr-uri+test
Summary:        Metapackage for python3-lazr-uri test extras
Requires:       python3-lazr-uri = %{version}-%{release}
Requires:       python3dist(zope.testing) >= 4.6.0
Requires:       python3dist(zope.testrunner) >= 6.6.1
Provides:       python3dist(lazr-uri[test]) = %{version}-%{release}

%description -n python3-lazr-uri+test
Metapackage for python3-lazr-uri test extras.

%description

%package -n     python3-lazr-uri
Summary:        A self-contained, easily reusable library for parsing, manipulating, and generating URIs.
%description -n python3-lazr-uri

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lazr_uri-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lazr-uri usr/lib/python3*/site-packages/lazr_uri* usr/lib64/python3*/site-packages/lazr_uri* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lazr_uri* usr/lib64/python3*/site-packages/lazr_uri* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lazr-uri -f %{oreon_filedir}/python3-lazr-uri.list

%changelog

%autochangelog
