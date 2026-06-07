%global source0_hash none

Summary:          Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:          2.3.8
Release:          3%{?dist}
License:          (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:              https://www.gnu.org/software/libidn/#libidn2

Source0:        https://mirrors.kernel.org/gnu/libidn/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/libidn/%{name}-%{version}.tar.gz.sig
Source2:          https://keys.openpgp.org/vks/v1/by-fingerprint/B1D2BD1375BECB784CF4F8C4D73CF638C53C06BE

BuildRequires:    gnupg2
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    gettext
BuildRequires:    libunistring-devel
BuildRequires:    texinfo
Provides:         bundled(gnulib)

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

# Clean-up examples for documentation
%make_build -C examples distclean
rm -f examples/Makefile*

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%find_lang %{name}

%check
%make_build -C tests check

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%doc AUTHORS NEWS README.md
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/%{name}.html examples
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/idn2.h
%{_mandir}/man3/idn2_*.3*
%{_datadir}/gtk-doc/

%files -n idn2
%{_bindir}/idn2
%{_mandir}/man1/idn2.1*
%{_infodir}/%{name}.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.8-3
- Prepare for Oreon 11 (RP1)
