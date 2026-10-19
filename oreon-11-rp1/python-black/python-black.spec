%global source0_hash dd321f668053961824bcc1be1cc1df748b2d7e4fa28086b08331e577b0100a73
Name:           python-black
Version:        26.5.1
Release:        1%{?dist}
Summary:        The uncompromising code formatter.
License:        MIT
URL:            https://github.com/psf/black
Source0:        https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
Patch:          https://github.com/psf/black/commit/14e1de805a.patch
Patch:          https://github.com/psf/black/commit/ed64d89faa.patch
Patch:          https://github.com/psf/black/commit/b0f36f5b42.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-black = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-black
Summary:        The uncompromising code formatter.
%description -n python3-black

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir black-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-black usr/lib/python3*/site-packages/black* usr/lib64/python3*/site-packages/black* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/black* usr/lib64/python3*/site-packages/black* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-black -f %{oreon_filedir}/python3-black.list

%changelog

%autochangelog
