%global source0_hash 52f8962ff0fdae8105d568123b144951257b6bfcfb44ff6f043379c307d0a8ac
Name:           python-click-repl
Version:        0.4.0
Release:        1%{?dist}
Summary:        REPL plugin for Click
License:        MIT
URL:            https://github.com/click-contrib/click-repl
Source0:        https://files.pythonhosted.org/packages/source/c/click_repl/click_repl-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/click-contrib/click-repl/pull/132.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-click-repl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-click-repl
Summary:        REPL plugin for Click
%description -n python3-click-repl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir click_repl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-repl usr/lib/python3*/site-packages/click_repl* usr/lib64/python3*/site-packages/click_repl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_repl* usr/lib64/python3*/site-packages/click_repl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-repl -f %{oreon_filedir}/python3-click-repl.list

%changelog

%autochangelog
