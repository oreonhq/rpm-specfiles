%global source0_hash 720f18440dad67b0b4b23fac2a54e3bd020245876836b16a8dfedec6a6ea8598
Name:           python-mock-ssh-server
Version:        0.9.1
Release:        1%{?dist}
Summary:        Mock SSH server for testing purposes
License:        MIT
URL:            https://github.com/carletes/mock-ssh-server
Source0:        https://files.pythonhosted.org/packages/source/m/mock-ssh-server/mock-ssh-server-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mock-ssh-server = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mock-ssh-server
Summary:        Mock SSH server for testing purposes
%description -n python3-mock-ssh-server

%prep
%global oreon_srcdir mock-ssh-server-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mock-ssh-server usr/lib/python3*/site-packages/mock_ssh_server* usr/lib64/python3*/site-packages/mock_ssh_server* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mock_ssh_server* usr/lib64/python3*/site-packages/mock_ssh_server* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mock-ssh-server -f %{oreon_filedir}/python3-mock-ssh-server.list

%changelog

%autochangelog
