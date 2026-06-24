%global source0_hash none

Name:           libbsd
Version:        0.12.2
Release:        7%{?dist}
Summary:        Library providing BSD-compatible functions for portability
URL:            https://libbsd.freedesktop.org/
# Breakdown in COPYING file of libbsd release tarball, see also:
# - https://gitlab.com/fedora/legal/fedora-license-data/-/issues/71
# - https://gitlab.com/fedora/legal/fedora-license-data/-/issues/73
License:        Beerware AND BSD-2-Clause AND BSD-3-Clause AND ISC AND libutil-David-Nugent AND MIT AND LicenseRef-Fedora-Public-Domain

Source0:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/4F3E74F436050C10F5696574B972BF3EA4AE57A3
Source3:        libbsd-cdefs.h

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmd-devel
BuildRequires:  make

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

# don't want static library or libtool archive
rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/%{name}.la

# avoid file conflicts in multilib installations of -devel subpackage
mv -f %{buildroot}%{_includedir}/bsd/sys/cdefs{,-%{__isa_bits}}.h
install -p -m 0644 %{SOURCE3} %{buildroot}%{_includedir}/bsd/sys/cdefs.h

%ldconfig_scriptlets

%files
%license COPYING
%doc README ChangeLog
%{_libdir}/%{name}.so.0*

%files devel
%{_mandir}/man3/*.3bsd.*
%{_mandir}/man7/%{name}.7.*
%{_includedir}/bsd
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-overlay.pc

%files ctor-static
%{_libdir}/%{name}-ctor.a
%{_libdir}/pkgconfig/%{name}-ctor.pc

%changelog
%autochangelog

