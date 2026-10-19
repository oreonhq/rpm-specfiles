%global source0_hash 14420786778039872ec2dc47af9adf4ea449bd6d80094acf966c1653814b02ef
Name:           python-lfpykit
Version:        0.6.2
Release:        1%{?dist}
Summary:        Electrostatic models for multicompartment neuron models
License:        ...
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/l/lfpykit/lfpykit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-lfpykit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lfpykit
Summary:        Electrostatic models for multicompartment neuron models
%description -n python3-lfpykit

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lfpykit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lfpykit usr/lib/python3*/site-packages/lfpykit* usr/lib64/python3*/site-packages/lfpykit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lfpykit* usr/lib64/python3*/site-packages/lfpykit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lfpykit -f %{oreon_filedir}/python3-lfpykit.list

%changelog

%autochangelog
