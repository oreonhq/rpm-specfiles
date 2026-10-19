%global source0_hash 5d2cf97c66bc42a6b583be0e307eae5a3945438322e2ed0c5e4f14dc251d693d
Name:           python-glfw
Version:        2.10.2
Release:        1%{?dist}
Summary:        A ctypes-based wrapper for GLFW3.
License:        MIT
URL:            https://github.com/FlorianRhiem/pyGLFW
Source0:        https://files.pythonhosted.org/packages/source/g/glfw/glfw-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-glfw = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-glfw
Summary:        A ctypes-based wrapper for GLFW3.
%description -n python3-glfw

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir glfw-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-glfw usr/lib/python3*/site-packages/glfw* usr/lib64/python3*/site-packages/glfw* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/glfw* usr/lib64/python3*/site-packages/glfw* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-glfw -f %{oreon_filedir}/python3-glfw.list

%changelog

%autochangelog
