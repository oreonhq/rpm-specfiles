%global source0_hash e3b270fe16fc90c50ac79107700330a133dd4c63d22939f5b03b4f24564d5dd8
Name:           python-readchar
Version:        4.2.2
Release:        1%{?dist}
Summary:        Library to easily read single chars and key strokes
License:        MIT
URL:            https://pypi.org/project/readchar
Source0:        https://files.pythonhosted.org/packages/source/r/readchar/readchar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-readchar = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-readchar
Summary:        Library to easily read single chars and key strokes
%description -n python3-readchar

%prep
%global oreon_srcdir readchar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-readchar usr/lib/python3*/site-packages/readchar* usr/lib64/python3*/site-packages/readchar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/readchar* usr/lib64/python3*/site-packages/readchar* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-readchar -f %{oreon_filedir}/python3-readchar.list

%changelog

%autochangelog
