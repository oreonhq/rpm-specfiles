%global source0_hash d6df0c8c896e160087c6981f3770ed513ec973a9f4066b9e4b0614eb08ba0ce1
Name:           python-rebulk
Version:        6.0.1
Release:        1%{?dist}
Summary:        Rebulk - Define simple search patterns in bulk to perform advanced matching on any string.
License:        MIT
URL:            https://github.com/Toilal/rebulk/
Source0:        https://files.pythonhosted.org/packages/source/r/rebulk/rebulk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.12
BuildRequires:  python3dist(uv-build) >= 0.11
Requires:       python3-rebulk = %{version}-%{release}
# /oreon:deps
%package -n       python3-rebulk+native
Summary:        Metapackage for python3-rebulk native extras
Requires:       python3-rebulk = %{version}-%{release}
Provides:       python3dist(rebulk[native]) = %{version}-%{release}

%description -n python3-rebulk+native
Metapackage for python3-rebulk native extras.

%description

%package -n     python3-rebulk
Summary:        Rebulk - Define simple search patterns in bulk to perform advanced matching on any string.
%description -n python3-rebulk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rebulk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rebulk usr/lib/python3*/site-packages/rebulk* usr/lib64/python3*/site-packages/rebulk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rebulk* usr/lib64/python3*/site-packages/rebulk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rebulk -f %{oreon_filedir}/python3-rebulk.list

%changelog

%autochangelog
