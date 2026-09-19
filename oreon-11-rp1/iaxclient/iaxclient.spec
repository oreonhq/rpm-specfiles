%global source0_hash 6ca6ce8103837ed6fa2fd2e88c1c0d3a3d93d7b4bd084878351527ebfb205149

%global betaver beta3
%global tclver 0.2
%global mainver 2.1
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8.6)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global tkphonearch %{_arch}

Name:		iaxclient
Version:	%{mainver}
Release:	0.54.%{betaver}%{?dist}
Summary:	Library for creating telephony solutions that interoperate with Asterisk
License:	LGPL-2.0-or-later
URL:		http://iaxclient.wiki.sourceforge.net/
Source0:	http://downloads.sourceforge.net/iaxclient/%{name}-%{version}%{betaver}.tar.gz
Source1:	tkiaxphone.desktop
Source2:	wxiax.desktop
Source3:	phone.png
Source4:	run-tkiaxphone.sh
Patch0:		iaxclient-2.1beta3-wxGTK28.patch
Patch1:		iaxclient-2.1beta3-tkphone-cleanups.patch
Patch2:		iaxclient-2.1beta3-tcl-includedir.patch
Patch3:		iaxclient-2.1beta3-tcl-libdir.patch
Patch4:		iaxclient-2.1beta3-tcl-nodoc.patch
Patch5:		iaxclient-2.1beta3-theora-detection.patch
Patch6:		iaxclient-2.1beta3-implicit-DSO-libm.patch
Patch7:		iaxclient-2.1beta3-arm-barriers.patch
Patch8:		iaxclient-portable.patch
# Link against the locally build iax
Patch9:		iaxclient-link-local-iax.patch
# Use system ilbc
Patch10:	iaxclient-system-ilbc.patch
# Add missing -fPIC to configure.ac test
Patch11:	iaxclient-2.1beta3-fpic.patch
Patch12:        wxwidgets-3.0.patch
Patch13:        gtk3.patch
Patch14:	iaxclient-gcc14.patch

# Fix some makefile issues
Patch20:	iax-0.2.3_makefile.patch
# Fix format-security issue
Patch21:	iax-0.2.3_format-security.patch
# Add missing #include <sys/socket.h>
Patch22:	iax-0.2.3_socket.patch
Patch23:	iaxclient-c99.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  gtk3-devel
BuildRequires:  ilbc-devel
BuildRequires:  libogg-devel
BuildRequires:  liboggz-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvidcap-devel
BuildRequires:  make
BuildRequires:  portaudio-devel
BuildRequires:  SDL-devel
BuildRequires:  spandsp-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  tk-devel < 1:9
BuildRequires:  wxGTK-devel

%description
Iaxclient is an open source, multiplatform library for creating telephony 
solutions that interoperate with Asterisk, the Open Source PBX.

Although asterisk supports other VOIP protocols (including SIP, and with 
patches, H.323), IAX's simple, lightweight nature gives it several advantages, 
particularly in that it can operate easily through NAT and packet firewalls, 
and it is easily extensible and simple to understand.
Iaxclient pulls together the wide array of open source technologies required 
for telephony applications.

%package libiax
Summary:	IAX library
Obsoletes:	iax < 0.2.3

%description libiax
The %{name}-libs package contains the IAX library version 0.2.3, an improved
version of the abandoned upstream IAX library.

%package libiax-devel
Summary:	IAX library development files
Requires:	%{name}-libiax%{?_isa} = %{version}-%{release}
Obsoletes:	iax-devel < 0.2.3

%description libiax-devel
The %{name}-libiax-devel package contains libraries and header files for
developing applications that use %{name}-libiax.

%package devel
Summary:	Development files for %{name}
Requires:	pkgconfig
Requires:	%{name} = %{mainver}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n tcl-iaxclient
Summary:	Tcl interface to iax2 client lib
Version:	%{tclver}
License:	BSD-3-Clause-No-Nuclear-License
Requires:	tcl(abi) = 8.6
Requires:	%{name} = %{mainver}-%{release}

%description -n tcl-iaxclient
Tcl extensions to iaxclient libraries.

%package -n tkiaxphone
Summary:	Tk IAX Phone Client
Version:	%{mainver}
License:	LGPL-2.0-or-later
Requires:	tcl(abi) = 8.6
Requires:	%{name} = %{mainver}-%{release}

