%global source0_hash none

%undefine __cmake_in_source_build
%global with_lua 1
%global with_maxminddb 1
%global with_pytools 1
%global plugins_version 4.6

%bcond http3 %[0%{?fedora} >= 43]

Summary:	Network traffic analyzer
Name:		wireshark
Version:	4.6.4
Release:	2%{?dist}
Epoch:		1
License:	BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND MIT AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Zlib AND ISC AND (BSD-3-Clause OR GPL-2.0-only) AND (GPL-2.0-or-later AND Zlib)
Url:		http://www.wireshark.org/

Source0:        https://www.wireshark.org/download/src/all-versions/%{name}-%{version}.tar.xz
Source1:        https://www.wireshark.org/download/src/all-versions/SIGNATURES-%{version}.txt
Source2:	90-wireshark-usbmon.rules
Source3:	wireshark.sysusers

# Fedora-specific
Patch2:   wireshark-0002-Customize-permission-denied-error.patch
# Fedora-specific
Patch4:   wireshark-0004-Restore-Fedora-specific-groups.patch
# Fedora-specific
Patch5:   wireshark-0005-Fix-paths-in-a-wireshark.desktop-file.patch
# Fedora-specific
Patch6:   wireshark-0006-Move-tmp-to-var-tmp.patch
Patch7:   wireshark-0007-cmakelists.patch
Patch8:   wireshark-0008-pkgconfig.patch
Patch9:   wireshark-0009-remove-strato-manpages.patch

#install tshark together with wireshark GUI
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}

Requires:	xdg-utils
Requires:	hicolor-icon-theme

%if %{with_maxminddb} && 0%{?fedora} || (0%{?oreon} >= 11)
Requires:	libmaxminddb
%endif

BuildRequires:	bzip2-devel
BuildRequires:	c-ares-devel
BuildRequires:	elfutils-devel
BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	gnutls-devel
BuildRequires:	krb5-devel
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libnl3-devel
BuildRequires:	libpcap-devel >= 0.9
BuildRequires:	libselinux-devel
BuildRequires:	libsmi-devel
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	xdg-utils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	perl(Pod::Html)
BuildRequires:	perl(Pod::Man)
BuildRequires:	perl(open)
BuildRequires:	pcre2-devel
Buildrequires:	libssh-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-linguist
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qt5compat-devel
BuildRequires:	qt6-qtmultimedia-devel
BuildRequires:	qt6-qtsvg-devel
BuildRequires:  qt6-qtimageformats
BuildRequires:	zlib-devel
BuildRequires:	asciidoctor
%if %{with_maxminddb} && 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires:	libmaxminddb-devel
%endif
%if %{with_lua} && 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires:	lua-devel
%endif
Buildrequires:	git-core
Buildrequires:	python3-devel
Buildrequires:	cmake
Buildrequires:	speexdsp-devel
#needed for sdjournal external capture interface
BuildRequires:	systemd-devel
BuildRequires:	libnghttp2-devel
%if %{with http3}
BuildRequires:	libnghttp3-devel
%endif
BuildRequires:	systemd-rpm-macros
BuildRequires:	lz4-devel
BuildRequires:	snappy-devel
BuildRequires:	brotli-devel
BuildRequires:	opus-devel
BuildRequires:	sbc-devel
%if 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires:	ilbc-devel
BuildRequires:	opencore-amr-devel
# bcg729 for G.729
BuildRequires:	bcg729-devel
# spandsp for G.722 and G.726
BuildRequires:	spandsp-devel
# wireshark needs the -compat package
%endif


%description
Wireshark allows you to examine protocol data stored in files or as it is
captured from wired or wireless (WiFi or Bluetooth) networks, USB devices,
and many other sources.  It supports dozens of protocol capture file formats
and understands more than a thousand protocols.

It has many powerful features including a rich display filter language
and the ability to reassemble multiple protocol packets in order to, for
example, view a complete TCP stream, save the contents of a file which was
transferred over HTTP or CIFS, or play back an RTP audio stream.

%package	cli
Summary:	Network traffic analyzer

%description cli
This package contains command-line utilities, plugins, and documentation for
Wireshark.

%package devel
Summary:	Development headers and libraries for wireshark
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Requires:	glib2-devel
%if %{with_pytools} && 0%{?fedora} || (0%{?oreon} >= 11)
Requires: python3-ply
Requires: omniORB-devel
%endif

%description devel
The wireshark-devel package contains the header files, developer
documentation, and libraries required for development of wireshark scripts
and plugins.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git

%build
%cmake -G "Unix Makefiles" \
  -DDISABLE_WERROR=ON \
  -DBUILD_wireshark=ON \
%if %{with_lua} && 0%{?fedora} || (0%{?oreon} >= 11)
  -DENABLE_LUA=ON \
%else
  -DENABLE_LUA=OFF \
%endif
%if %{with_maxminddb} && 0%{?fedora} || (0%{?oreon} >= 11) 
  -DBUILD_mmdbresolve=ON \
%else
  -DBUILD_mmdbresolve=OFF \
%endif
  -DBUILD_randpktdump=OFF \
  -DBUILD_androiddump=ON \
  -DENABLE_SMI=ON \
  -DUSE_qt6=ON \
  -DENABLE_PLUGINS=ON \
  -DENABLE_NETLINK=ON \
  -DBUILD_dcerpcidl2wrs=OFF \
  -DBUILD_sdjournal=ON \
  -DBUILD_stratoshark=OFF

%cmake_build

%install
%cmake_install
%cmake_install --component Development

