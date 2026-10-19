%global source0_hash 0fd35a7030052acd9f58948d1d900fe1e432ee37103c5561554408bdac6bbf0d
Name:           tini
Version:        0.19.0
Release:        1%{?dist}
Summary:        A tiny but valid init for containers
License:        MIT
URL:            https://github.com/krallin/tini
Source0:        https://github.com/krallin/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?el7}
%else
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  sed
# /oreon:deps
%description
Tini is the simplest init you could think of.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit all the while reaping zombies and performing signal
forwarding.

%package        static
Summary:        Standalone static build of %{name}
%description    static
This package contains a standalone static build of %{name}, meant to be used
inside a container.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Do not strip binaries
sed -i CMakeLists.txt -e 's/ -Wl,-s//'

%build

%if 0%{?el7}
%cmake3
%cmake3_build
%else
%cmake
%cmake_build
%endif
%install
%if 0%{?el7}
%cmake3_install
%else
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n tini-static -f %{oreon_filedir}/tini-static.list

%changelog

%autochangelog
