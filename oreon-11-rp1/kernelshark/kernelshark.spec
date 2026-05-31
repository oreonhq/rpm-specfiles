%global source0_hash 6ec307876b28fb08fc4833f14d29e02cb51fcb7d48054b51b24b3f2a6e5db9d9

Name: kernelshark
Version: 2.3.1
Release: 8%{?dist}
Epoch: 1

# As of 2.3.1, only kernelshark.cpp, kshark-record.cpp and examples are GPL-2.0. The rest of kernel-shark is LGPL-2.1.
# See SPDX identifier for most accurate info
License: GPL-2.0-only AND LGPL-2.1-only
Summary: GUI analysis for Ftrace data captured by trace-cmd

URL: https://kernelshark.org
Source0:        https://git.kernel.org/pub/scm/utils/trace-cmd/kernel-shark.git/snapshot/kernel-shark-kernelshark-v%{version}.tar.gz
Source1: %{name}.appdata.xml

ExcludeArch: %{ix86} %{arm}

BuildRequires: cmake 
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libappstream-glib
BuildRequires: pkgconf
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6StateMachine)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: libtracecmd-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: libtracecmd >= 1.5.0
BuildRequires: trace-cmd
BuildRequires: xmlto
BuildRequires: make
BuildRequires: chrpath
BuildRequires: freeglut-devel
BuildRequires: font(notosans)
BuildRequires: fontconfig
BuildRequires: docbook-style-xsl
BuildRequires: texlive-epstopdf
BuildRequires: ghostscript
BuildRequires: marshalparser
Requires: polkit
Requires: font(notosans)


%description
KernelShark is a front end reader of trace-cmd output. "trace-cmd
record" and "trace-cmd extract" create a trace.dat (trace-cmd.dat)
file. kernelshark can read this file and produce a graph and list
view of its data. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n kernel-shark-%{name}-v%{version}

%build
cd build
tt_font=`fc-list NotoSans:style=Regular | cut -d':' -f 1 -z`
# To fix error: ‘for_each’ is not a member of ‘std’
sed -i '/iostream/a #include <algorithm>' ../src/plugins/LatencyPlot.cpp
cmake ..  -DCMAKE_BUILD_TYPE=Package -D_INSTALL_PREFIX=%{_prefix} -D_LIBDIR=%{_libdir} -DCMAKE_C_FLAGS_PACKAGE="%{optflags}" -DCMAKE_EXE_LINKER_FLAGS="%{build_ldflags}" -D_DOXYGEN_DOC=1 -DTT_FONT_FILE=${tt_font} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
make V=1 all doc

%install
cd build
make libdir=%{_libdir} prefix=%{_prefix} V=1 DESTDIR=%{buildroot}/  install
sed -i '/Version/d' %{buildroot}/%{_datadir}/applications/kernelshark.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kernelshark.desktop
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

#Remove all rpath
find %{buildroot} -type f -perm 755 -name \*so\* -exec chrpath --delete {} \;
chrpath --delete %{buildroot}/%{_bindir}/kernelshark
chrpath --delete %{buildroot}/%{_bindir}/kshark-record

%files
%doc README
%{_bindir}/kernelshark
%{_bindir}/kshark-record
%{_bindir}/kshark-su-record
%dir %{_libdir}/kernelshark
%{_libdir}/kernelshark/*
%{_datadir}/applications/kernelshark.desktop
%dir %{_datadir}/icons/kernelshark
%{_datadir}/icons/kernelshark/*
%{_datadir}/polkit-1/actions/org.freedesktop.kshark-record.policy
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/libkshark-gui.so.*
%{_libdir}/libkshark-plot.so.*
%{_libdir}/libkshark.so
%{_libdir}/libkshark.so.*
%{_libdir}/pkgconfig/libkshark.pc
%{_includedir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-8
- Prepare for Oreon 11 (RP1)
