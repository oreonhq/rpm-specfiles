%global source0_hash 540ea1ef5cb3dbcb8a21acfa2ee6cee7d8234979a3dd96f64c287616f79b2425
Name:           python-ast-monitor
Version:        0.5.6
Release:        1%{?dist}
Summary:        AST-Monitor is a wearable Raspberry Pi computer for cyclists
License:        MIT
URL:            https://github.com/firefly-cpp/AST-Monitor
Source0:        https://files.pythonhosted.org/packages/source/a/ast_monitor/ast_monitor-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-ast-monitor = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ast-monitor
Summary:        AST-Monitor is a wearable Raspberry Pi computer for cyclists
%description -n python3-ast-monitor

%prep
%global oreon_srcdir ast_monitor-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ast-monitor usr/lib/python3*/site-packages/ast_monitor* usr/lib64/python3*/site-packages/ast_monitor* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ast_monitor* usr/lib64/python3*/site-packages/ast_monitor* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ast-monitor -f %{oreon_filedir}/python3-ast-monitor.list

%changelog

%autochangelog
