%global source0_hash 82c4f9bbf4b03be5162a24d6d8e4fdbfe3ed2602d3ebcbf505a33350a379dcb7
Name:           python-genshi
Version:        0.7.11
Release:        1%{?dist}
Summary:        A toolkit for generation of output for the web
License:        ...
URL:            https://github.com/edgewall/genshi
Source0:        https://files.pythonhosted.org/packages/source/g/genshi/genshi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-genshi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-genshi
Summary:        A toolkit for generation of output for the web
%description -n python3-genshi

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir genshi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-genshi usr/lib/python3*/site-packages/genshi* usr/lib64/python3*/site-packages/genshi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/genshi* usr/lib64/python3*/site-packages/genshi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-genshi -f %{oreon_filedir}/python3-genshi.list

%changelog

%autochangelog
