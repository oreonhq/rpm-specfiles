%global source0_hash 23d11ebd1b680b3e6a2a926b73de4ffe872cb1ffed8701f257cd1c46d1a840ac
Name:           python-pyrtlsdr
Version:        0.5.0
Release:        1%{?dist}
Summary:        A Python wrapper for librtlsdr _a driver for Realtek RTL2832U based SDRs_
License:        GPL-3.0-or-later
URL:            https://github.com/pyrtlsdr/pyrtlsdr
Source0:        https://files.pythonhosted.org/packages/source/p/pyrtlsdr/pyrtlsdr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pyrtlsdr = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyrtlsdr+lib
Summary:        Metapackage for python3-pyrtlsdr lib extras
Requires:       python3-pyrtlsdr = %{version}-%{release}
Provides:       python3dist(pyrtlsdr[lib]) = %{version}-%{release}

%description -n python3-pyrtlsdr+lib
Metapackage for python3-pyrtlsdr lib extras.

%description

%package -n     python3-pyrtlsdr
Summary:        A Python wrapper for librtlsdr _a driver for Realtek RTL2832U based SDRs_
%description -n python3-pyrtlsdr

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyrtlsdr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyrtlsdr usr/lib/python3*/site-packages/pyrtlsdr* usr/lib64/python3*/site-packages/pyrtlsdr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyrtlsdr* usr/lib64/python3*/site-packages/pyrtlsdr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyrtlsdr -f %{oreon_filedir}/python3-pyrtlsdr.list

%changelog

%autochangelog
