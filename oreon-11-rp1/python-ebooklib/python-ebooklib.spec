%global source0_hash 35e2f9d7d39907be8d39ae2deb261b19848945903ae3dbb6577b187ead69e985
Name:           python-ebooklib
Version:        0.20
Release:        1%{?dist}
Summary:        Ebook library which can handle EPUB2/EPUB3 format
License:        AGPL-3.0-or-later
URL:            https://github.com/aerkalov/ebooklib
Source0:        https://files.pythonhosted.org/packages/source/e/ebooklib/ebooklib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ebooklib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ebooklib
Summary:        Ebook library which can handle EPUB2/EPUB3 format
%description -n python3-ebooklib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ebooklib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ebooklib usr/lib/python3*/site-packages/ebooklib* usr/lib64/python3*/site-packages/ebooklib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ebooklib* usr/lib64/python3*/site-packages/ebooklib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ebooklib -f %{oreon_filedir}/python3-ebooklib.list

%changelog

%autochangelog
