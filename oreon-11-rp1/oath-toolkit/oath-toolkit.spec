%global source1_hash b775216920c4a6eab58da5a98ff6e61cfe4caca93064e6160a4cd787513b7869
%global source0_hash 8b1da365759f1249be57a82aec6e107f7b57dc77d813f96dc0aaf81624f28971
Name:          oath-toolkit
Version:       2.6.14
Release:        2%{?dist}
License:       GPL-3.0-or-later
Summary:        One-time password components
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:       https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source2:       keyring.asc
URL:           https://www.nongnu.org/oath-toolkit/
Patch:        oath-toolkit-2.6.14-lockfile.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnupg2
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
# /oreon:deps
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
License:  GPL-3.0-or-later
Provides: bundled(gnulib)
%description -n oathtool
A command line tool for generating and validating OTPs.

%package -n pskctool
Summary:  A command line tool for manipulating PSKC data
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
for d in liboath libpskc pam_oath
do
  sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $d/libtool
  sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $d/libtool
  sed -i 's| -shared | -Wl,--as-needed\0|g' $d/libtool
done
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{a,la}
rm -f %{buildroot}%{_libdir}/security/*.la
mkdir -p -m 0600 %{buildroot}%{_sysconfdir}/liboath
%ldconfig_scriptlets -n liboath
%ldconfig_scriptlets -n libpskc
%oreon_autofiles liboath usr/*/lib*.so.*
%oreon_autofiles liboath-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles liboath-doc usr/*/lib*.so.*
%oreon_autofiles libpskc usr/*/lib*.so.*
%oreon_autofiles libpskc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libpskc-doc usr/*/lib*.so.*
%oreon_autofiles oathtool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pskctool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pam_oath usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n liboath -f %{oreon_filedir}/liboath.list
%files -n liboath-devel -f %{oreon_filedir}/liboath-devel.list
%files -n liboath-doc -f %{oreon_filedir}/liboath-doc.list
%files -n libpskc -f %{oreon_filedir}/libpskc.list
%files -n libpskc-devel -f %{oreon_filedir}/libpskc-devel.list
%files -n libpskc-doc -f %{oreon_filedir}/libpskc-doc.list
%files -n oathtool -f %{oreon_filedir}/oathtool.list
%files -n pskctool -f %{oreon_filedir}/pskctool.list
%files -n pam_oath -f %{oreon_filedir}/pam_oath.list

%changelog

%autochangelog