desktop-file-validate %{buildroot}%{_datadir}/applications/org.wireshark.Wireshark.desktop

#install devel files (inspired by debian/wireshark-dev.header-files)
install -d -m 0755  %{buildroot}%{_includedir}/wireshark
install -m 0644 %{__cmake_builddir}/config.h %{buildroot}%{_includedir}/wireshark/config.h
IDIR="%{buildroot}%{_includedir}/wireshark"
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 %{SOURCE2}		%{buildroot}%{_udevrulesdir}
install -Dpm 0644 %{SOURCE3}		%{buildroot}%{_sysusersdir}/%{name}.conf

%if %{with_pytools} && 0%{?fedora} || (0%{?oreon} >= 11)
#install asn2wrs.py, idl2wrs and make-plugin-reg.py tools
mkdir -p %{buildroot}%{_libexecdir}/wireshark/pytools
install -m 0755 tools/asn2wrs.py %{buildroot}%{_libexecdir}/wireshark/pytools/
install -m 0755 tools/make-plugin-reg.py %{buildroot}%{_libexecdir}/wireshark/pytools/
install -m 0755 tools/idl2wrs %{buildroot}%{_libexecdir}/wireshark/pytools/

#install idl2wrs dependent scripts
install -m 0644 tools/wireshark_be.py %{buildroot}%{_libexecdir}/wireshark/pytools/
install -m 0644 tools/wireshark_gen.py %{buildroot}%{_libexecdir}/wireshark/pytools/
%endif

touch %{buildroot}%{_bindir}/%{name}

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete


%post cli
%{?ldconfig}
# skip triggering if udevd isn't even accessible, e.g. containers or
# rpm-ostree-based systems
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=usbmon || :
fi

%ldconfig_postun cli

%files
%{_datadir}/applications/org.wireshark.Wireshark.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_bindir}/wireshark
%{_mandir}/man1/wireshark.*

%files cli
%license COPYING
%doc AUTHORS INSTALL README*
%{_bindir}/capinfos
%{_bindir}/captype
%{_bindir}/editcap
%{_bindir}/dftest
%{_bindir}/mergecap
%{_bindir}/randpkt
%{_bindir}/reordercap
%{_bindir}/sharkd
%{_bindir}/text2pcap
%{_bindir}/tshark
%if %{with_maxminddb} && 0%{?fedora} || (0%{?oreon} >= 11)
%{_bindir}/mmdbresolve
%endif
%attr(0750, root, wireshark) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/dumpcap
%{_bindir}/rawshark
%{_udevrulesdir}/90-wireshark-usbmon.rules
%{_libdir}/lib*.so.*
%dir %{_libexecdir}/wireshark
%dir %{_libexecdir}/wireshark/extcap
%dir %{_libdir}/wireshark/plugins
%dir %{_libdir}/wireshark
%{_libexecdir}/wireshark/extcap/ciscodump
%{_libexecdir}/wireshark/extcap/udpdump
%{_libexecdir}/wireshark/extcap/wifidump
%{_libexecdir}/wireshark/extcap/sshdump
%{_libexecdir}/wireshark/extcap/sdjournal
%{_libexecdir}/wireshark/extcap/dpauxmon
%{_libexecdir}/wireshark/extcap/androiddump
#the version wireshark uses to store plugins is only x.y, not .z
%dir %{_libdir}/wireshark/plugins/%{plugins_version}
%dir %{_libdir}/wireshark/plugins/%{plugins_version}/epan
%dir %{_libdir}/wireshark/plugins/%{plugins_version}/wiretap
%dir %{_libdir}/wireshark/plugins/%{plugins_version}/codecs
%{_libdir}/wireshark/plugins/%{plugins_version}/epan/*.so
%{_libdir}/wireshark/plugins/%{plugins_version}/wiretap/*.so
%{_libdir}/wireshark/plugins/%{plugins_version}/codecs/*.so
%{_mandir}/man1/editcap.*
%{_mandir}/man1/tshark.*
%{_mandir}/man1/mergecap.*
%{_mandir}/man1/text2pcap.*
%{_mandir}/man1/capinfos.*
%{_mandir}/man1/dumpcap.*
%{_mandir}/man4/wireshark-filter.*
%{_mandir}/man1/rawshark.*
%{_mandir}/man1/randpkt.*
%{_mandir}/man1/reordercap.*
%{_mandir}/man1/sshdump.*
%{_mandir}/man1/udpdump.*
%{_mandir}/man1/wifidump.*
%{_mandir}/man1/androiddump.*
%{_mandir}/man1/captype.*
%{_mandir}/man1/ciscodump.*
%{_mandir}/man1/randpktdump.*
%{_mandir}/man1/dpauxmon.*
%{_mandir}/man1/sdjournal.*
%{_mandir}/man1/etwdump.*
%{_mandir}/man4/extcap.*
%{_datadir}/doc/wireshark/*

%if %{with_maxminddb} && 0%{?fedora} || (0%{?oreon} >= 11)
%{_mandir}/man1/mmdbresolve.*
%endif
%dir %{_datadir}/wireshark
%{_datadir}/wireshark/*
%{_sysusersdir}/%{name}.conf

%files devel
%doc doc/README.* ChangeLog
%dir %{_includedir}/wireshark
%{_includedir}/wireshark/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake
%if %{with_pytools} && 0%{?fedora} || (0%{?oreon} >= 11)
%dir %{_libexecdir}/wireshark/pytools
%{_libexecdir}/wireshark/pytools/*.py
%{_libexecdir}/wireshark/pytools/idl2wrs
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:4.6.4-2
- Import
