%global source0_hash ac6397369f128212c43064a2b4878038dab78dab41875364554aaf2a684e6979
Name:      python-pbkdf2
Version:   1.3
Release:        39%{?dist}
Summary:        A module for a password-based key derivation function
License:   MIT
URL:       https://www.dlitz.net/software/python-pbkdf2/
Source0:        https://files.pythonhosted.org/packages/source/p/pbkdf2/pbkdf2-%{version}.tar.gz
Patch1:    pbkdf2-license.patch
Patch2:    pbkdf2-remove-shebang.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pbkdf2 = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pbkdf2
Summary:        A module for a password-based key derivation function
%description -n python3-pbkdf2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pbkdf2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pbkdf2 usr/lib/python3*/site-packages/pbkdf2* usr/lib64/python3*/site-packages/pbkdf2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pbkdf2* usr/lib64/python3*/site-packages/pbkdf2* usr/bin/*

%check

%pyproject_check_import
%{python3} -m unittest test/*
%files
%files -n python3-pbkdf2 -f %{oreon_filedir}/python3-pbkdf2.list

%changelog

%autochangelog
