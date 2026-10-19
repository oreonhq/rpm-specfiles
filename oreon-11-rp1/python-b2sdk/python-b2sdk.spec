%global source0_hash edb586be7698b4b868194506cd81d594364e445817461c7e7b43df47378f6827
Name:           python-b2sdk
Version:        2.13.0
Release:        1%{?dist}
Summary:        Backblaze B2 SDK
License:        MIT
URL:            https://github.com/Backblaze/b2-sdk-python
Source0:        https://files.pythonhosted.org/packages/source/b/b2sdk/b2sdk-%{version}.tar.gz
BuildArch:      noarch
Patch0:         relax-setuptools_scm-version.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.4
BuildRequires:  python3dist(hatchling) >= 1.24.2
Requires:       python3-b2sdk = %{version}-%{release}
# /oreon:deps
%package -n       python3-b2sdk+full
Summary:        Metapackage for python3-b2sdk full extras
Requires:       python3-b2sdk = %{version}-%{release}
Requires:       python3dist(tqdm) < 5.0.0
Requires:       python3dist(tqdm) >= 4.5.0
Requires:       python3dist(pydantic) >= 2.0.1
Requires:       python3dist(pydantic) < 2.13
Provides:       python3dist(b2sdk[full]) = %{version}-%{release}

%description -n python3-b2sdk+full
Metapackage for python3-b2sdk full extras.

%description

%package -n     python3-b2sdk
Summary:        Backblaze B2 SDK
# oreon:reqs
Requires:       python3dist(annotated-types) >= 0.5.0
Requires:       python3dist(logfury) < 2.0.0
Requires:       python3dist(logfury) >= 1.0.1
Requires:       python3dist(requests) < 3.0.0
Requires:       python3dist(requests) >= 2.33.0
Requires:       python3dist(typing-extensions) >= 4.7.1
# /oreon:reqs
%description -n python3-b2sdk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir b2sdk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-b2sdk usr/lib/python3*/site-packages/b2sdk* usr/lib64/python3*/site-packages/b2sdk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/b2sdk* usr/lib64/python3*/site-packages/b2sdk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-b2sdk -f %{oreon_filedir}/python3-b2sdk.list

%changelog

%autochangelog
