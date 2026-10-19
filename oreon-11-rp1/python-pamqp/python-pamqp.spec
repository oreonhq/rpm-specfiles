%global source0_hash 9dd13b828e346622793981f14a5df817fce5de998c746209d6c0154eb8403970
Name:           python-pamqp
Version:        4.0.1
Release:        1%{?dist}
Summary:        RabbitMQ Focused AMQP low-level library
License:        BSD-3-Clause
URL:            https://github.com/gmr/pamqp
Source0:        https://files.pythonhosted.org/packages/source/p/pamqp/pamqp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pamqp = %{version}-%{release}
# /oreon:deps
%package -n       python3-pamqp+codegen
Summary:        Metapackage for python3-pamqp codegen extras
Requires:       python3-pamqp = %{version}-%{release}
Provides:       python3dist(pamqp[codegen]) = %{version}-%{release}

%description -n python3-pamqp+codegen
Metapackage for python3-pamqp codegen extras.

%description

%package -n     python3-pamqp
Summary:        RabbitMQ Focused AMQP low-level library
%description -n python3-pamqp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pamqp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pamqp usr/lib/python3*/site-packages/pamqp* usr/lib64/python3*/site-packages/pamqp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pamqp* usr/lib64/python3*/site-packages/pamqp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pamqp -f %{oreon_filedir}/python3-pamqp.list

%changelog

%autochangelog
