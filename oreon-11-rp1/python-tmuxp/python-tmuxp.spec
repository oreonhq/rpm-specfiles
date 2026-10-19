%global source0_hash 9e0480ea012999602635887e0461d395c2d8aa6e36a85b5a6d1d65dcd6c7809c
Name:           python-tmuxp
Version:        1.74.0
Release:        1%{?dist}
Summary:        Session manager for tmux, which allows users to save and load tmux sessions through simple configuration files.
License:        MIT
URL:            https://github.com/tmux-python/tmuxp
Source0:        https://files.pythonhosted.org/packages/source/t/tmuxp/tmuxp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tmuxp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tmuxp
Summary:        Session manager for tmux, which allows users to save and load tmux sessions through simple configuration files.
# oreon:reqs
Requires:       python3dist(tmuxp) >= 1.7.0
# /oreon:reqs
%description -n python3-tmuxp

%prep
%global oreon_srcdir tmuxp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tmuxp usr/lib/python3*/site-packages/tmuxp* usr/lib64/python3*/site-packages/tmuxp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tmuxp* usr/lib64/python3*/site-packages/tmuxp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tmuxp -f %{oreon_filedir}/python3-tmuxp.list

%changelog

%autochangelog
