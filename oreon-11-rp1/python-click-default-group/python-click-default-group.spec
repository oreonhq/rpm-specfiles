%global source0_hash eb3f3c99ec0d456ca6cd2a7f08f7d4e91771bef51b01bdd9580cc6450fe1251e
Name:           python-click-default-group
Version:        1.2.4
Release:        1%{?dist}
Summary:        click_default_group
License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/click-contrib/click-default-group
Source0:        https://files.pythonhosted.org/packages/source/c/click_default_group/click_default_group-%{version}.tar.gz
BuildArch:      noarch
Patch0:         https://patch-diff.githubusercontent.com/raw/click-contrib/click-default-group/pull/18.patch#/0001-Fix-detection-of-error-message.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-click-default-group = %{version}-%{release}
# /oreon:deps
%package -n       python3-click-default-group+test
Summary:        Metapackage for python3-click-default-group test extras
Requires:       python3-click-default-group = %{version}-%{release}
Provides:       python3dist(click-default-group[test]) = %{version}-%{release}

%description -n python3-click-default-group+test
Metapackage for python3-click-default-group test extras.

%description

%package -n     python3-click-default-group
Summary:        click_default_group
%description -n python3-click-default-group

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir click_default_group-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-default-group usr/lib/python3*/site-packages/click_default_group* usr/lib64/python3*/site-packages/click_default_group* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_default_group* usr/lib64/python3*/site-packages/click_default_group* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-default-group -f %{oreon_filedir}/python3-click-default-group.list

%changelog

%autochangelog
