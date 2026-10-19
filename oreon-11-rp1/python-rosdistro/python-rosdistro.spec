%global source0_hash 81a0c4e51a1bfbdcab026365a0053ae55f877a398a7b56ea1411c3bf68c4f822
Name:           python-rosdistro
Version:        1.1.0
Release:        1%{?dist}
Summary:        A tool to work with rosdistro files
License:        ...
URL:            https://github.com/ros-infrastructure/rosdistro
Source0:        https://files.pythonhosted.org/packages/source/r/rosdistro/rosdistro-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rosdistro = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rosdistro
Summary:        A tool to work with rosdistro files
%description -n python3-rosdistro

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rosdistro-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rosdistro usr/lib/python3*/site-packages/rosdistro* usr/lib64/python3*/site-packages/rosdistro* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rosdistro* usr/lib64/python3*/site-packages/rosdistro* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rosdistro -f %{oreon_filedir}/python3-rosdistro.list

%changelog

%autochangelog
