%global source0_hash ef84b6ba3b5ece72da5f0f33b7a6719bf3b13c7e24fdb92ce8161a3ae11eee31
Summary:        In memory VT-compatible terminal emulator
Name:           python-pyte
Version:        0.8.2
Release:        1%{?dist}
License:        LGPL-3.0-only
URL:            https://github.com/selectel/pyte
Source0:        https://github.com/selectel/pyte/archive/%{version}/pyte-%{version}.tar.gz
Patch0:         python-pyte-0.8.0-docs.patch
Patch1:         %{url}/pull/177.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyte = %{version}-%{release}
# /oreon:deps
%description
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.

%package     -n python3-pyte
Summary:        In memory VT-compatible terminal emulator
%description -n python3-pyte
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.

%package     -n python3-pyte-docs
Summary:        Documentation of API in Python module pyte
%description -n python3-pyte-docs
This contains documentation of the API in Python module pyte.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyte-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs && make all
%install
%pyproject_install
%oreon_autofiles python3-pyte usr/lib/python3*/site-packages/pyte* usr/lib64/python3*/site-packages/pyte* usr/bin/*
%oreon_autofiles python3-pyte-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyte* usr/lib64/python3*/site-packages/pyte* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{pytest} --color=yes
%files
%files -n python3-pyte -f %{oreon_filedir}/python3-pyte.list
%files -n python3-pyte-docs -f %{oreon_filedir}/python3-pyte-docs.list

%changelog

%autochangelog
