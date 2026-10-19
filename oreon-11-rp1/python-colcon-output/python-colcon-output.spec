%global source0_hash db72d0353938c4e85866d9515be08149a2dd216705528b98d092a645b2abac1a
Name:           python-colcon-output
Version:        0.2.15
Release:        1%{?dist}
Summary:        Extension for colcon to customize the output in various ways.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-output/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_output/colcon_output-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-output = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-output
Summary:        Extension for colcon to customize the output in various ways.
%description -n python3-colcon-output

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_output-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-output usr/lib/python3*/site-packages/colcon_output* usr/lib64/python3*/site-packages/colcon_output* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_output* usr/lib64/python3*/site-packages/colcon_output* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-output -f %{oreon_filedir}/python3-colcon-output.list

%changelog

%autochangelog
