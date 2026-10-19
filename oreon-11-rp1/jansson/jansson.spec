%global source0_hash dbf95cb0af903f4fb8b61507d96b45b67db7d1479688ede352e1d571394d06f7
%global forgeurl https://github.com/akheron/jansson
Version:        2.15.1
%forgemeta
Name:		jansson
Release:        1%{?dist}
Summary:        C library for encoding, decoding and manipulating JSON data
License:	MIT AND LicenseRef-Fedora-Public-Domain
URL:		%{forgeurl}
Source0:        https://github.com/akheron/jansson/archive/refs/tags/v2.15.1.tar.gz#/jansson-2.15.1.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-sphinx
# /oreon:deps
%description
Small library for parsing and writing JSON documents.

%package devel
Summary: Header files for jansson
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for developing applications making use of jansson.

%package devel-doc
Summary: Development documentation for jansson
BuildArch: noarch
%description devel-doc
Development documentation for jansson.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgeautosetup -p1

%build

autoreconf -f -i -v
%configure --disable-static
%make_build
make html
%check

make check
%install
%make_install
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jansson-devel -f %{oreon_filedir}/jansson-devel.list
%files -n jansson-devel-doc -f %{oreon_filedir}/jansson-devel-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14-4
- Prepare for Oreon 11 (RP1)
