%global source0_hash 67cc773182c0958f09835b9d30f4851860ede89766d57d01f17821b4596fd555
Name:           python-colcon-metadata
Version:        0.3.1
Release:        1%{?dist}
Summary:        Extension for colcon to read package metadata from files.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-metadata/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_metadata/colcon_metadata-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-metadata = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-metadata
Summary:        Extension for colcon to read package metadata from files.
%description -n python3-colcon-metadata

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_metadata-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-metadata usr/lib/python3*/site-packages/colcon_metadata* usr/lib64/python3*/site-packages/colcon_metadata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_metadata* usr/lib64/python3*/site-packages/colcon_metadata* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-metadata -f %{oreon_filedir}/python3-colcon-metadata.list

%changelog

%autochangelog
