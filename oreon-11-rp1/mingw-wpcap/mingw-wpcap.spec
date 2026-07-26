%global source0_hash 346a93f6b375ac4c1add5c8c7178498f1feed4172fb33383474a91b48ec6633a

%{?mingw_package_header}

%global versionmajor 4
%global versionminor 1
%global versionsuffix 3

%global wpcapexamples %{_docdir}/%{name}/examples
%global wpcapdoc %{_docdir}/%{name}

Name:           mingw-wpcap
Version:        %{versionmajor}.%{versionminor}.final%{versionsuffix}
Release:        25%{?dist}
Summary:        MinGW user-level packet capture

# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            http://www.winpcap.org/
Source0:        http://www.winpcap.org/install/bin/WpcapSrc_%{versionmajor}_%{versionminor}_%{versionsuffix}.zip
Source1:        wpcap.pc
Source2:        wpcap64.pc
Patch0:         wpcap.patch
Patch1:         wpcap-w2k.patch
Patch2:         winpcap-mingw-w64-compatibility.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  doxygen
BuildRequires:  unzip
BuildRequires:  dos2unix
BuildRequires:  bison
BuildRequires:  flex

%description
MinGW Windows pcap library.

%package -n mingw32-wpcap
Summary:        MinGW user-level packet capture

%description -n mingw32-wpcap
MinGW Windows pcap library.

%package -n mingw32-wpcap-examples
Summary:        Example source code for MinGW pcap
Requires:       mingw32-wpcap = %{version}

%description -n mingw32-wpcap-examples
This package contains examples on the usage of the Windows pcap
library.

%package -n mingw32-wpcap-docs
Summary:        MinGW pcap documentation
Requires:       mingw32-wpcap = %{version}

%description -n mingw32-wpcap-docs
This package contains the Windows pcap library documentation.

%package -n mingw64-wpcap
Summary:        MinGW user-level packet capture

%description -n mingw64-wpcap
MinGW Windows pcap library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n winpcap

%patch -P0 -p0 -b .build
%patch -P2 -p0 -b .mingw-w64

find . -type f -print0 |xargs -0 dos2unix || true
pushd wpcap/libpcap/Win32/Include/
mv ip6_misc.h IP6_misc.h
popd

%patch -P1 -p0 -b .w2k

find . -name GNUmakefile |xargs perl -i -pe 's,-mno-cygwin,,'

# Prevent a conflict between getaddrinfo.c and ws2_32
sed -i s@../libpcap/Win32/Src/getaddrinfo.o@@ wpcap/PRJ/GNUmakefile

mkdir build64
cp -r packetNtx wpcap Common build64

%build
pushd packetNtx/Dll/Project
make -f GNUmakefile CC=i686-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd wpcap/PRJ
make -f GNUmakefile CC=i686-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd build64/packetNtx/Dll/Project
make -f GNUmakefile CC=x86_64-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd build64/wpcap/PRJ
make -f GNUmakefile CC=x86_64-w64-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd

pushd dox/prj
doxygen winpcap_noc.dox
popd

