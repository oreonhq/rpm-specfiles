%global source0_hash 46d64e77e8d95e5c76c7d9a94ff05d8b38b2ae4e1d4869eb0235024b6fcb5212
Name:           python-vcrpy
Version:        8.3.0
Release:        1%{?dist}
Summary:        Automatically mock your HTTP interactions to simplify and speed up testing
License:        MIT
URL:            https://github.com/kevin1024/vcrpy
Source0:        https://files.pythonhosted.org/packages/source/v/vcrpy/vcrpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-vcrpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-vcrpy+tests
Summary:        Metapackage for python3-vcrpy tests extras
Requires:       python3-vcrpy = %{version}-%{release}
Requires:       python3dist(httpbin) >= 0.10.3
Requires:       python3dist(requests) >= 2.22.0
Provides:       python3dist(vcrpy[tests]) = %{version}-%{release}

%description -n python3-vcrpy+tests
Metapackage for python3-vcrpy tests extras.

%package -n       python3-vcrpy+tests-niquests
Summary:        Metapackage for python3-vcrpy tests-niquests extras
Requires:       python3-vcrpy = %{version}-%{release}
Requires:       python3dist(httpbin) >= 0.10.3
Provides:       python3dist(vcrpy[tests-niquests]) = %{version}-%{release}

%description -n python3-vcrpy+tests-niquests
Metapackage for python3-vcrpy tests-niquests extras.

%description

%package -n     python3-vcrpy
Summary:        Automatically mock your HTTP interactions to simplify and speed up testing
%description -n python3-vcrpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir vcrpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-vcrpy usr/lib/python3*/site-packages/vcrpy* usr/lib64/python3*/site-packages/vcrpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/vcrpy* usr/lib64/python3*/site-packages/vcrpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-vcrpy -f %{oreon_filedir}/python3-vcrpy.list

%changelog

%autochangelog
