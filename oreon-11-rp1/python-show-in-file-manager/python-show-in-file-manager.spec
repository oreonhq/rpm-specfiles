%global source0_hash 559b596e3e563800cf69d734cd236824279a9d820d1d841640c5f13e0058f9b6
Name:           python-show-in-file-manager
Version:        1.1.6
Release:        1%{?dist}
Summary:        Open the system file manager and select files in it
License:        MIT
URL:            https://github.com/damonlynch/showinfilemanager
Source0:        https://files.pythonhosted.org/packages/source/s/show_in_file_manager/show_in_file_manager-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-show-in-file-manager = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-show-in-file-manager
Summary:        Open the system file manager and select files in it
# oreon:reqs
Requires:       python3dist(pywin32) >= 301
Requires:       python3dist(pyxdg) >= 0.25
# /oreon:reqs
%description -n python3-show-in-file-manager

%prep
%global oreon_srcdir show_in_file_manager-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-show-in-file-manager usr/lib/python3*/site-packages/show_in_file_manager* usr/lib64/python3*/site-packages/show_in_file_manager* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/show_in_file_manager* usr/lib64/python3*/site-packages/show_in_file_manager* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-show-in-file-manager -f %{oreon_filedir}/python3-show-in-file-manager.list

%changelog

%autochangelog
