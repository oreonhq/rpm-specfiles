%global source0_hash 14bc073439513d7773662a338f4db9829cf16c12b74b9568e2d2689975fbd7fc
Name:           python-semver
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python helper for Semantic Versioning _https://semver.org_
License:        ...
URL:            https://github.com/python-semver/python-semver
Source0:        https://files.pythonhosted.org/packages/source/s/semver/semver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-semver = %{version}-%{release}
# /oreon:deps
%package -n       python3-semver+native
Summary:        Metapackage for python3-semver native extras
Requires:       python3-semver = %{version}-%{release}
Requires:       python3dist(fast-semver-rs-backend) >= 0.1.1
Provides:       python3dist(semver[native]) = %{version}-%{release}

%description -n python3-semver+native
Metapackage for python3-semver native extras.

%description

%package -n     python3-semver
Summary:        Python helper for Semantic Versioning _https://semver.org_
%description -n python3-semver

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir semver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-semver usr/lib/python3*/site-packages/semver* usr/lib64/python3*/site-packages/semver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/semver* usr/lib64/python3*/site-packages/semver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-semver -f %{oreon_filedir}/python3-semver.list

%changelog

%autochangelog
