%global source0_hash fe20326b0d10641f71c4673fae637bf9222a96e1712f71f170fca2fc34bf7a83

Summary: Music Player Daemon Library
Name: libmpd
Version: 11.8.17
Release: 30%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: http://gmpc.wikia.com/wiki/Gnome_Music_Player_Client
Source: http://download.sarine.nl/Programs/gmpc/11.8/libmpd-11.8.17.tar.gz
Patch0: libmpd-11.8.17-strndup.patch
Patch1: libmpd-c99.patch
BuildRequires:  gcc
BuildRequires: glib2-devel >= 2.16
BuildRequires: make

%package devel
Summary: Header files for developing programs with libmpd
Requires: %{name} = %{version}
Requires: pkgconfig

%description
libmpd is an abstraction around libmpdclient. It provides an easy and
reliable callback based interface to mpd.

%description devel
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .strndup
%patch -P 1 -p1

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR="$RPM_BUILD_ROOT" install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%doc ChangeLog COPYING README
%{_libdir}/libmpd.so.1*

%files devel
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd-1.0

%changelog
%autochangelog
