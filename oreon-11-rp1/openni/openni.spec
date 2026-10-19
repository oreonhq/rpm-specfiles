%global source0_hash fd1c15c6334bb9d69733bd69c76f19f5544cce65f61bc7710085c63d167a6e52
%global commit 1e9524ffd759841789dadb4ca19fb5d4ac5820e7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%ifarch x86_64
%global niarch x64
%endif
%ifarch %{ix86}
%global niarch x86
%endif
%ifarch %arm
%global niarch Arm
%endif
Name:           openni
Version:        1.5.7.10
Release:        39%{?dist}
Summary:        Library for human-machine Natural Interaction
License:        Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            http://www.openni.org
Source0:        https://github.com/OpenNI/OpenNI/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        libopenni.pc
Patch0:         openni-1.5.7.10-willow.patch
Patch1:         openni-1.5.7.10-fedora.patch
Patch2:         openni-1.5.2.23-disable-sse.patch
Patch3:         openni-1.3.2.1-silence-assert.patch
Patch4:         openni-1.3.2.1-fedora-java.patch
Patch5:         openni-1.5.2.23-disable-softfloat.patch
Patch6:         openni-1.5.2.23-armsamples.patch
Patch7:         openni-1.5.7.10-rename-equivalent-for-gcc6.patch
Patch8:         openni-freeglut.patch
Patch9:         openni-ansi.patch
Patch10:        python3.patch
ExclusiveArch:  x86_64 %{arm}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  libjpeg-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  tinyxml-devel
# /oreon:deps
%description
OpenNI (Open Natural Interaction) is a multi-language, cross-platform
framework that defines APIs for writing applications utilizing Natural
Interaction. OpenNI APIs are composed of a set of interfaces for writing NI
applications. The main purpose of OpenNI is to form a standard API that
enables communication with both:
 * Vision and audio sensors
 * Vision and audio perception middleware

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        java
Summary:        %{name} Java library
Requires:       %{name} = %{version}-%{release}
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
Requires:       java-25-headless
Requires:       jpackage-utils
%description    java
The %{name}-java package contains a Java JNI library for
developing applications that use %{name} in Java.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains the automatically generated API documentation
for OpenNI.

%package        examples
Summary:        Sample programs for %{name}
Requires:       %{name} = %{version}-%{release}
%description    examples
The %{name}-examples package contains example programs for OpenNI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n OpenNI-%{commit}
rm -rf Platform/Win32 Platform/Android Platform/ARC
%patch -P0 -p1 -b .willow
%patch -P1 -p1 -b .fedora
%patch -P2 -p1 -b .disable-sse
%patch -P3 -p1 -b .silence-assert
%patch -P4 -p1 -b .fedora-java
%patch -P5 -p1 -b .disable-softfloat
%patch -P6 -p1 -b .armsamples
%patch -P7 -p1 -b .rename-equivalent-for-gcc6
%patch -P8 -p0 -b .freeglut
%patch -P9 -p1 -b .ansi
dos2unix Platform/Linux/CreateRedist/Redist_OpenNi.py
%patch -P10 -p1 -b python3
rm -rf Source/External
rm -rf Platform/Linux/Build/Prerequisites/*
find Samples -name GL -prune -exec rm -rf {} \;
find Samples -name Libs -prune -exec rm -rf {} \;

for ext in c cpp; do
  find Samples -name "*.$ext" -exec \
    sed -i -e 's|#define SAMPLE_XML_PATH "../../../../Data/SamplesConfig.xml"|#define SAMPLE_XML_PATH "%{_sysconfdir}/%{name}/SamplesConfig.xml"|' {} \;
done

sed -i 's|python|python3|' Platform/Linux/CreateRedist/RedistMaker
sed -i 's|if (os.path.exists("/usr/bin/gmcs"))|if (0)|' Platform/Linux/CreateRedist/Redist_OpenNi.py

dos2unix README
dos2unix LICENSE

%build

cd Platform/Linux/CreateRedist
chmod +x RedistMaker RedistMaker.Arm
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DEBUG=1 \
%ifarch %arm
./RedistMaker.Arm || cat Output/BuildOpenNI.txt
%else
./RedistMaker
%endif
cat Output/BuildOpenNI.txt
%install
rm -rf $RPM_BUILD_ROOT
pushd Platform/Linux/Redist/OpenNI-Bin-Dev-Linux-%{niarch}-v%{version}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/ni \
INSTALL_VAR=$RPM_BUILD_ROOT%{_var}/lib/ni \
INSTALL_JAR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
./install.sh -n
install -m 0755 Samples/Bin/%{niarch}-Release/libSample-NiSampleModule.so $RPM_BUILD_ROOT%{_libdir}/libNiSampleModule.so
install -m 0755 Samples/Bin/%{niarch}-Release/NiViewer $RPM_BUILD_ROOT%{_bindir}
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiAudioSample $RPM_BUILD_ROOT%{_bindir}/NiAudioSample
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiBackRecorder $RPM_BUILD_ROOT%{_bindir}/NiBackRecorder
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiConvertXToONI $RPM_BUILD_ROOT%{_bindir}/NiConvertXToONI
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiCRead $RPM_BUILD_ROOT%{_bindir}/NiCRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiRecordSynthetic $RPM_BUILD_ROOT%{_bindir}/NiRecordSynthetic
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleCreate $RPM_BUILD_ROOT%{_bindir}/NiSimpleCreate
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleRead $RPM_BUILD_ROOT%{_bindir}/NiSimpleRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleViewer $RPM_BUILD_ROOT%{_bindir}/NiSimpleViewer
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiUserTracker $RPM_BUILD_ROOT%{_bindir}/NiUserTracker
popd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 0644 Data/SamplesConfig.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/ni
touch $RPM_BUILD_ROOT%{_var}/lib/ni/modules.xml
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
    -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
    -e 's![@]libdir[@]!%{_libdir}!g' \
    -e 's![@]includedir[@]!%{_includedir}!g' \
    -e 's![@]version[@]!%{version}!g' \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/libopenni.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{?ldconfig}
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libnimMockNodes.so
  niReg -r %{_libdir}/libnimCodecs.so
  niReg -r %{_libdir}/libnimRecorder.so
fi
%preun

if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libnimMockNodes.so
  niReg -u %{_libdir}/libnimCodecs.so
  niReg -u %{_libdir}/libnimRecorder.so
fi
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n openni-devel -f %{oreon_filedir}/openni-devel.list
%files -n openni-java -f %{oreon_filedir}/openni-java.list
%files -n openni-doc -f %{oreon_filedir}/openni-doc.list
%files -n openni-examples -f %{oreon_filedir}/openni-examples.list

%changelog

%autochangelog
