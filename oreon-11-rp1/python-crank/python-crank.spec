%global source0_hash 823df091e2d694bb4fba83ff921e590be3c106494eaac9c8a8c150b617e8b827
Name:           python-crank
Version:        0.9.0
Release:        1%{?dist}
Summary:        Generalization of dispatch mechanism for use across frameworks
License:        MIT
URL:            https://github.com/TurboGears/crank
Source0:        https://files.pythonhosted.org/packages/source/c/crank/crank-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-crank = %{version}-%{release}
# /oreon:deps
%package -n       python3-crank+testing
Summary:        Metapackage for python3-crank testing extras
Requires:       python3-crank = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(crank[testing]) = %{version}-%{release}

%description -n python3-crank+testing
Metapackage for python3-crank testing extras.

%description

%package -n     python3-crank
Summary:        Generalization of dispatch mechanism for use across frameworks
# oreon:reqs
Requires:       python3dist(webob) >= 1.8.0
# /oreon:reqs
%description -n python3-crank

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir crank-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-crank usr/lib/python3*/site-packages/crank* usr/lib64/python3*/site-packages/crank* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/crank* usr/lib64/python3*/site-packages/crank* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-crank -f %{oreon_filedir}/python3-crank.list

%changelog

%autochangelog
