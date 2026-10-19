%global source0_hash 2ad086262b5bd3b3804f2d044926e5f63d8f6ae72b235d8b774f164b79f587c4
Name:           python-tifffile
Version:        2026.9.15
Release:        1%{?dist}
Summary:        Read and write TIFF files
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/tifffile
Source0:        https://files.pythonhosted.org/packages/source/t/tifffile/tifffile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tifffile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tifffile
Summary:        Read and write TIFF files
%description -n python3-tifffile

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tifffile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tifffile usr/lib/python3*/site-packages/tifffile* usr/lib64/python3*/site-packages/tifffile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tifffile* usr/lib64/python3*/site-packages/tifffile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tifffile -f %{oreon_filedir}/python3-tifffile.list

%changelog

%autochangelog
