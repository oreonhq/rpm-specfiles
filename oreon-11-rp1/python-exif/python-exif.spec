%global source0_hash none

%global srcname exif-py

Summary:        Python module to extract EXIF information
Name:           python-exif
Version:        3.5.1
Release:        3%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ianare/exif-py
Source0:        https://github.com/ianare/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%global _description\
Python Library to extract EXIF information in digital camera image files.
%description %_description

%package -n    python3-exif
Summary:       Python 3 module to extract EXIF information
%description -n python3-exif %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l exifread
ln -s EXIF.py %{buildroot}%{_bindir}/EXIF
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%pytest

%files -n python3-exif -f %{pyproject_files}
%doc README.rst
%{_bindir}/EXIF
%{_bindir}/EXIF.py

%changelog
%autochangelog
