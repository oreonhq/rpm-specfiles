%global source0_hash b49b78cc7ec0b252bfbd74cef0187121b18e4f5a0c57e3b9c3d8fc15090af3b4
Name:           python-tempora
Version:        5.12.0
Release:        1%{?dist}
Summary:        ...
License:        Apache-2.0
URL:            https://github.com/jaraco/tempora
Source0:        https://files.pythonhosted.org/packages/source/t/tempora/tempora-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-tempora = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tempora
Summary:        ...
%description -n python3-tempora

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tempora-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tempora usr/lib/python3*/site-packages/tempora* usr/lib64/python3*/site-packages/tempora* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tempora* usr/lib64/python3*/site-packages/tempora* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tempora -f %{oreon_filedir}/python3-tempora.list

%changelog

%autochangelog
