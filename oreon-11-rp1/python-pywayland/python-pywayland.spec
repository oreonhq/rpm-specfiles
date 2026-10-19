%global source0_hash 9d8478f5b0df3540333ccf85a55fe8b34150b2c28c685805de9ffa855898549e
Name:           python-pywayland
Version:        0.4.19
Release:        1%{?dist}
Summary:        Python bindings for the libwayland library written in pure Python
License:        Apache-2.0
URL:            https://github.com/flacjacket/pywayland
Source0:        https://files.pythonhosted.org/packages/source/p/pywayland/pywayland-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.12.0
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-pywayland = %{version}-%{release}
# /oreon:deps
%package -n       python3-pywayland+test
Summary:        Metapackage for python3-pywayland test extras
Requires:       python3-pywayland = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.15.0
Requires:       python3dist(coveralls) >= 4.1.0
Requires:       python3dist(setuptools) >= 77.0.0
Provides:       python3dist(pywayland[test]) = %{version}-%{release}

%description -n python3-pywayland+test
Metapackage for python3-pywayland test extras.

%package -n       python3-pywayland+docs
Summary:        Metapackage for python3-pywayland docs extras
Requires:       python3-pywayland = %{version}-%{release}
Provides:       python3dist(pywayland[docs]) = %{version}-%{release}

%description -n python3-pywayland+docs
Metapackage for python3-pywayland docs extras.

%description

%package -n     python3-pywayland
Summary:        Python bindings for the libwayland library written in pure Python
# oreon:reqs
Requires:       python3dist(cffi) >= 1.12.0
# /oreon:reqs
%description -n python3-pywayland

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pywayland-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pywayland usr/lib/python3*/site-packages/pywayland* usr/lib64/python3*/site-packages/pywayland* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pywayland* usr/lib64/python3*/site-packages/pywayland* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pywayland -f %{oreon_filedir}/python3-pywayland.list

%changelog

%autochangelog
