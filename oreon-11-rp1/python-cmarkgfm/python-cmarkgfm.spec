%global source0_hash 5bec61007b65b919488442c838c58a6c8bf4741f5103c593b2ef180d39818eda
Name:           python-cmarkgfm
Version:        2025.10.22
Release:        1%{?dist}
Summary:        Minimal bindings to GitHub_s fork of cmark
License:        MIT
URL:            https://github.com/theacodes/cmarkgfm
Source0:        https://files.pythonhosted.org/packages/source/c/cmarkgfm/cmarkgfm-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 2.0.0
BuildRequires:  python3dist(pycparser) >= 2.06
BuildRequires:  python3dist(setuptools) >= 80.9.0
Requires:       python3-cmarkgfm = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cmarkgfm
Summary:        Minimal bindings to GitHub_s fork of cmark
# oreon:reqs
Requires:       python3dist(cffi) >= 2.0.0
# /oreon:reqs
%description -n python3-cmarkgfm

%prep
%global oreon_srcdir cmarkgfm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cmarkgfm usr/lib/python3*/site-packages/cmarkgfm* usr/lib64/python3*/site-packages/cmarkgfm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cmarkgfm* usr/lib64/python3*/site-packages/cmarkgfm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cmarkgfm -f %{oreon_filedir}/python3-cmarkgfm.list

%changelog

%autochangelog