%description -n tkiaxphone
Tk IAX Phone Client.

%package -n wxiax
Summary:	wx IAX Phone Client
Version:	%{mainver}
License:	LGPL-2.0-or-later
Requires:	%{name} = %{mainver}-%{release}

%description -n wxiax
wx IAX Phone Client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{betaver}
%patch -P0 -p1 -b .wxGTK28
%patch -P1 -p1 -b .tkphone
%patch -P2 -p1 -b .includedir
%patch -P3 -p1 -b .libdir
%patch -P4 -p1 -b .nodoc
%patch -P5 -p1 -b .theoradetect
%patch -P6 -p1 -b .DSO
%patch -P7 -p1 -b .arm
%patch -P8 -p1 -b .portable
%patch -P9 -p1 -b .linkiax
%patch -P10 -p1 -b .ilbc
%patch -P11 -p1 -b .fpic
%patch -P12 -p1 -b .wx3
%patch -P13 -p1 -b .gtk3
%patch -P14 -p1 -b .gcc14

# Delete bundled libraries (except libiax2) just to be sure
rm -rf lib/{gsm, portmixer, sox, spandsp}

autoreconf -vif

chmod -x contrib/tcl/README.txt

(
cd lib/libiax2
%patch -P20 -p1 -b .iaxmakefile
%patch -P21 -p1 -b .iaxfmtsecurity
%patch -P22 -p1 -b .iaxsocket

sed -i 's|${exec_prefix}/lib|${exec_prefix}/%{_lib}|g' iax-config.in
sed -i 's|/usr/lib|%{_libdir}|g' iax-config.in

autoreconf -vif
)

%patch -P23 -p1 -b .c99

%build
(
cd lib/libiax2
%configure --disable-static
make %{?_smp_mflags} UCFLAGS="%{optflags}"
)

%configure --disable-static --with-wish=%{_bindir}/wish8.6
# sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
# sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LIBTOOL="%{_bindir}/libtool"

(
cd contrib/tcl/
%configure
make %{?_smp_mflags} LIBTOOL="%{_bindir}/libtool"
)

%install
%make_install -C lib/libiax2

%make_install LIBTOOL="%{_bindir}/libtool"

find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'

install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/iaxclient %{buildroot}%{tcl_sitearch}/

%make_install LIBTOOL="%{_bindir}/libtool" -C contrib/tcl
mv %{buildroot}%{_libdir}/tcliaxclient0.2 %{buildroot}%{tcl_sitearch}/tcliaxclient0.2
chmod +x %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/phone.ui.tcl
chmod +x %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/pref.ui.tcl
install -p %{SOURCE4} %{buildroot}%{_bindir}

install -Dd %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/tkiaxphone.png
install -p %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/wxiax.png

install -Dd %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE1}

desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE2}	

cd %{buildroot}%{tcl_sitearch}/iaxclient/tkphone/
ln -s iaxcli iaxcli-Linux-%{tkphonearch}

%files
%doc AUTHORS ChangeLog README
%license COPYING.LIB
%{_bindir}/iaxcomm
%{_bindir}/iaxphone
%{_datadir}/iaxcomm/
%{_libdir}/libiaxclient.so.*

%files libiax
%doc lib/libiax2/ChangeLog lib/libiax2/COPYING lib/libiax2/COPYING.LIB
%{_libdir}/libiax.so.*

%files libiax-devel
%{_bindir}/iax-config
%{_includedir}/iax/
%{_libdir}/libiax.so

%files devel
%{_bindir}/stresstest
%{_bindir}/testcall
%{_bindir}/vtestcall
%{_includedir}/iaxclient.h
%{_libdir}/libiaxclient.so
%{_libdir}/pkgconfig/iaxclient.pc

%files -n tcl-iaxclient
%doc contrib/tcl/README.txt
%{tcl_sitearch}/tcliaxclient0.2/

%files -n tkiaxphone
%{_bindir}/run-tkiaxphone.sh
%{_bindir}/tkiaxphone
%{tcl_sitearch}/iaxclient/
%{_datadir}/applications/tkiaxphone.desktop
%{_datadir}/pixmaps/tkiaxphone.png

%files -n wxiax
%{_bindir}/wxiax
%{_datadir}/applications/wxiax.desktop
%{_datadir}/pixmaps/wxiax.png

%changelog
%autochangelog
