%global source0_hash 9990639e19a9c8f1db4af453b7e6a45ef2995ec03e13bac35b9824839fd46867
%global sum Simple packet creation/parsing library
Name:           python-dpkt
Version:        1.9.8
Release:        1%{?dist}
Summary:        Simple packet creation/parsing library
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kbandla/dpkt
Source0:        https://github.com/kbandla/dpkt/archive/v%{version}.tar.gz
Patch0:         nostdeb-1.8.8.patch
Patch1:         python3-fixes-1.8.8.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dpkt = %{version}-%{release}
# /oreon:deps
%description
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%package -n python3-dpkt
Summary:        %{sum}
%description -n python3-dpkt
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dpkt-%{version}
#%patch0 -p1
#%patch1 -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dpkt usr/lib/python3*/site-packages/dpkt* usr/lib64/python3*/site-packages/dpkt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dpkt* usr/lib64/python3*/site-packages/dpkt* usr/bin/*

%check

%pyproject_check_import
%ifarch s390x
%{__python3} -m pytest dpkt -k "not test_deprecated_decorator"
%endif
%files
%files -n python3-dpkt -f %{oreon_filedir}/python3-dpkt.list

%changelog

%autochangelog
