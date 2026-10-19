%global source0_hash b5f60fb47bbf5d8d762f134bcea0c388eba6b498342a682a21f1686545094b77
%bcond_without tests
Name:           python-dkimpy
Version:        1.1.8
Release:        1%{?dist}
Summary:        DKIM, ARC, and TLSRPT email signing and verification
License:        Zlib
URL:            https://launchpad.net/dkimpy
Source0:        https://files.pythonhosted.org/packages/source/d/dkimpy/dkimpy-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dkimpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dkimpy
Summary:        DKIM, ARC, and TLSRPT email signing and verification
%description -n python3-dkimpy

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dkimpy-%{version}

# Drop shebang for these files, as we don't need them
sed -e "s|^#!/usr/bin/.*python$||" -i dkim/{arcsign.py,arcverify.py,dkimsign.py,dkimverify.py,dknewkey.py}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dkimpy usr/lib/python3*/site-packages/dkimpy* usr/lib64/python3*/site-packages/dkimpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dkimpy* usr/lib64/python3*/site-packages/dkimpy* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%{py3_test_envvars} %{python3} -m unittest -v
%endif
%files
%files -n python3-dkimpy -f %{oreon_filedir}/python3-dkimpy.list

%changelog

%autochangelog
