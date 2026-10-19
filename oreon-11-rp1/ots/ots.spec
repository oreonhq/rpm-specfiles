%global source0_hash ea908d22256166d1200fef55a82dd3ea8e096a249eaaf0b926f3577f1a63e137
Name:		ots
Summary:        A text summarizer
Version:	0.5.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		http://libots.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/libots/ots-%{version}.tar.gz
Patch0: ots-c99.patch
Requires:	%{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
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
%oreon_prep
%build

%configure --with-html-dir=%{_datadir}/gtk-doc/html/ots
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ots-devel -f %{oreon_filedir}/ots-devel.list
%files -n ots-libs -f %{oreon_filedir}/ots-libs.list

%changelog

%autochangelog
