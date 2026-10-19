%global source0_hash 8cf3898b945c2f44eeb52ffce57b91104e89752f7b01345c975fdfbbaa7c38c6
Name:           python-fastrlock
Version:        0.8.3
Release:        1%{?dist}
Summary:        Fast, re-entrant optimistic lock implemented in Cython
License:        MIT
URL:            https://github.com/scoder/fastrlock
Source0:        https://github.com/scoder/fastrlock/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastrlock = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastrlock
Summary:        Fast, re-entrant optimistic lock implemented in Cython
%description -n python3-fastrlock

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n fastrlock-%{version}

# So we do not have to keep up with a license for something we don't use.
rm appveyor_env.cmd

# Adjust cython's upper bound limit
sed -i -e 's@Cython>=3.0.11, <3.1@Cython>=3.0.11, <3.3@' requirements.txt
grep Cython requirements.txt

%build

%pyproject_wheel -C=--global-option=--with-cython
%install
%pyproject_install
%oreon_autofiles python3-fastrlock usr/lib/python3*/site-packages/fastrlock* usr/lib64/python3*/site-packages/fastrlock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastrlock* usr/lib64/python3*/site-packages/fastrlock* usr/bin/*

%check

%pyproject_check_import
mv fastrlock fastrlock_
%pytest
%files
%files -n python3-fastrlock -f %{oreon_filedir}/python3-fastrlock.list

%changelog

%autochangelog
