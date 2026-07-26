%global source0_hash 5a12bcf2a26dac7f2a5c9507c662c4c85556881c64bb55365dceb437cf3652cd

%global realname drumstick

Summary: C++/Qt4 wrapper around the ALSA library sequencer interface
Name:    drumstick0
Version: 0.5.0
Release: 40%{?dist}
#define svn svn

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://drumstick.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/drumstick/%{version}%{?svn}/drumstick-%{version}%{?svn}.tar.bz2
# fix FTBFS due to the strict ld in Fedora >= 13
Patch0:  drumstick-0.5.0-fix-implicit-linking.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1307434
Patch1:  drumstick-0.5.0-gcc6.patch

BuildRequires: gcc-c++
BuildRequires: cmake qt4-devel alsa-lib-devel desktop-file-utils
BuildRequires: shared-mime-info
# For building manpages
BuildRequires: docbook-style-xsl /usr/bin/xsltproc
# For building API documents
BuildRequires: doxygen

Obsoletes: aseqmm < %{version}-%{release}
Provides: aseqmm = %{version}-%{release}

%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt4 objects, idioms and style. The ALSA sequencer interface
provides software support for MIDI technology on GNU/Linux.

%package devel
Summary: Developer files for %{name}
Conflicts: %{realname}-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: aseqmm-devel < %{version}-%{release}
Provides: aseqmm-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-%{version}%{?svn}
%patch -P0 -p1 -b .implicit-linking
%patch -P1 -p1 -b .gcc6

%build
%cmake 
%cmake_build
doxygen %{_vpath_builddir}/Doxyfile

%install
%cmake_install
mv $RPM_BUILD_ROOT%{_datadir}/mime/packages/{%{realname},%{name}}.xml
# don't include example applications in the compat package
rm -fr $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/icons \
       $RPM_BUILD_ROOT%{_datadir}/man \
       $RPM_BUILD_ROOT%{_datadir}/applications

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/libdrumstick-file.so.*
%{_libdir}/libdrumstick-alsa.so.*
%{_datadir}/mime/packages/%{name}.xml

%files devel
%doc doc/html/*
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/pkgconfig/drumstick-file.pc
%{_libdir}/pkgconfig/drumstick-alsa.pc
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%changelog
%autochangelog
