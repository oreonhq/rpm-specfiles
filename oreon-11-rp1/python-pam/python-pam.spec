%global source0_hash 04598b0fba9e3fa290f27e4f8d1762a9d61b75f1e38b53e9d8d861af53eb0d2a
Name:           python-pam
Version:        2.1.0
Release:        1%{?dist}
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
License:        MIT
URL:            https://github.com/FirefighterBlu3/python-pam
Source0:        https://files.pythonhosted.org/packages/source/p/python_pam/python_pam-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pam = %{version}-%{release}
# /oreon:deps
%description
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%package -n python3-pam
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
%{?python_provide:%python_provide python3-pam}
%description -n python3-pam
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python_pam-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pam usr/lib/python3*/site-packages/pam* usr/lib64/python3*/site-packages/pam* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pam* usr/lib64/python3*/site-packages/pam* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pam -f %{oreon_filedir}/python3-pam.list

%changelog

%autochangelog
