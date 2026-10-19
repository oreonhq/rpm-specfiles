%global source0_hash 77b63fdd6cb2fb5e3d7032c5e1cde70c005f498d6096b77827efe71913196464
Name:           stomppy
Version:        9.0.0
Release:        1%{?dist}
Summary:        Python stomp client for messaging
License:        Apache-2.0
URL:            https://github.com/jasonrbriggs/stomp.py
Source0:        https://files.pythonhosted.org/packages/source/s/stomp_py/stomp_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-stomppy = %{version}-%{release}
# /oreon:deps
%description
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

%package -n python3-stomppy
Summary:        Python stomp client for messaging for python3
%description -n python3-stomppy
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

This module is for the python3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stomp_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stomppy usr/lib/python3*/site-packages/stomppy* usr/lib64/python3*/site-packages/stomppy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stomppy* usr/lib64/python3*/site-packages/stomppy* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-stomppy -f %{oreon_filedir}/python3-stomppy.list

%changelog

%autochangelog
