%global source0_hash 1de441703cd298d75a419bfdc0066e9fc7b0a1de630df96eea8ce8f5c759358c
Name:           python-google-resumable-media
Version:        2.10.2
Release:        1%{?dist}
Summary:        Utilities for Google Media Downloads and Resumable Uploads
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-resumable-media
Source0:        https://files.pythonhosted.org/packages/source/g/google_resumable_media/google_resumable_media-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-resumable-media = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-resumable-media
Summary:        Utilities for Google Media Downloads and Resumable Uploads
%description -n python3-google-resumable-media

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_resumable_media-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-resumable-media usr/lib/python3*/site-packages/google_resumable_media* usr/lib64/python3*/site-packages/google_resumable_media* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_resumable_media* usr/lib64/python3*/site-packages/google_resumable_media* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-resumable-media -f %{oreon_filedir}/python3-google-resumable-media.list

%changelog

%autochangelog
