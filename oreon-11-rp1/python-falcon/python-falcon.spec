%global source0_hash b5081be62f1e2d4f5140f4bad6993fd2bf8b1e503ee7261f56d324b87e41a67a
Name:           python-falcon
Version:        4.3.1
Release:        1%{?dist}
Summary:        The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.
License:        Apache-2.0
URL:            https://falconframework.org
Source0:        https://files.pythonhosted.org/packages/source/f/falcon/falcon-%{version}.tar.gz
Patch:          0001-Remove-coverage-test-requirement.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0.8
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-falcon = %{version}-%{release}
# /oreon:deps
%package -n       python3-falcon+test
Summary:        Metapackage for python3-falcon test extras
Requires:       python3-falcon = %{version}-%{release}
Provides:       python3dist(falcon[test]) = %{version}-%{release}

%description -n python3-falcon+test
Metapackage for python3-falcon test extras.

%description

%package -n     python3-falcon
Summary:        The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.
%description -n python3-falcon

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir falcon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-falcon usr/lib/python3*/site-packages/falcon* usr/lib64/python3*/site-packages/falcon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/falcon* usr/lib64/python3*/site-packages/falcon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-falcon -f %{oreon_filedir}/python3-falcon.list

%changelog

%autochangelog
