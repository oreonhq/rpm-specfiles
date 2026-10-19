%global source0_hash 874aaf89765db87a9b911b7a2ca7c5068554868eed9e75c7766affe342a2913d
Name:           python-google-cloud-core
Version:        2.7.0
Release:        1%{?dist}
Summary:        Google Cloud API client core library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-core
Source0:        https://files.pythonhosted.org/packages/source/g/google_cloud_core/google_cloud_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-cloud-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-cloud-core
Summary:        Google Cloud API client core library
%description -n python3-google-cloud-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_cloud_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-cloud-core usr/lib/python3*/site-packages/google_cloud_core* usr/lib64/python3*/site-packages/google_cloud_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_cloud_core* usr/lib64/python3*/site-packages/google_cloud_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-cloud-core -f %{oreon_filedir}/python3-google-cloud-core.list

%changelog

%autochangelog
