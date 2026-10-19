%global source2_hash f28314aa33159c5c82cfae3eb4f6012be2775ebf1a4fb8e5c6c10233339c0e17
%global source1_hash 620dc92f158ebe0a650c0e92214a8121b927276895dc9a1dcaa38f627fa0fcb0
%global source0_hash b88cc9163d0c652aaf39a99991d974ddba1c3a9711db8f1b5838af2a14731014
Name:           libbsd
Version:        0.12.2
Release:        7%{?dist}
Summary:        Library providing BSD-compatible functions for portability
URL:            https://libbsd.freedesktop.org/
License:        Beerware AND BSD-2-Clause AND BSD-3-Clause AND ISC AND libutil-David-Nugent AND MIT AND LicenseRef-Fedora-Public-Domain
Source0:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/4F3E74F436050C10F5696574B972BF3EA4AE57A3
Source3:        libbsd-cdefs.h
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmd-devel
BuildRequires:  make
# /oreon:deps
%description
libbsd provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package devel
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmd-devel
%description devel
Development files for the libbsd library.

%package ctor-static
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".
# See the libbsd mailing list message by Guillem Jover on Jul 14 2013:
#     http://lists.freedesktop.org/archives/libbsd/2013-July/000091.html

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

%configure
%make_build
%check

%make_build check
%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/%{name}.la
mv -f %{buildroot}%{_includedir}/bsd/sys/cdefs{,-%{__isa_bits}}.h
install -p -m 0644 %{SOURCE3} %{buildroot}%{_includedir}/bsd/sys/cdefs.h
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libbsd-devel -f %{oreon_filedir}/libbsd-devel.list
%files -n libbsd-ctor-static -f %{oreon_filedir}/libbsd-ctor-static.list

%changelog

%autochangelog

