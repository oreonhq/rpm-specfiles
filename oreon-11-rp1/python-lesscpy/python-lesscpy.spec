%global source0_hash 4f6b7f34c22c5ce137e7ee280dcb1984ade0d500b6dab591d4a4d84252d18de9
Name:           python-lesscpy
Version:        0.15.2
Release:        1%{?dist}
Summary:        Python LESS compiler
License:        MIT
URL:            https://github.com/lesscpy/lesscpy
Source0:        https://files.pythonhosted.org/packages/source/l/lesscpy/lesscpy-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-Remove-tabfile-support-as-PLY-removed-it-as-well.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-lesscpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-lesscpy+test
Summary:        Metapackage for python3-lesscpy test extras
Requires:       python3-lesscpy = %{version}-%{release}
Provides:       python3dist(lesscpy[test]) = %{version}-%{release}

%description -n python3-lesscpy+test
Metapackage for python3-lesscpy test extras.

%package -n       python3-lesscpy+release
Summary:        Metapackage for python3-lesscpy release extras
Requires:       python3-lesscpy = %{version}-%{release}
Provides:       python3dist(lesscpy[release]) = %{version}-%{release}

%description -n python3-lesscpy+release
Metapackage for python3-lesscpy release extras.

%package -n       python3-lesscpy+tox
Summary:        Metapackage for python3-lesscpy tox extras
Requires:       python3-lesscpy = %{version}-%{release}
Provides:       python3dist(lesscpy[tox]) = %{version}-%{release}

%description -n python3-lesscpy+tox
Metapackage for python3-lesscpy tox extras.

%description

%package -n     python3-lesscpy
Summary:        Python LESS compiler
%description -n python3-lesscpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lesscpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lesscpy usr/lib/python3*/site-packages/lesscpy* usr/lib64/python3*/site-packages/lesscpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lesscpy* usr/lib64/python3*/site-packages/lesscpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lesscpy -f %{oreon_filedir}/python3-lesscpy.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.0-24
- Prepare for Oreon 11 (RP1)
