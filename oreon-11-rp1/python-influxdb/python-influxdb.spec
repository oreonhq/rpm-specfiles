%global source0_hash 58c647f6043712dd86e9aee12eb4ccfbbb5415467bc9910a48aa8c74c1108970
Name:           python-influxdb
Version:        5.3.2
Release:        1%{?dist}
Summary:        InfluxDB client
License:        MIT
URL:            https://github.com/influxdb/influxdb-python
Source0:        https://files.pythonhosted.org/packages/source/i/influxdb/influxdb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-influxdb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-influxdb
Summary:        InfluxDB client
%description -n python3-influxdb

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir influxdb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-influxdb usr/lib/python3*/site-packages/influxdb* usr/lib64/python3*/site-packages/influxdb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/influxdb* usr/lib64/python3*/site-packages/influxdb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-influxdb -f %{oreon_filedir}/python3-influxdb.list

%changelog

%autochangelog
