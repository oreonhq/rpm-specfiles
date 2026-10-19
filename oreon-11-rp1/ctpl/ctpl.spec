%global source0_hash 21108fc7567ed216deea4591adbfece8e88b1f4bb1ca77c37400920644d756be
%global ctpl_docdir %{_defaultdocdir}/ctpl-%{version}
Name:           ctpl
Version:        0.3.5
Release:        1%{?dist}
Summary:        Template library and engine written in C
License:        GPL-3.0-or-later
URL:            http://ctpl.tuxfamily.org/
Source0:        http://download.tuxfamily.org/ctpl/releases/ctpl-%{version}.tar.gz
Requires:       ctpl-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
# /oreon:deps
%description
CTPL is a template library written in C. It allows fast and easy parsing of
templates from many sources (including in-memory data and local and remote
streaming, thanks to GIO) and fine control over template parsing environment.

CTPL has following features:
* It is a library, then it can be easily used from programs
* Separated lexer and parser
* It is written in portable C
* Simple syntax
* Fast and strict parsing
* Possible in-memory parsing, allowing non-file data parsing and avoiding
  I/O-latency, through GIO's GMemoryInputStream and GMemoryOutputStream

%package libs
Summary: Template library written in C
%description libs
This package contains the CTPL library.

%ldconfig_scriptlets libs

%package devel
Summary:   Development headers of the template library written in C
Requires:  ctpl-libs = %{version}-%{release}
%description devel
This package contains the development headers of the CTPL library.

%package doc
Summary:   Documentation for the CTPL library
Requires:  ctpl-libs = %{version}-%{release}
%description doc
This package contains the HTML documentation reference for the CTPL library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# remove waf since this isn't needed for the build, we're building the
# package with autotools
rm -f waf
rm -f wscript

# The CLI tool only needs to be disabled on RHEL because of GIO dependency issues,

#%patch1 -p1

%build

%configure --docdir %{ctpl_docdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ctpl_docdir}
install -Dpm0644 AUTHORS COPYING NEWS HACKING TODO README THANKS $RPM_BUILD_ROOT%{ctpl_docdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.la
%oreon_autofiles ctpl-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ctpl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ctpl-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ctpl-libs -f %{oreon_filedir}/ctpl-libs.list
%files -n ctpl-devel -f %{oreon_filedir}/ctpl-devel.list
%files -n ctpl-doc -f %{oreon_filedir}/ctpl-doc.list

%changelog

%autochangelog
