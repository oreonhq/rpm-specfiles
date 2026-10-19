%global source0_hash dcbd2c47ad87688facaef5cc11aab6d1ec9ed05645fed97a5de7204d5d17cc44
Name:           python-fabric
Version:        3.2.3
Release:        1%{?dist}
Summary:        High level SSH command execution
License:        ...
URL:            https://github.com/fabric/fabric
Source0:        https://files.pythonhosted.org/packages/source/f/fabric/fabric-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fabric = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fabric
Summary:        High level SSH command execution
%description -n python3-fabric

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fabric-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fabric usr/lib/python3*/site-packages/fabric* usr/lib64/python3*/site-packages/fabric* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fabric* usr/lib64/python3*/site-packages/fabric* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fabric -f %{oreon_filedir}/python3-fabric.list

%changelog

%autochangelog
