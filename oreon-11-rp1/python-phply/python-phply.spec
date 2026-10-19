%global source0_hash 0b27774d285f507a3445805a05f8fb2998f56d709270f78b89208b65b0d84917
Name:           python-phply
Version:        1.2.6
Release:        1%{?dist}
Summary:        Lexer and parser for PHP source implemented using PLY
License:        ...
URL:            https://github.com/viraptor/phply
Source0:        https://files.pythonhosted.org/packages/source/p/phply/phply-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-phply = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-phply
Summary:        Lexer and parser for PHP source implemented using PLY
%description -n python3-phply

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir phply-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-phply usr/lib/python3*/site-packages/phply* usr/lib64/python3*/site-packages/phply* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/phply* usr/lib64/python3*/site-packages/phply* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-phply -f %{oreon_filedir}/python3-phply.list

%changelog

%autochangelog
