%global source0_hash 0f063cbd36ec232032e425769ebc871f195a7d183b9af32f9901589ea7129ac3

%global srcname sysv_ipc
%global sum System V IPC for Python - Semaphores, Shared Memory and Message Queues
%global desc The sysv_ipc module which gives Python access to System V inter-process\
semaphores, shared memory and message queues on systems that support them.

Name:           python-%{srcname}
Version:        1.1.0
Release:        18%{?dist}
Summary:        %{sum}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://semanchuk.com/philip/%{srcname}/
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{desc}

%package examples
Summary:    Examples for Python sysv_ipc module

%description examples
This module comes with four demonstration apps. 

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sysv_ipc-%{version}

%build
%py3_build

%install
%py3_install
chmod -x demos/*/*.{py,sh}

%files -n python3-%{srcname}
%license LICENSE 
%doc LICENSE README ReadMe.html VERSION
%{python3_sitearch}/*
%{python3_sitearch}/%{srcname}-%{version}-*.egg-info

%files examples
%doc demos

%changelog
%autochangelog
