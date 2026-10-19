%global source0_hash e69da08c9d47d9424268a958be682bc1b108f38b2fcf50f37187e37afd4a266b
Name:           python-gearbox
Version:        0.5.0
Release:        1%{?dist}
Summary:        Command line toolkit born as a PasteScript replacement for the TurboGears2 web framework
License:        MIT
URL:            https://github.com/TurboGears/gearbox
Source0:        https://files.pythonhosted.org/packages/source/g/gearbox/gearbox-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-gearbox = %{version}-%{release}
# /oreon:deps
%package -n       python3-gearbox+test
Summary:        Metapackage for python3-gearbox test extras
Requires:       python3-gearbox = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(gearbox[test]) = %{version}-%{release}

%description -n python3-gearbox+test
Metapackage for python3-gearbox test extras.

%description

%package -n     python3-gearbox
Summary:        Command line toolkit born as a PasteScript replacement for the TurboGears2 web framework
# oreon:reqs
Requires:       python3dist(hupper) >= 1.3
Requires:       python3dist(pastedeploy) >= 3.1.0
# /oreon:reqs
%description -n python3-gearbox

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gearbox-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gearbox usr/lib/python3*/site-packages/gearbox* usr/lib64/python3*/site-packages/gearbox* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gearbox* usr/lib64/python3*/site-packages/gearbox* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gearbox -f %{oreon_filedir}/python3-gearbox.list

%changelog

%autochangelog
