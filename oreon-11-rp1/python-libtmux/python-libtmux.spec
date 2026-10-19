%global source0_hash 41e9e80602b2656fd119b13253b27bad46af5cfef32099be53cdd391e2936b61
Name:           python-libtmux
Version:        0.62.0
Release:        1%{?dist}
Summary:        Typed library that provides an ORM wrapper for tmux, a terminal multiplexer.
License:        MIT
URL:            https://github.com/tmux-python/libtmux
Source0:        https://files.pythonhosted.org/packages/source/l/libtmux/libtmux-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{srcname}-no-gp-libs.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libtmux = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-libtmux
Summary:        Typed library that provides an ORM wrapper for tmux, a terminal multiplexer.
%description -n python3-libtmux

%prep
%global oreon_srcdir libtmux-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libtmux usr/lib/python3*/site-packages/libtmux* usr/lib64/python3*/site-packages/libtmux* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libtmux* usr/lib64/python3*/site-packages/libtmux* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-libtmux -f %{oreon_filedir}/python3-libtmux.list

%changelog

%autochangelog
