%global source0_hash 2ea980955530499865225eff917b649b39fd014b53f8c6461b6348c1d8b866f1
Name:           python-archspec
Version:        0.2.6
Release:        1%{?dist}
Summary:        A library to query system architecture
License:        Apache-2.0 OR MIT
URL:            https://github.com/archspec/archspec.git
Source0:        https://files.pythonhosted.org/packages/source/a/archspec/archspec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-archspec = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-archspec
Summary:        A library to query system architecture
%description -n python3-archspec

%prep
%global oreon_srcdir archspec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-archspec usr/lib/python3*/site-packages/archspec* usr/lib64/python3*/site-packages/archspec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/archspec* usr/lib64/python3*/site-packages/archspec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-archspec -f %{oreon_filedir}/python3-archspec.list

%changelog

%autochangelog
