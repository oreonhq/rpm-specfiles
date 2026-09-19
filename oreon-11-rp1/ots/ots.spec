%global source0_hash ea908d22256166d1200fef55a82dd3ea8e096a249eaaf0b926f3577f1a63e137

Name:		ots
Summary:	A text summarizer
Version:	0.5.0
Release:	36%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://libots.sourceforge.net/

Source0:	http://prdownloads.sourceforge.net/libots/ots-%{version}.tar.gz
Patch0: ots-c99.patch

BuildRequires: make
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	popt-devel >= 1.5
BuildRequires:	libtool

Requires:	%{name}-libs = %{version}-%{release}

%description
The open text summarizer is an open source tool for summarizing texts.
The program reads a text and decides which sentences are important and
which are not.

 
%package	devel
Summary: 	Libraries and include files for developing with libots
Requires:	%{name}-libs = %{version}-%{release}
Requires: 	glib2-devel >= 2.0
Requires:	libxml2-devel >= 2.4.23
Requires:	popt-devel >= 1.5
Requires:	pkgconfig

%description	devel
This package provides the necessary development libraries and include
files to allow you to develop with libots.

%package	libs
Summary:	Shared libraries for %{name}

%description	libs
The %{name}-libs package contains shared libraries used by %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --with-html-dir=%{_datadir}/gtk-doc/html/ots
# XXX: Disgusting kludge to fix upstream's broken package.
touch ./gtk-doc.make
%{__make} \
%if 0%{?flatpak}
    LIBTOOL=/usr/bin/libtool
%else
    LIBTOOL=%{_bindir}/libtool
%endif

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%ldconfig_scriptlets	libs

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/ots

%files	libs
%doc COPYING
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/libots-1.so.*
%{_datadir}/ots/

%files	devel
%doc COPYING
%{_libdir}/libots-1.so
%{_includedir}/libots-1/
%{_libdir}/pkgconfig/libots-1.pc

%changelog
%autochangelog
