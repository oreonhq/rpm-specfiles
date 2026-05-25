%{?mingw_package_header}

%global api_version 1.0

Name:           mingw-gstreamer1
Version:        1.28.2
Release:        1%{?dist}
Summary:        MinGW Windows Streaming-Media Framework Runtime

License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2

BuildRequires:  bison flex
BuildRequires:  perl-interpreter


%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win32
%package  -n mingw32-gstreamer1
Summary:        MinGW Windows Streaming-Media Framework Runtime

%description -n mingw32-gstreamer1
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win64
%package  -n mingw64-gstreamer1
Summary:        MinGW Windows Streaming-Media Framework Runtime

%description -n mingw64-gstreamer1
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gstreamer-%{version}


%build
%mingw_meson \
	-Dpackage-name='Fedora MinGW GStreamer package' \
	-Dpackage-origin='http://download.fedoraproject.org' \
	-Dtests=disabled \
	-Dexamples=disabled

%mingw_ninja


%install
%mingw_ninja_install

# Don't ship debug helpers
rm -rf %{buildroot}%{mingw32_datadir}/gstreamer-1.0/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gstreamer-1.0/gdb
rm -rf %{buildroot}%{mingw32_datadir}/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gdb
rmdir %{buildroot}%{mingw32_datadir}/gstreamer-1.0/
rmdir %{buildroot}%{mingw64_datadir}/gstreamer-1.0/

# Don't ship man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%mingw_find_lang gstreamer-%{api_version}


# Win32
%files -n mingw32-gstreamer1 -f mingw32-gstreamer-%{api_version}.lang
%license COPYING

%dir %{mingw32_includedir}/gstreamer-%{api_version}
%{mingw32_includedir}/gstreamer-%{api_version}/gst

%dir %{mingw32_libexecdir}/gstreamer-%{api_version}
%{mingw32_libexecdir}/gstreamer-%{api_version}/gst-completion-helper.exe
%{mingw32_libexecdir}/gstreamer-%{api_version}/gst-plugin-scanner.exe

%dir %{mingw32_libdir}/gstreamer-%{api_version}/
%{mingw32_libdir}/gstreamer-%{api_version}/*.dll
%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
%{mingw32_libdir}/libgstbase-%{api_version}.dll.a
%{mingw32_libdir}/libgstcheck-%{api_version}.dll.a
%{mingw32_libdir}/libgstcontroller-%{api_version}.dll.a
%{mingw32_libdir}/libgstnet-%{api_version}.dll.a
%{mingw32_libdir}/libgstreamer-%{api_version}.dll.a
%{mingw32_libdir}/pkgconfig/gstreamer-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-base-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-check-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-controller-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-net-%{api_version}.pc

%{mingw32_bindir}/gst-inspect-%{api_version}.exe
%{mingw32_bindir}/gst-launch-%{api_version}.exe
%{mingw32_bindir}/gst-stats-%{api_version}.exe
%{mingw32_bindir}/gst-typefind-%{api_version}.exe

%{mingw32_bindir}/libgstbase-%{api_version}-0.dll
%{mingw32_bindir}/libgstcheck-%{api_version}-0.dll
%{mingw32_bindir}/libgstcontroller-%{api_version}-0.dll
%{mingw32_bindir}/libgstnet-%{api_version}-0.dll
%{mingw32_bindir}/libgstreamer-%{api_version}-0.dll

%{mingw32_datadir}/aclocal/gst-element-check-%{api_version}.m4
%{mingw32_datadir}/cmake/FindGStreamer.cmake


# Win64
%files -n mingw64-gstreamer1 -f mingw64-gstreamer-%{api_version}.lang
%license COPYING

%dir %{mingw64_includedir}/gstreamer-%{api_version}
%{mingw64_includedir}/gstreamer-%{api_version}/gst

%dir %{mingw64_libexecdir}/gstreamer-%{api_version}
%{mingw64_libexecdir}/gstreamer-%{api_version}/gst-completion-helper.exe
%{mingw64_libexecdir}/gstreamer-%{api_version}/gst-plugin-scanner.exe

%dir %{mingw64_libdir}/gstreamer-%{api_version}/
%{mingw64_libdir}/gstreamer-%{api_version}/*.dll
%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a
%{mingw64_libdir}/libgstbase-%{api_version}.dll.a
%{mingw64_libdir}/libgstcheck-%{api_version}.dll.a
%{mingw64_libdir}/libgstcontroller-%{api_version}.dll.a
%{mingw64_libdir}/libgstnet-%{api_version}.dll.a
%{mingw64_libdir}/libgstreamer-%{api_version}.dll.a
%{mingw64_libdir}/pkgconfig/gstreamer-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-base-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-check-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-controller-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-net-%{api_version}.pc

%{mingw64_bindir}/gst-inspect-%{api_version}.exe
%{mingw64_bindir}/gst-launch-%{api_version}.exe
%{mingw64_bindir}/gst-stats-%{api_version}.exe
%{mingw64_bindir}/gst-typefind-%{api_version}.exe

%{mingw64_bindir}/libgstbase-%{api_version}-0.dll
%{mingw64_bindir}/libgstcheck-%{api_version}-0.dll
%{mingw64_bindir}/libgstcontroller-%{api_version}-0.dll
%{mingw64_bindir}/libgstnet-%{api_version}-0.dll
%{mingw64_bindir}/libgstreamer-%{api_version}-0.dll

%{mingw64_datadir}/aclocal/gst-element-check-%{api_version}.m4
%{mingw64_datadir}/cmake/FindGStreamer.cmake


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.2-1
- Import
