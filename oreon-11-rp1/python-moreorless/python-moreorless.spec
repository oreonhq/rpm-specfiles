%global source0_hash 175e8afa824006c4356353d97b1cc9699a6ef68a851e0859257cde8d00e88a64
Name:           python-moreorless
Version:        0.6.0
Release:        1%{?dist}
Summary:        Python diff wrapper
License:        MIT
URL:            https://github.com/thatch/moreorless/
Source0:        https://files.pythonhosted.org/packages/source/m/moreorless/moreorless-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8.0
Requires:       python3-moreorless = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-moreorless
Summary:        Python diff wrapper
%description -n python3-moreorless

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir moreorless-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-moreorless usr/lib/python3*/site-packages/moreorless* usr/lib64/python3*/site-packages/moreorless* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/moreorless* usr/lib64/python3*/site-packages/moreorless* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-moreorless -f %{oreon_filedir}/python3-moreorless.list

%changelog

%autochangelog
