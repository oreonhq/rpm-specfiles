%global source0_hash 5688aa4a685547d7174a8a373ea9d8ee927e766e3cc302bdee34523c2c5d6c11
%bcond_without  log4cplus
%bcond_without  examples
Name:           libstatgrab
Epoch:          1
Version:        0.92.1
Release:        1%{?dist}
Summary:        A library that provides cross platform access to statistics of the system
License:        LGPL-2.1-or-later
URL:            http://www.i-scream.org/libstatgrab
Source0:        http://ftp.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
Source1:        libstatgrab.pc.in
%if %{with log4cplus}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  log4cplus-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
rm -frv %{buildroot}%{_docdir}
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
%oreon_autofiles saidar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles statgrab usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libstatgrab-devel -f %{oreon_filedir}/libstatgrab-devel.list
%files -n libstatgrab-examples -f %{oreon_filedir}/libstatgrab-examples.list
%files -n saidar -f %{oreon_filedir}/saidar.list
%files -n statgrab -f %{oreon_filedir}/statgrab.list
%files -n libstatgrab-tools-compat -f %{oreon_filedir}/libstatgrab-tools-compat.list

%changelog

%autochangelog
