%global source0_hash e4e1dccc92cb4be7c34dc513216f0ffc3610fe071d87e28ceecf784b43d6ccf3
%{?mingw_package_header}
%global api_version 1.0
Name:           mingw-gstreamer1
Version:        1.29.2
Release:        1%{?dist}
Summary:        MinGW Windows Streaming-Media Framework Runtime
License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2
BuildRequires:  perl-interpreter
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gstreamer-%{version}
%oreon_prep
%build

%mingw_meson \
	-Dpackage-name='Fedora MinGW GStreamer package' \
	-Dpackage-origin='http://download.fedoraproject.org' \
	-Dtests=disabled \
	-Dexamples=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_datadir}/gstreamer-1.0/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gstreamer-1.0/gdb
rm -rf %{buildroot}%{mingw32_datadir}/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gdb
rmdir %{buildroot}%{mingw32_datadir}/gstreamer-1.0/
rmdir %{buildroot}%{mingw64_datadir}/gstreamer-1.0/
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%mingw_find_lang gstreamer-%{api_version}
%oreon_autofiles mingw32-gstreamer1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gstreamer1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gstreamer1 -f %{oreon_filedir}/mingw32-gstreamer1.list
%files -n mingw64-gstreamer1 -f %{oreon_filedir}/mingw64-gstreamer1.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.2-1
- Import
