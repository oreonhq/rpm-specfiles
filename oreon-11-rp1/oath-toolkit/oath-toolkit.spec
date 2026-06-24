%global source0_hash none

Name:          oath-toolkit
Version:       2.6.14
Release:       2%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
Summary:       One-time password components
BuildRequires: make
BuildRequires: pam-devel
BuildRequires: gtk-doc
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gnupg2
Source0:       https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:       https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
# gpg2 --recv-keys EDA21E94B565716F
# gpg2 --armor --export D73CF638C53C06BE > keyring.asc
Source2:       keyring.asc
URL:           https://www.nongnu.org/oath-toolkit/
Patch:        oath-toolkit-2.6.14-lockfile.patch

%description
The OATH Toolkit provide components for building one-time password
authentication systems. It contains shared libraries, command line tools and a
PAM module. Supported technologies include the event-based HOTP algorithm
(RFC4226) and the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC) format
described in RFC6030 is supported.

%package -n liboath
Summary:          Library for OATH handling
License:          LGPL-2.1-or-later
# https://fedorahosted.org/fpc/ticket/174
Provides:         bundled(gnulib)

%description -n liboath
OATH stands for Open AuTHentication, which is the organization that
specify the algorithms. Supported technologies include the event-based
HOTP algorithm (RFC4226) and the time-based TOTP algorithm (RFC6238).

%package -n liboath-devel
Summary:  Development files for liboath
License:  LGPL-2.1-or-later
Requires: liboath%{?_isa} = %{version}-%{release}

%description -n liboath-devel
Development files for liboath.

%package -n liboath-doc
Summary:   Documentation files for liboath
License:   LGPL-2.1-or-later
Requires:  liboath = %{version}-%{release}
Requires:  gtk-doc
BuildArch: noarch

%description -n liboath-doc
Documentation files for liboath.

%package -n libpskc
Summary:          Library for PSKC handling
License:          LGPL-2.1-or-later
Requires:         xml-common
# https://fedorahosted.org/fpc/ticket/174
Provides:         bundled(gnulib)

%description -n libpskc
Library for managing secret key files, the Portable Symmetric Key
Container (PSKC) format described in RFC6030 is supported.

%package -n libpskc-devel
Summary:  Development files for libpskc
License:  LGPL-2.1-or-later
Requires: libpskc%{?_isa} = %{version}-%{release}

%description -n libpskc-devel
Development files for libpskc.

%package -n libpskc-doc
Summary:   Documentation files for libpskc
License:   LGPL-2.1-or-later
Requires:  libpskc = %{version}-%{release}
Requires:  gtk-doc
BuildArch: noarch

%description -n libpskc-doc
Documentation files for libpskc.

%package -n oathtool
Summary:  A command line tool for generating and validating OTPs
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later
# https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)

%description -n oathtool
A command line tool for generating and validating OTPs.

%package -n pskctool
Summary:  A command line tool for manipulating PSKC data
# https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)
Requires: xmlsec1-openssl%{?_isa}

%description -n pskctool
A command line tool for manipulating PSKC data.

%package -n pam_oath
Summary:  A PAM module for pluggable login authentication for OATH
Requires: pam

%description -n pam_oath
A PAM module for pluggable login authentication for OATH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -fi
%configure --with-pam-dir=%{_libdir}/security

# Kill rpaths and link with --as-needed
for d in liboath libpskc pam_oath
do
  sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $d/libtool
  sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $d/libtool
  sed -i 's| -shared | -Wl,--as-needed\0|g' $d/libtool
done

%make_build

%install
%make_install

# Remove static objects and libtool files
rm -f %{buildroot}%{_libdir}/*.{a,la}
rm -f %{buildroot}%{_libdir}/security/*.la

# Make /etc/liboath directory
mkdir -p -m 0600 %{buildroot}%{_sysconfdir}/liboath

%ldconfig_scriptlets -n liboath

%ldconfig_scriptlets -n libpskc

%files -n liboath
%doc COPYING
%attr(0600, root, root) %dir %{_sysconfdir}/liboath
%{_libdir}/liboath.so.*

%files -n liboath-devel
%{_includedir}/liboath
%{_libdir}/liboath.so
%{_libdir}/pkgconfig/liboath.pc

%files -n liboath-doc
%{_mandir}/man3/oath*
%{_datadir}/gtk-doc/html/liboath/*

%files -n libpskc
%doc libpskc/README
%{_libdir}/libpskc.so.*
%{_datadir}/xml/pskc

%files -n libpskc-devel
%{_includedir}/pskc
%{_libdir}/libpskc.so
%{_libdir}/pkgconfig/libpskc.pc

%files -n libpskc-doc
%{_mandir}/man3/pskc*
%{_datadir}/gtk-doc/html/libpskc/*

%files -n oathtool
%doc COPYING
%{_bindir}/oathtool
%{_mandir}/man1/oathtool.*

%files -n pskctool
%{_bindir}/pskctool
%{_mandir}/man1/pskctool.*

%files -n pam_oath
%doc pam_oath/README COPYING
%{_libdir}/security/pam_oath.so

%changelog
%autochangelog

