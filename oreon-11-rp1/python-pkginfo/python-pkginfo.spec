%global source0_hash 4f70471c643f71fe84a06230c0e33c5c5b12a33b2fd21bff14ddaef5a974adb1
Name:           python-pkginfo
Version:        1.13
Release:        1%{?dist}
Summary:        Query metadata from sdists / bdists / installed packages.
License:        MIT
URL:            https://code.launchpad.net/~tseaver/pkginfo/trunk
Source0:        https://files.pythonhosted.org/packages/source/p/pkginfo/pkginfo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pkginfo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pkginfo
Summary:        Query metadata from sdists / bdists / installed packages.
%description -n python3-pkginfo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pkginfo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pkginfo usr/lib/python3*/site-packages/pkginfo* usr/lib64/python3*/site-packages/pkginfo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pkginfo* usr/lib64/python3*/site-packages/pkginfo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pkginfo -f %{oreon_filedir}/python3-pkginfo.list

%changelog

%autochangelog
