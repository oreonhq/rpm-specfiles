%global source0_hash 74a2b6e8cb4a0304e95b995496ea3ac644c29371649b892b856e22f12a0bdeed
Name:           libmtp
Version:        1.1.23
Release:        1%{?dist}
Summary:        Software library for MTP media players
URL:            http://libmtp.sourceforge.net/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND FSFULLR AND LicenseRef-Fedora-UltraPermissive
Recommends:     udev
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libusb-1.0)
# /oreon:deps
%description
This package provides a software library for communicating with MTP
(Media Transfer Protocol) media players, typically audio players, video
players etc.

%package examples
Summary:        Example programs for libmtp
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
This package provides example programs for communicating with MTP
devices.

%package devel
Summary:        Development files for libmtp
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development files for the libmtp
library for MTP media players.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export ACLOCAL_PATH=/usr/share/gettext/m4/
yes "" | ./autogen.sh
%configure --disable-static \
           --with-udev-rules=69-libmtp.rules \
            %{nil}
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libmtp.la
rm -f $RPM_BUILD_ROOT%{_bindir}/mtp-delfile
rm -f $RPM_BUILD_ROOT%{_bindir}/mtp-getfile
rm -f $RPM_BUILD_ROOT%{_bindir}/mtp-newfolder
rm -f $RPM_BUILD_ROOT%{_bindir}/mtp-sendfile
rm -f $RPM_BUILD_ROOT%{_bindir}/mtp-sendtr
pushd $RPM_BUILD_ROOT%{_bindir}
ln -sf mtp-connect mtp-delfile
ln -sf mtp-connect mtp-getfile
ln -sf mtp-connect mtp-newfolder
ln -sf mtp-connect mtp-sendfile
ln -sf mtp-connect mtp-sendtr
popd
mkdir -p $RPM_BUILD_ROOT/usr/lib
if [ -d $RPM_BUILD_ROOT/usr/lib64/udev ] ; then \
	mv $RPM_BUILD_ROOT/usr/lib64/udev $RPM_BUILD_ROOT/usr/lib/ ; \
fi
iconv -f iso-8859-1 -t utf-8 -o COPYING.utf8 COPYING
touch -r COPYING COPYING.utf8; mv -f COPYING.utf8 COPYING
mkdir -p -m 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -p -m 644 AUTHORS README TODO \
      $RPM_BUILD_ROOT%{_pkgdocdir}
if [ $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html != $RPM_BUILD_ROOT%{_pkgdocdir}/html ] ; then \
	mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html \
		$RPM_BUILD_ROOT%{_pkgdocdir} ; \
fi
touch -r configure.ac \
      $RPM_BUILD_ROOT%{_includedir}/*.h \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
chrpath --delete $RPM_BUILD_ROOT{%{_bindir},/usr/lib/udev}/mtp*
%ldconfig_scriptlets
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmtp-examples -f %{oreon_filedir}/libmtp-examples.list
%files -n libmtp-devel -f %{oreon_filedir}/libmtp-devel.list

%changelog

%autochangelog
