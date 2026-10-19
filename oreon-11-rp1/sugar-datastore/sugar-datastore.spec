%global source0_hash 6c38b10cf0e294a9c5d9d00d291aa9be9b8e85e3045dc6f71a54ab3792880bb4
Name:    sugar-datastore
Version: 0.121
Release:        1%{?dist}
Summary:        Sugar Datastore
License: GPL-2.0-or-later
URL:     http://sugarlabs.org/
Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Requires: python3-xapian
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-xapian
# /oreon:deps
%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done
%configure
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
