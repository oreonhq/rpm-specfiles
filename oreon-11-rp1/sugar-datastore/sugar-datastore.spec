%global source0_hash 6c38b10cf0e294a9c5d9d00d291aa9be9b8e85e3045dc6f71a54ab3792880bb4

Name:    sugar-datastore
Version: 0.121
Release: 11%{?dist}
Summary: Sugar Datastore
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://sugarlabs.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-xapian
# py-compile needs updating
BuildRequires: automake
Requires: python3-xapian

%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS NEWS
%{python3_sitelib}/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

%changelog
%autochangelog
