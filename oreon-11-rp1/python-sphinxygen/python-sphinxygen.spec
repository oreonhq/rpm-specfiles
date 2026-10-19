%global source0_hash b1ac1515e84fa4c31dc10ad1a7800c0f305a1a3887b4b4e6e1980ceda4f50173
Name:           python-sphinxygen
Version:        1.0.12
Release:        1%{?dist}
Summary:        A script to read Doxygen XML output and emit ReST for Sphinx
License:        ISC
URL:            https://gitlab.com/drobilla/sphinxygen
Source0:        https://gitlab.com/drobilla/sphinxygen/-/archive/v%{version}/sphinxygen-v%{version}.tar.gz
Patch:          0001-Fix-tests-with-doxygen-1.14.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-sphinxygen = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxygen+testing
Summary:        Metapackage for python3-sphinxygen testing extras
Requires:       python3-sphinxygen = %{version}-%{release}
Provides:       python3dist(sphinxygen[testing]) = %{version}-%{release}

%description -n python3-sphinxygen+testing
Metapackage for python3-sphinxygen testing extras.

%description

%package -n python3-sphinxygen
Summary:        A script to read Doxygen XML output and emit ReST for Sphinx
%description -n python3-sphinxygen

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinxygen-v%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
chmod 644 %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py
sed -i '/^#!\/usr\/bin/d' %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py
mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 doc/sphinxygen.1 -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles python3-sphinxygen usr/lib/python3*/site-packages/sphinxygen* usr/lib64/python3*/site-packages/sphinxygen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxygen* usr/lib64/python3*/site-packages/sphinxygen* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-sphinxygen -f %{oreon_filedir}/python3-sphinxygen.list

%changelog

%autochangelog
