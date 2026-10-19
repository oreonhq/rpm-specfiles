%global source0_hash 233751d7819c9e6743ec1c2405927eb4fa52a284c7b894bd10e28106a9309a92
Name:           python-plumbum
Version:        2.0.2
Release:        1%{?dist}
Summary:        Plumbum: shell combinators library
License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        https://files.pythonhosted.org/packages/source/p/plumbum/plumbum-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-fix-test-on-prerelease-of-3.15.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-plumbum = %{version}-%{release}
# /oreon:deps
%package -n       python3-plumbum+ssh
Summary:        Metapackage for python3-plumbum ssh extras
Requires:       python3-plumbum = %{version}-%{release}
Provides:       python3dist(plumbum[ssh]) = %{version}-%{release}

%description -n python3-plumbum+ssh
Metapackage for python3-plumbum ssh extras.

%description

%package -n     python3-plumbum
Summary:        Plumbum: shell combinators library
%description -n python3-plumbum

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir plumbum-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-plumbum usr/lib/python3*/site-packages/plumbum* usr/lib64/python3*/site-packages/plumbum* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/plumbum* usr/lib64/python3*/site-packages/plumbum* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-plumbum -f %{oreon_filedir}/python3-plumbum.list

%changelog

%autochangelog
