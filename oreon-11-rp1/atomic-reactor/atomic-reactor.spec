%global source0_hash 2ee135565c7e828db4c1544b275da347d67a509168277c1892f23e0f093f4c58
%global owner projectatomic
%global project atomic-reactor
%global dock_obsolete_vr 1.3.7-2
Name:           %{project}
Version:        4.22.1
Release:        1%{?dist}
Summary:        Improved builder for Docker images
License:        BSD-2-Clause
URL:            https://github.com/%{owner}/%{project}
Source0:        https://github.com/containerbuildsystem/atomic-reactor/archive/refs/tags/%{version}.tar.gz
Patch0:         atomic-reactor-rpmqa-dbpath.patch
BuildArch:      noarch
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       git >= 1.7.10
%if 0%{?with_check}
%endif
Provides:       dock = %{version}-%{release}
Obsoletes:      dock < %{dock_obsolete_vr}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-atomic-reactor = %{version}-%{release}
# /oreon:deps
%description
Simple Python tool with command line interface for building Docker
images. It contains a lot of helpful functions which you would
probably implement if you started hooking Docker into your
infrastructure.

%package -n python3-atomic-reactor
Summary:        Python 3 Atomic Reactor library
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-reflink
Requires:       python3-setuptools
Requires:       python3-dockerfile-parse >= 0.0.5
Requires:       python3-docker-squash >= 1.0.0-0.3
Requires:       python3-jsonschema
Requires:       python3-PyYAML
Provides:       python3-dock = %{version}-%{release}
Obsoletes:      python3-dock < %{dock_obsolete_vr}
%{?python_provide:%python_provide python3-atomic-reactor}
%description -n python3-atomic-reactor
Simple Python 3 library for building Docker images. It contains
a lot of helpful functions which you would probably implement if
you started hooking Docker into your infrastructure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n %{name}-%{version}
%setup -q
%patch -P0 -p1

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a docs/manpage/atomic-reactor.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles python3-atomic-reactor usr/lib/python3*/site-packages/atomic_reactor* usr/lib64/python3*/site-packages/atomic_reactor* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/atomic_reactor* usr/lib64/python3*/site-packages/atomic_reactor* usr/bin/*
%if 0%{?with_check}
%check

%{__python3} -m pytest -vv tests
%endif
%files
%files -n python3-atomic-reactor -f %{oreon_filedir}/python3-atomic-reactor.list

%changelog

%autochangelog
