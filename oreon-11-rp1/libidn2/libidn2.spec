%global source2_hash 6f6066b8f06ce8d65fe65da94a853cbd79e16e45d91b3111b067c6899f028e12
%global source1_hash 268ad6787ed902fba2154bcd64347269af6c4298bdeed8d7db59df7b65fd31f2
%global source0_hash f557911bf6171621e1f72ff35f5b1825bb35b52ed45325dcdee931e5d3c0787a
Summary:        Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:          2.3.8
Release:        3%{?dist}
License:          (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:              https://www.gnu.org/software/libidn/#libidn2
Source0:        https://mirrors.kernel.org/gnu/libidn/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/libidn/%{name}-%{version}.tar.gz.sig
Source2:          https://keys.openpgp.org/vks/v1/by-fingerprint/B1D2BD1375BECB784CF4F8C4D73CF638C53C06BE
Provides:         bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package devel
Summary:          Development files for libidn2
Requires:         %{name}%{?_isa} = %{version}-%{release}, pkgconfig
%description devel
The libidn2-devel package contains libraries and header files for
developing applications that use libidn2.

%package -n idn2
Summary:          IDNA2008 internationalized domain names conversion tool
License:          GPL-3.0-or-later
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description -n idn2
The idn2 package contains the idn2 command line tool for testing
IDNA2008 conversions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%configure --disable-static
%make_build
%make_build -C doc html
%install
%make_install
%make_build -C examples distclean
rm -f examples/Makefile*
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir
%find_lang %{name}
%oreon_autofiles idn2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build -C tests check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libidn2-devel -f %{oreon_filedir}/libidn2-devel.list
%files -n idn2 -f %{oreon_filedir}/idn2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.8-3
- Prepare for Oreon 11 (RP1)
