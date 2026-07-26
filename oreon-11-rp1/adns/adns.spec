%global source0_hash 7138b3789b7506bd683f451d4f7d853077a91803b7b35d86ec667f0f9cd401cd

Name:		adns
Version:	1.6.1
Release:	6%{?dist}

Summary:	Advanced, easy to use, asynchronous-capable DNS client library

License:	GPL-1.0-or-later
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
Source0:	http://www.chiark.greenend.org.uk/~ian/adns/ftp/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:  gcc
BuildRequires: make

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
 - It is reasonably easy to use for simple programs which just want to
   translate names to addresses, look up MX records, etc.
 - It can be used in an asynchronous, non-blocking, manner. Many
   queries can be handled simultaneously.
 - Responses are decoded automatically into a natural representation
   for a C program - there is no need to deal with DNS packet formats.
 - Sanity checking (eg, name syntax checking, reverse/forward
   correspondence, CNAME pointing to CNAME) is performed automatically.
 - Time-to-live, CNAME and other similar information is returned in an
   easy-to-use form, without getting in the way.
 - There is no global state in the library; resolver state is an opaque
   data structure which the client creates explicitly. A program can have
   several instances of the resolver.
 - Errors are reported to the application in a way that distinguishes
   the various causes of failure properly.
 - Understands conventional resolv.conf, but this can overridden by
   environment variables.
 - Flexibility. For example, the application can tell adns to: ignore
   environment variables (for setuid programs), disable sanity checks eg
   to return arbitrary data, override or ignore resolv.conf in favour of
   supplied configuration, etc.
 - Believed to be correct ! For example, will correctly back off to TCP
   in case of long replies or queries, or to other nameservers if several
   are available. It has sensible handling of bad responses etc.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Requires:	%{name} = %{version}

%description devel
Asynchronous-capable DNS client library - development files.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Requires:	%{name} = %{version}

%description progs
DNS utility programs: adns also comes with a number of utility
programs for use from the command line and in scripts:
 - adnslogres is a much faster version of Apache's logresolv program,
 - adnsresfilter is a filter which copies its input to its output,
   replacing IP addresses by the corresponding names, without unduly
   delaying the output. For example, you can usefully pipe the output of
   netstat -n, tcpdump -ln, and the like, into it.
 - adnshost is a general-purpose DNS lookup utility which can be used
   easily in from the command line and from shell scripts to do simple
   lookups. In a more advanced mode it can be used as a general-purpose
   DNS helper program for scripting languages which can invoke and
   communicate with subprocesses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%ifarch sparcv9 sparc64 s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fpic"
%endif
autoreconf -fiv
%configure --enable-dynamic
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    includedir=$RPM_BUILD_ROOT%{_includedir} \
    libdir=$RPM_BUILD_ROOT%{_libdir} \
    install

rm -f $RPM_BUILD_ROOT%{_libdir}/libadns.a

%ldconfig_scriptlets

%files
%doc README TODO changelog
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%files progs
%attr(755,root,root) %{_bindir}/*

%changelog
%autochangelog
