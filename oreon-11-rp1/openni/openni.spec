%global source0_hash 2de0a0beb3879f4fe9a7effa97403363a1a2bfb771d37908905290faf686bda3

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

# Automatically converted from old format: ASL 2.0 and BSD - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            http://www.openni.org
# To reproduce tarball (adapt version and shortcommit):
# wget https://github.com/OpenNI/OpenNI/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# tar xvf openni-%{version}-%{shortcommit}.tar.gz
# cd OpenNI-%{commit}
# rm -rf Platform/Win32 Platform/Android Platform/ARC
# cd ..
# tar czf openni-%{version}-%{shortcommit}-fedora.tar.gz OpenNI-%{commit}
Source0:        openni-%{version}-%{shortcommit}-fedora.tar.gz
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
# Fix compilation with -ansi or -std options
# https://github.com/OpenNI/OpenNI/commit/ca99f6181234c682bba42a6ba988cc10cee894d7
Patch9:         openni-ansi.patch

Patch10:        python3.patch

ExclusiveArch:  x86_64 %{arm}

BuildRequires:  gcc-c++, make
BuildRequires:  freeglut-devel, tinyxml-devel, libjpeg-devel, dos2unix, libusb1-devel
BuildRequires:  python3, doxygen, graphviz

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
# {?_smp_mflags} omitted, not supported by OpenNI Makefiles
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

%files
%doc LICENSE README NOTICE CHANGES
%dir %{_sysconfdir}/%{name}
%dir %{_var}/lib/ni
%ghost %{_var}/lib/ni/modules.xml
%{_libdir}/*.so
%{_bindir}/ni*

%files devel
%doc Documentation/OpenNI_UserGuide.pdf
%{_includedir}/*
%{_libdir}/pkgconfig/libopenni.pc

%files java
%{_libdir}/%{name}

%files examples
%config(noreplace) %{_sysconfdir}/%{name}/SamplesConfig.xml
%{_bindir}/Ni*
# not packaging any .desktop files for the sample applications. The
# applications will print relevant to the console and hence they are
# intended to be run on the console, not from the menu

%files doc
%doc Source/DoxyGen/html

%changelog
%autochangelog
