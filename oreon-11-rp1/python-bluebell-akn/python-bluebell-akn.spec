%global source0_hash 8066e08bc4b8bb137788f03b11faf684937d11bb995a91b2db048e3e90e2e38a
Name:           python-bluebell-akn
Version:        5.0.0
Release:        1%{?dist}
Summary:        Transforms text to and from Akoma Ntoso
License:        LGPL-3.0-or-later
URL:            https://github.com/laws-africa/bluebell
Source0:        https://files.pythonhosted.org/packages/source/b/bluebell_akn/bluebell_akn-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 1.8
Requires:       python3-bluebell-akn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bluebell-akn
Summary:        Transforms text to and from Akoma Ntoso
%description -n python3-bluebell-akn

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir bluebell_akn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bluebell-akn usr/lib/python3*/site-packages/bluebell_akn* usr/lib64/python3*/site-packages/bluebell_akn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bluebell_akn* usr/lib64/python3*/site-packages/bluebell_akn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bluebell-akn -f %{oreon_filedir}/python3-bluebell-akn.list

%changelog

%autochangelog
