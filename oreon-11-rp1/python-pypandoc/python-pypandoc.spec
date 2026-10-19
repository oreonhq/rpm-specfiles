%global source0_hash 51179abfd6e582a25ed03477541b48836b5bba5a4c3b282a547630793934d799
Name:           python-pypandoc
Version:        1.17
Release:        1%{?dist}
Summary:        Thin wrapper for pandoc.
License:        MIT
URL:            https://github.com/JessicaTegner/pypandoc
Source0:        https://files.pythonhosted.org/packages/source/p/pypandoc/pypandoc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pypandoc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pypandoc
Summary:        Thin wrapper for pandoc.
%description -n python3-pypandoc

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pypandoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypandoc usr/lib/python3*/site-packages/pypandoc* usr/lib64/python3*/site-packages/pypandoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypandoc* usr/lib64/python3*/site-packages/pypandoc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypandoc -f %{oreon_filedir}/python3-pypandoc.list

%changelog

%autochangelog
