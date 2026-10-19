%global source0_hash 33cbfe7924e6d4524dfa9e8bd85608a3b779ecace0d9edb32444a4b356237549
Name:           python-google-cloud-testutils
Version:        1.9.3
Release:        1%{?dist}
Summary:        ...
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/packages/google-cloud-testutils
Source0:        https://files.pythonhosted.org/packages/source/g/google_cloud_testutils/google_cloud_testutils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-cloud-testutils = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-cloud-testutils
Summary:        ...
%description -n python3-google-cloud-testutils

%prep
%global oreon_srcdir google_cloud_testutils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-cloud-testutils usr/lib/python3*/site-packages/google_cloud_testutils* usr/lib64/python3*/site-packages/google_cloud_testutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_cloud_testutils* usr/lib64/python3*/site-packages/google_cloud_testutils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-cloud-testutils -f %{oreon_filedir}/python3-google-cloud-testutils.list

%changelog

%autochangelog
