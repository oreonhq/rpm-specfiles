%global source0_hash 16ec1cea4cf3dda767e6c0a718f664ef97a34ed24c91998a3c25c3f960c15fba
Name:           python-opcodes
Version:        0.3.14
Release:        1%{?dist}
Summary:        Database of Processor Instructions/Opcodes
License:        ...
URL:            https://github.com/Maratyszcza/Opcodes
Source0:        https://files.pythonhosted.org/packages/source/o/opcodes/opcodes-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opcodes = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opcodes
Summary:        Database of Processor Instructions/Opcodes
%description -n python3-opcodes

%prep
%global oreon_srcdir opcodes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opcodes usr/lib/python3*/site-packages/opcodes* usr/lib64/python3*/site-packages/opcodes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opcodes* usr/lib64/python3*/site-packages/opcodes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opcodes -f %{oreon_filedir}/python3-opcodes.list

%changelog

%autochangelog
