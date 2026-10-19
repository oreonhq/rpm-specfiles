%global source0_hash 8cfc8b33a5cb16e733bd60cffca9732c0d1d761ecd80a89f34ed7df2cd38d6d6
Name:           python-pika
Version:        1.4.4
Release:        1%{?dist}
Summary:        Pika Python AMQP Client Library
License:        BSD-3-Clause
URL:            https://pika.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/pika/pika-%{version}.tar.gz
BuildArch:      noarch
Patch:          python3.14.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-pika = %{version}-%{release}
# /oreon:deps
%package -n       python3-pika+gevent
Summary:        Metapackage for python3-pika gevent extras
Requires:       python3-pika = %{version}-%{release}
Provides:       python3dist(pika[gevent]) = %{version}-%{release}

%description -n python3-pika+gevent
Metapackage for python3-pika gevent extras.

%package -n       python3-pika+tornado
Summary:        Metapackage for python3-pika tornado extras
Requires:       python3-pika = %{version}-%{release}
Provides:       python3dist(pika[tornado]) = %{version}-%{release}

%description -n python3-pika+tornado
Metapackage for python3-pika tornado extras.

%package -n       python3-pika+twisted
Summary:        Metapackage for python3-pika twisted extras
Requires:       python3-pika = %{version}-%{release}
Provides:       python3dist(pika[twisted]) = %{version}-%{release}

%description -n python3-pika+twisted
Metapackage for python3-pika twisted extras.

%description

%package -n     python3-pika
Summary:        Pika Python AMQP Client Library
%description -n python3-pika

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pika-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pika usr/lib/python3*/site-packages/pika* usr/lib64/python3*/site-packages/pika* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pika* usr/lib64/python3*/site-packages/pika* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pika -f %{oreon_filedir}/python3-pika.list

%changelog

%autochangelog
