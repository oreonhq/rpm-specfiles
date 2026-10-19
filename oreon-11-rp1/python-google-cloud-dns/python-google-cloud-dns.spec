%global source0_hash 84e87e6bbe11845e3576484f55be5aa44abcbd2e677cd57d3f841e77ab927702
Name:           python-google-cloud-dns
Version:        0.37.1
Release:        1%{?dist}
Summary:        Google Cloud DNS API client library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dns
Source0:        https://files.pythonhosted.org/packages/source/g/google_cloud_dns/google_cloud_dns-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-google-cloud-dns-mock.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-cloud-dns = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-cloud-dns
Summary:        Google Cloud DNS API client library
%description -n python3-google-cloud-dns

%prep
%global oreon_srcdir google_cloud_dns-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-cloud-dns usr/lib/python3*/site-packages/google_cloud_dns* usr/lib64/python3*/site-packages/google_cloud_dns* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_cloud_dns* usr/lib64/python3*/site-packages/google_cloud_dns* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-cloud-dns -f %{oreon_filedir}/python3-google-cloud-dns.list

%changelog

%autochangelog
