%global source0_hash 0b85fbef5e10c4e5b4aef8f059da49e3c770ef659b471e82d90b7b95791b9291
Name:           python-zuul-sphinx
Version:        0.8.1
Release:        1%{?dist}
Summary:        A Sphinx extension for documenting Zuul jobs
License:        ...
URL:            https://docs.openstack.org/infra/zuul-sphinx/
Source0:        https://files.pythonhosted.org/packages/source/z/zuul_sphinx/zuul_sphinx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zuul-sphinx = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-zuul-sphinx
Summary:        A Sphinx extension for documenting Zuul jobs
%description -n python3-zuul-sphinx

%prep
%global oreon_srcdir zuul_sphinx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zuul-sphinx usr/lib/python3*/site-packages/zuul_sphinx* usr/lib64/python3*/site-packages/zuul_sphinx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zuul_sphinx* usr/lib64/python3*/site-packages/zuul_sphinx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zuul-sphinx -f %{oreon_filedir}/python3-zuul-sphinx.list

%changelog

%autochangelog
