%global source0_hash ba0309fd86be3c27dbf78cdd813c13c5e1df16e5874b99d2535ebbdfb9892993
Name:           python-s3transfer
Version:        0.19.2
Release:        1%{?dist}
Summary:        An Amazon S3 Transfer Manager
License:        ...
URL:            https://github.com/boto/s3transfer
Source0:        https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-s3transfer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-s3transfer
Summary:        An Amazon S3 Transfer Manager
%description -n python3-s3transfer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir s3transfer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-s3transfer usr/lib/python3*/site-packages/s3transfer* usr/lib64/python3*/site-packages/s3transfer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/s3transfer* usr/lib64/python3*/site-packages/s3transfer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-s3transfer -f %{oreon_filedir}/python3-s3transfer.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-2
- Prepare for Oreon 11 (RP1)
