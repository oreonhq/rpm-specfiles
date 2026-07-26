%global source0_hash 21108fc7567ed216deea4591adbfece8e88b1f4bb1ca77c37400920644d756be

%global ctpl_docdir %{_defaultdocdir}/ctpl-%{version}

Name:           ctpl
Version:        0.3.5
Release:        5%{?dist}
Summary:        Template library and engine written in C

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://ctpl.tuxfamily.org/
Source0:        http://download.tuxfamily.org/ctpl/releases/ctpl-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.10
BuildRequires:  make
Requires:       ctpl-libs = %{version}-%{release}

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

%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch: noarch
%endif

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
%if 0%{?rhel}
%patch -P0 -p1
%endif

#%patch1 -p1

%build
%if 0%{?rhel}
%configure --docdir %{ctpl_docdir} --disable-cli-tool
%else
%configure --docdir %{ctpl_docdir}
%endif

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Seems the --docdir flag is not working correctly, working around this here
# for now
install -d $RPM_BUILD_ROOT%{ctpl_docdir}
install -Dpm0644 AUTHORS COPYING NEWS HACKING TODO README THANKS $RPM_BUILD_ROOT%{ctpl_docdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.la

%if ! 0%{?rhel}
%files
%doc %{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%endif

%files libs
%dir %{ctpl_docdir}
%doc %{ctpl_docdir}/AUTHORS
%doc %{ctpl_docdir}/COPYING
%doc %{ctpl_docdir}/NEWS
%{_libdir}/lib%{name}.so.*
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/it/LC_MESSAGES/%{name}.mo

%files devel
%doc %{ctpl_docdir}/HACKING
%doc %{ctpl_docdir}/TODO
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{ctpl_docdir}/README
%doc %{ctpl_docdir}/THANKS
%doc %{_datadir}/gtk-doc/html/%{name}

%changelog
%autochangelog
