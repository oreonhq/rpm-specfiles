%global source0_hash 3c79502d56cf6b76210032e1c53494ddfbc73c140bccf2ef4092b3f0825323ab
Name:           python-fastavro
Version:        1.12.2
Release:        1%{?dist}
Summary:        Fast read/write of AVRO files
License:        MIT
URL:            https://github.com/fastavro/fastavro
Source0:        https://files.pythonhosted.org/packages/source/f/fastavro/fastavro-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastavro = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastavro
Summary:        Fast read/write of AVRO files
%description -n python3-fastavro

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fastavro-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastavro usr/lib/python3*/site-packages/fastavro* usr/lib64/python3*/site-packages/fastavro* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastavro* usr/lib64/python3*/site-packages/fastavro* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastavro -f %{oreon_filedir}/python3-fastavro.list

%changelog

%autochangelog
