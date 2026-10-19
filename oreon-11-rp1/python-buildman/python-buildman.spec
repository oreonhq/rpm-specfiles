%global source0_hash 8143a1f18444a92dd829b1c66eba15a3fc3791ffccc6717b1cbdb0855f86f8af
Name:           python-buildman
Version:        0.0.7
Release:        1%{?dist}
Summary:        Buildman build tool for U-Boot
License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/build/buildman.html
Source0:        https://files.pythonhosted.org/packages/source/b/buildman/buildman-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-buildman = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-buildman
Summary:        Buildman build tool for U-Boot
# oreon:reqs
Requires:       python3dist(filelock) >= 3.0.12
Requires:       python3dist(patch-manager) >= 0.0.6
Requires:       python3dist(u-boot-pylib) >= 0.0.6
# /oreon:reqs
%description -n python3-buildman

%prep
%global oreon_srcdir buildman-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-buildman usr/lib/python3*/site-packages/buildman* usr/lib64/python3*/site-packages/buildman* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/buildman* usr/lib64/python3*/site-packages/buildman* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-buildman -f %{oreon_filedir}/python3-buildman.list

%changelog

%autochangelog
