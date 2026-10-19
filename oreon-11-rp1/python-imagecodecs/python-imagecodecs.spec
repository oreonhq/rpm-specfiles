%global source0_hash 03a6add9ad9ba61dce1520489fd090b1b5cf2a2701a9666d1ab8e7653278175f
Name:           python-imagecodecs
Version:        2026.8.16
Release:        1%{?dist}
Summary:        Image transformation, compression, and decompression codecs
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/imagecodecs
Source0:        https://files.pythonhosted.org/packages/source/i/imagecodecs/imagecodecs-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.2
BuildRequires:  python3dist(numpy) >= 2.1
Requires:       python3-imagecodecs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-imagecodecs
Summary:        Image transformation, compression, and decompression codecs
%description -n python3-imagecodecs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir imagecodecs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-imagecodecs usr/lib/python3*/site-packages/imagecodecs* usr/lib64/python3*/site-packages/imagecodecs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/imagecodecs* usr/lib64/python3*/site-packages/imagecodecs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-imagecodecs -f %{oreon_filedir}/python3-imagecodecs.list

%changelog

%autochangelog
