%global source0_hash 5cd4637ce76312ba1e05eb9c5193fec231f64fee0944e135fa1e951242355b37
Name:           python-multidict
Version:        6.8.0
Release:        1%{?dist}
Summary:        multidict implementation
License:        ...
URL:            https://matrix.to/#/#aio-libs:matrix.org
Source0:        https://files.pythonhosted.org/packages/source/m/multidict/multidict-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 47
Requires:       python3-multidict = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-multidict
Summary:        multidict implementation
%description -n python3-multidict

%prep
%global oreon_srcdir multidict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multidict usr/lib/python3*/site-packages/multidict* usr/lib64/python3*/site-packages/multidict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multidict* usr/lib64/python3*/site-packages/multidict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-multidict -f %{oreon_filedir}/python3-multidict.list

%changelog

%autochangelog
