%global source0_hash 13b2beaad985e05e2d6407ee4c4f35590b11f8d693a258a561055cac8f64cab7
Name:           python-annotated-types
Version:        0.8.0
Release:        1%{?dist}
Summary:        Reusable constraint types to use with typing.Annotated
License:        MIT
URL:            https://github.com/annotated-types/annotated-types
Source0:        https://files.pythonhosted.org/packages/source/a/annotated_types/annotated_types-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-annotated-types = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-annotated-types
Summary:        Reusable constraint types to use with typing.Annotated
%description -n python3-annotated-types

%prep
%global oreon_srcdir annotated_types-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-annotated-types usr/lib/python3*/site-packages/annotated_types* usr/lib64/python3*/site-packages/annotated_types* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/annotated_types* usr/lib64/python3*/site-packages/annotated_types* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-annotated-types -f %{oreon_filedir}/python3-annotated-types.list

%changelog

%autochangelog
