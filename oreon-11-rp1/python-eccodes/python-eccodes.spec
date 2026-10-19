%global source0_hash 7ea659eb15044f6ac809636ca1712cd026cdbfad5a189f4c55d86a8711ab1a9d
Name:           python-eccodes
Version:        2.48.0
Release:        1%{?dist}
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder
License:        ...
URL:            https://github.com/ecmwf/eccodes-python
Source0:        https://files.pythonhosted.org/packages/source/e/eccodes/eccodes-%{version}.tar.gz
Patch1:         python-eccodes-setup.patch
Patch2:         python-eccodes-sphinx-config.patch
Patch3:         python-eccodes-disable-findlibs.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-eccodes = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-eccodes
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder
%description -n python3-eccodes

%prep
%global oreon_srcdir eccodes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-eccodes usr/lib/python3*/site-packages/eccodes* usr/lib64/python3*/site-packages/eccodes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/eccodes* usr/lib64/python3*/site-packages/eccodes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-eccodes -f %{oreon_filedir}/python3-eccodes.list

%changelog

%autochangelog
