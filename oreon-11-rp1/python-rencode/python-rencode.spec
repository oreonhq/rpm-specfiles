%global source0_hash ca3afe8d09d26fb48ac0ad6773e35ec0ae1b92d038d217685c54c5a86577e2f2
Name:           python-rencode
Version:        1.0.9
Release:        1%{?dist}
Summary:        rencode is an object serialization library similar to bencode from the Bittorrent project.
License:        GPL-3.0-only
URL:            https://github.com/aresch/rencode
Source0:        https://files.pythonhosted.org/packages/source/r/rencode/rencode-%{version}.tar.gz
Patch:          fix-arm-build.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0.0
BuildRequires:  python3dist(setuptools) >= 64.0.0
Requires:       python3-rencode = %{version}-%{release}
# /oreon:deps
%package -n       python3-rencode+dev
Summary:        Metapackage for python3-rencode dev extras
Requires:       python3-rencode = %{version}-%{release}
Requires:       python3dist(cython) >= 3.0.0
Requires:       python3dist(pytest) >= 8.0.0
Requires:       python3dist(black) >= 24.0.0
Requires:       python3dist(line-profiler) >= 4.2.0
Provides:       python3dist(rencode[dev]) = %{version}-%{release}

%description -n python3-rencode+dev
Metapackage for python3-rencode dev extras.

%description

%package -n     python3-rencode
Summary:        rencode is an object serialization library similar to bencode from the Bittorrent project.
%description -n python3-rencode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rencode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rencode usr/lib/python3*/site-packages/rencode* usr/lib64/python3*/site-packages/rencode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rencode* usr/lib64/python3*/site-packages/rencode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rencode -f %{oreon_filedir}/python3-rencode.list

%changelog

%autochangelog