%install
# mingw32
install -d $RPM_BUILD_ROOT/%{mingw32_bindir}
install -d $RPM_BUILD_ROOT/%{mingw32_libdir}/pkgconfig
install -m0644 %{SOURCE1} $RPM_BUILD_ROOT/%{mingw32_libdir}/pkgconfig
install -m0644 packetNtx/Dll/Project/libpacket.a $RPM_BUILD_ROOT/%{mingw32_libdir}/libpacket.dll.a
install -m0644 packetNtx/Dll/Project/Packet.dll $RPM_BUILD_ROOT/%{mingw32_bindir}/packet.dll
install -m0644 wpcap/lib/libwpcap.a $RPM_BUILD_ROOT/%{mingw32_libdir}/libwpcap.dll.a
install -m0644 wpcap/PRJ/wpcap.dll $RPM_BUILD_ROOT/%{mingw32_bindir}
install -m0644 packetNtx/Dll/Packet.def $RPM_BUILD_ROOT/%{mingw32_libdir}/packet.def
install -m0644 wpcap/PRJ/WPCAP.DEF $RPM_BUILD_ROOT/%{mingw32_libdir}/wpcap.def
install -d $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap/*.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-int.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-bpf.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-namedb.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/remote-ext.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-stdinc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/Win32-Extensions/Win32-Extensions.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/bittypes.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/IP6_misc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/Gnuc.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
install -m0644 Common/Packet32.h $RPM_BUILD_ROOT/%{mingw32_includedir}/wpcap/
# mingw64
install -d $RPM_BUILD_ROOT/%{mingw64_bindir}
install -d $RPM_BUILD_ROOT/%{mingw64_libdir}/pkgconfig
install -m0644 %{SOURCE2} $RPM_BUILD_ROOT/%{mingw64_libdir}/pkgconfig/wpcap.pc
install -m0644 build64/packetNtx/Dll/Project/libpacket.a $RPM_BUILD_ROOT/%{mingw64_libdir}/libpacket.dll.a
install -m0644 build64/packetNtx/Dll/Project/Packet.dll $RPM_BUILD_ROOT/%{mingw64_bindir}/packet.dll
install -m0644 build64/wpcap/lib/libwpcap.a $RPM_BUILD_ROOT/%{mingw64_libdir}/libwpcap.dll.a
install -m0644 build64/wpcap/PRJ/wpcap.dll $RPM_BUILD_ROOT/%{mingw64_bindir}
install -m0644 build64/packetNtx/Dll/Packet.def $RPM_BUILD_ROOT/%{mingw64_libdir}/packet.def
install -m0644 build64/wpcap/PRJ/WPCAP.DEF $RPM_BUILD_ROOT/%{mingw64_libdir}/wpcap.def
install -d $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/pcap
install -m0644 build64/wpcap/libpcap/pcap/*.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/pcap
install -m0644 build64/wpcap/libpcap/pcap.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-int.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-bpf.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-namedb.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/remote-ext.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/pcap-stdinc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/Win32-Extensions/Win32-Extensions.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/bittypes.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/IP6_misc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/wpcap/libpcap/Win32/Include/Gnuc.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
install -m0644 build64/Common/Packet32.h $RPM_BUILD_ROOT/%{mingw64_includedir}/wpcap/
# doc
install -d $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/WinPcap_docs.html $RPM_BUILD_ROOT/%{wpcapdoc}/
install -m0644 dox/prj/docs/* $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/pics/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
# examples
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
cp -r Examples $RPM_BUILD_ROOT/%{wpcapexamples}/remote
cp -r Examples-pcap $RPM_BUILD_ROOT/%{wpcapexamples}/pcap
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/NetMeter
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/kdump
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/winpcap_stress
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/stats

%files -n mingw32-wpcap
%doc wpcap/libpcap/LICENSE
%{mingw32_libdir}/pkgconfig/wpcap.pc
%{mingw32_bindir}/packet.dll
%{mingw32_bindir}/wpcap.dll
%{mingw32_libdir}/libpacket.dll.a
%{mingw32_libdir}/libwpcap.dll.a
%{mingw32_libdir}/packet.def
%{mingw32_libdir}/wpcap.def
%{mingw32_includedir}/wpcap

%files -n mingw32-wpcap-docs
%{wpcapdoc}/WinPcap_docs.html
%{wpcapdoc}/html

%files -n mingw32-wpcap-examples
%{wpcapexamples}

%files -n mingw64-wpcap
%doc build64/wpcap/libpcap/LICENSE
%{mingw64_libdir}/pkgconfig/wpcap.pc
%{mingw64_bindir}/packet.dll
%{mingw64_bindir}/wpcap.dll
%{mingw64_libdir}/libpacket.dll.a
%{mingw64_libdir}/libwpcap.dll.a
%{mingw64_libdir}/packet.def
%{mingw64_libdir}/wpcap.def
%{mingw64_includedir}/wpcap

%changelog
%autochangelog
