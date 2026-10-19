%global source0_hash fe8b7b67c6c728f017f09b8a6c877c3e3ecbc1344e41c44c7c3405c8c01778fc
Name:           python-linuxdoc
Version:        20260504
Release:        1%{?dist}
Summary:        Sphinx-doc extensions _ tools to extract documentation from C/C++ source file comments.
License:        AGPL-3.0-or-later
URL:            https://github.com/return42/linuxdoc
Source0:        https://files.pythonhosted.org/packages/source/l/linuxdoc/linuxdoc-%{version}.tar.gz
BuildArch:      noarch
Patch:          Fix-compatibility-with-docutils-0.22.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-linuxdoc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-linuxdoc
Summary:        Sphinx-doc extensions _ tools to extract documentation from C/C++ source file comments.
%description -n python3-linuxdoc

%prep
%global oreon_srcdir linuxdoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-linuxdoc usr/lib/python3*/site-packages/linuxdoc* usr/lib64/python3*/site-packages/linuxdoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/linuxdoc* usr/lib64/python3*/site-packages/linuxdoc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-linuxdoc -f %{oreon_filedir}/python3-linuxdoc.list

%changelog

%autochangelog
