%global source0_hash 59c6336e24626a4d4433d23e50aa28b0eb3fe384a471285cd5ebe9623570872c
Name:       dib-utils
Summary:        Pieces of diskimage-builder that are useful standalone
Version:    0.0.11
Release:        1%{?dist}
License:    Apache-2.0
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:        http://tarballs.openstack.org/dib-utils/dib-utils-%{version}.tar.gz
BuildArch: noarch
Conflicts: diskimage-builder < 0.1.15
Obsoletes: dib-utils < %{version}-%{release}
# oreon:deps
BuildRequires:  python3-d2to1
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
