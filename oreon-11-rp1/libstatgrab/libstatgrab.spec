%global source0_hash 5688aa4a685547d7174a8a373ea9d8ee927e766e3cc302bdee34523c2c5d6c11

%bcond_without  log4cplus
%bcond_without  examples

Name:           libstatgrab
Epoch:          1
Version:        0.92.1
Release:        15%{?dist}
Summary:        A library that provides cross platform access to statistics of the system
License:        LGPL-2.1-or-later
URL:            http://www.i-scream.org/libstatgrab
Source0:        http://ftp.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
# REJECTED due to Solaris or whatever linking issue,
# thus we cope with pkgconfig manually.
# See: https://github.com/i-scream/libstatgrab/pull/70
Source1:        libstatgrab.pc.in
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%if %{with log4cplus}
BuildRequires:  log4cplus-devel
%endif
BuildRequires:  ncurses-devel
# Tests.
BuildRequires:  perl-generators
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires: make

%description
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's running. It's written in C and presents a
selection of useful interfaces which can be used to access key system
statistics. The current list of statistics includes CPU usage, memory
utilisation, disk usage, process counts, network traffic, disk I/O, and more.

The current list of supported and tested platforms includes FreeBSD, Linux,
NetBSD, OpenBSD, Solaris, DragonFly BSD, HP-UX and AIX.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains libraries, header files and manpages for
developing applications that use libstatgrab.

%if %{with examples}
%package        examples
Summary:        The example files from %{name}
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    examples
This package contains various examples used to show how
to develop libstatgrab based applications.
%endif

%package -n     saidar
Summary:        System information real-time monitor
License:        GPL-2.0-or-later

%description -n saidar
Saidar is a curses-based interface to viewing the current state of the
system.

%package -n     statgrab
Summary:        Sysctl-style interface to the statistics from libstatgrab
License:        GPL-2.0-or-later

%description -n statgrab
Statgrab gives a sysctl-style interface to the statistics gathered by
libstatgrab. This extends the use of libstatgrab to people writing scripts or
anything else that can't easily make C function calls. Included with statgrab
is a script to generate an MRTG configuration file to use statgrab.

# TODO: F23+2 must drop -tools-compat?
%package        tools-compat
Summary:        Transition package for statgrab-tools
Obsoletes:      statgrab-tools < 1:0.91-0
Requires:       statgrab%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       saidar%{?_isa} = %{epoch}:%{version}-%{release}

%description    tools-compat
This package only exists to help transition statgrab-tools users to the new
package split. It will be removed after 2 distribution release cycles, please
do not reference it or depend on it in any way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Instead of wasting several lines to install these programs, makefile hack
# will save the time.
sed -i 's|noinst_PROGRAMS|bin_PROGRAMS|g' examples/Makefile*
# Place log files underneath /var/log.
sed -i 's|@localstatedir@|@localstatedir@/log|g;s|.log4cplus|.log|g' *.properties.in

%build
cp -pf %{S:1} .
autoreconf -fiv
# Changing to asciidoc            --enable-man-build
%configure --with-ncurses      \
%if %{with log4cplus}
           --with-log4cplus    \
%endif
%if %{with examples}
           --enable-examples   \
%endif
           --disable-static

%make_build

%install
%make_install
%if %{with examples}
%make_install -C examples/
%endif
# Use %%doc instead.
rm -frv %{buildroot}%{_docdir}
# Drop libtool archive.
find %{buildroot} -name '*.la' -delete -print

mkdir -p %{buildroot}%{_docdir}/%{name}-tools-compat/
cat <<'EOF' >> %{buildroot}%{_docdir}/%{name}-tools-compat/README.Fedora
This package only exists to help transition statgrab-tools users to the new
package split. the structure of the transition is:

└── statgrab-tools --> └── %{name}-tools-compat
                           ├── saidar
                           └── statgrab

In the past prior to Fedora 24, libstatgrab had only 1 package for 2 programs
with different usage, while putting them inside one package seems reasonable,
however in order to reduce the size of the package, we decided to halve the
original package, now users can choose which to install, saidar or statgrab.

Note this compat package will be removed after 2 distribution release cycles,
please do not reference it or depend on it in any way.

Yours,
libstatgrab maintainers
EOF

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LGPL
%{_libdir}/*.so.*

%files devel
%doc AUTHORS NEWS PLATFORMS README
%doc examples/*.c
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/*/sg_*

%if %{with examples}
%files examples
%license COPYING
%{_bindir}/cpu_usage
%{_bindir}/disk_traffic
%{_bindir}/filesys_snapshot
%{_bindir}/load_stats
%{_bindir}/network_iface_stats
%{_bindir}/network_traffic
%{_bindir}/os_info
%{_bindir}/page_stats
%{_bindir}/process_snapshot
%{_bindir}/process_stats
%{_bindir}/user_list
%{_bindir}/valid_filesystems
%{_bindir}/vm_stats
%endif

%files tools-compat
%{_docdir}/%{name}-tools-compat/README.Fedora

%files -n saidar
%license COPYING
%{_bindir}/saidar
%if %{with log4cplus}
%config(noreplace) %{_sysconfdir}/saidar.properties
%endif
%{_mandir}/*/saidar*

%files -n statgrab
%license COPYING
%{_bindir}/statgrab*
%if %{with log4cplus}
%config(noreplace) %{_sysconfdir}/statgrab.properties
%endif
%{_mandir}/*/*statgrab*

%changelog
%autochangelog
