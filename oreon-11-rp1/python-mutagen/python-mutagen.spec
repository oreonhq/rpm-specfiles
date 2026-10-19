%global source0_hash 8f95637ab9f6f305cec6bd1294e197debe207998e3e068596563c74f86b0a173
Name:           python-mutagen
Version:        1.48.1
Release:        1%{?dist}
Summary:        read and write audio tags for many formats
License:        GPL-2.0-or-later
URL:            https://mutagen.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/m/mutagen/mutagen-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-mutagen = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mutagen
Summary:        read and write audio tags for many formats
%description -n python3-mutagen

%prep
%global oreon_srcdir mutagen-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mutagen usr/lib/python3*/site-packages/mutagen* usr/lib64/python3*/site-packages/mutagen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mutagen* usr/lib64/python3*/site-packages/mutagen* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mutagen -f %{oreon_filedir}/python3-mutagen.list

%changelog

%autochangelog
