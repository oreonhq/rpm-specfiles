%global source0_hash 29c4a53481591faf2f30086a16a58cadd8a963d540c0b0f10ec464a99003d93c
%{!?with_Werror: %global with_Werror 0}
%{!?with_sqlite: %global with_sqlite 0%{?fedora} >= 17 || 0%{?rhel} >= 7}
%{!?with_docs: %global with_docs 0}
%{!?with_htmldocs: %global with_htmldocs 0}
%{!?with_monitor: %global with_monitor 1}
%ifarch ppc ppc64 %{sparc} %{mips} %{riscv}
%{!?with_crash: %global with_crash 0}
%else
%{!?with_crash: %global with_crash 1}
%endif
%{!?with_rpm: %global with_rpm 1}
%{!?elfutils_version: %global elfutils_version 0.179}
%{!?with_boost: %global with_boost 1}
%ifarch x86_64 ppc ppc64 ppc64le aarch64
%{!?with_dyninst: %global with_dyninst 0%{?fedora} >= 18 || 0%{?rhel} >= 7}
%else
%{!?with_dyninst: %global with_dyninst 0}
%endif
%{!?with_bpf: %global with_bpf 0%{?fedora} >= 22 || 0%{?rhel} >= 8}
%{!?with_systemd: %global with_systemd 0%{?fedora} >= 19 || 0%{?rhel} >= 7}
%{!?with_emacsvim: %global with_emacsvim 0%{?fedora} >= 19 || 0%{?rhel} >= 7}
%ifarch %{ix86}
%{!?with_java: %global with_java 0}
%else
%{!?with_java: %global with_java 0%{?fedora} >= 19 || 0%{?rhel} >= 7}
%endif
%{!?with_debuginfod: %global with_debuginfod 0%{?fedora} >= 25 || 0%{?rhel} >= 7}
%{!?with_virthost: %global with_virthost 0%{?fedora} >= 19 || 0%{?rhel} >= 7}
%{!?with_virtguest: %global with_virtguest 1}
%{!?with_dracut: %global with_dracut 0%{?fedora} >= 19 || 0%{?rhel} >= 6}
%ifarch x86_64
%{!?with_mokutil: %global with_mokutil 0%{?fedora} >= 18 || 0%{?rhel} >= 7}
%{!?with_openssl: %global with_openssl 0%{?fedora} >= 18 || 0%{?rhel} >= 7}
%else
%{!?with_mokutil: %global with_mokutil 0}
%{!?with_openssl: %global with_openssl 0}
%endif
%{!?with_pyparsing: %global with_pyparsing 0%{?fedora} >= 18 || 0%{?rhel} >= 7}
%{!?with_python3: %global with_python3 0%{?fedora} >= 23 || 0%{?rhel} > 7}
%{!?with_python2_probes: %global with_python2_probes (0%{?fedora} <= 28 && 0%{?rhel} <= 7)}
%{!?with_python3_probes: %global with_python3_probes (0%{?fedora} >= 23 || 0%{?rhel} > 7)}
%{!?with_httpd: %global with_httpd 0}
%{!?with_specific_python: %global with_specific_python 0%{?fedora} >= 31}
%{!?with_sysusers: %global with_sysusers 0%{?fedora} >= 32 || 0%{?rhel} >= 9}
%{!?with_check: %global with_check 0}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 6 || 0%{?oreon} >= 11
   %define initdir %{_initddir}
%else
   %define initdir %{_initrddir}
%endif
%if %{with_virtguest}
   %if 0%{?fedora} >= 18 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
      %define udevrulesdir /usr/lib/udev/rules.d
   %else
   %endif
%endif
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
   %define dracutstap %{_prefix}/lib/dracut/modules.d/99stap
%else
   %define dracutstap %{_prefix}/share/dracut/modules.d/99stap
%endif
    %define dracutbindir %{_bindir}
%{!?_rpmmacrodir: %define _rpmmacrodir %{_rpmconfigdir}/macros.d}
%define __brp_mangle_shebangs_exclude_from .stp$
%define _systemtap_runtime_preinstall \
\
g     stapusr  156\
g     stapsys  157\
g     stapdev  158\
g     stapunpriv 159\
u     stapunpriv 159      "systemtap unprivileged user"   /var/lib/stapunpriv   /sbin/nologin\
m     stapunpriv stapunpriv
%define _systemtap_server_preinstall \
\
g     stap-server  -\
u     stap-server  -      "systemtap compiler server"   /var/lib/stap-server   /sbin/nologin\
m     stap-server stap-server
%define _systemtap_testsuite_preinstall \
\
u     stapusr  -          "systemtap testsuite user"    /   /sbin/nologin\
u     stapsys  -          "systemtap testsuite user"    /   /sbin/nologin\
u     stapdev  -          "systemtap testsuite user"    /   /sbin/nologin\
m     stapusr  stapusr\
m     stapsys  stapusr\
m     stapsys  stapsys\
m     stapdev  stapusr\
m     stapdev  stapdev
%define _systemtap_server_preinstall_tmpfiles \
d /var/lib/stap-server 0750 stap-server stap-server -\
d /var/lib/stap-server/.systemtap 0700 stap-server stap-server -\
d /var/log/stap-server 0755 stap-server stap-server -\
f /var/log/stap-server/log 0644 stap-server stap-server -
Name: systemtap
Version: 5.6
Release:        1%{?dist}
Summary:        Programmable system-wide instrumentation system
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Source0:        https://sourceware.org/pub/systemtap/releases/systemtap-%{version}.tar.gz
%if %{with_debuginfod}
%endif
%if %{with_dyninst}
%endif
%if %{with_sqlite}
%endif
%if %{with_monitor}
%endif
%if %{with_systemd}
%endif
%if %{with_crash}
%endif
%if %{with_rpm}
%endif
%if %{with_docs}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%endif
%if %{with_htmldocs}
%endif
%endif
%if %{with_emacsvim}
%endif
%if %{with_java}
%endif
%if %{with_python2_probes}
%endif
%if %{with_python3}
%endif
%if %{with_python3_probes}
%endif
%if %{with_httpd}
%endif
%if %{with_sysusers}
%endif
%if %{with_check}
%endif
Requires: systemtap-client = %{version}-%{release}
Requires: systemtap-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/dvips
BuildRequires:  /usr/bin/latex
BuildRequires:  /usr/bin/ps2pdf
BuildRequires:  avahi-devel
BuildRequires:  boost-devel
BuildRequires:  cpio
BuildRequires:  crash-devel
BuildRequires:  dejagnu
BuildRequires:  elfutils-devel
BuildRequires:  emacs-common
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  kernel-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  nss-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(nss)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  readline-devel
BuildRequires:  rpm-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  tex(bchr7t.tfm)
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  zlib-devel
# /oreon:deps
%description
SystemTap is an instrumentation system for systems running Linux.
Developers can write instrumentation scripts to collect data on
the operation of the system.  The base systemtap package contains/requires
the components needed to locally develop and execute systemtap scripts.

# ------------------------------------------------------------------------

%package server
Summary: Instrumentation System Server
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-devel = %{version}-%{release}
Conflicts: systemtap-devel < %{version}-%{release}
Conflicts: systemtap-runtime < %{version}-%{release}
Conflicts: systemtap-client < %{version}-%{release}
Requires: nss coreutils
Requires: zip unzip
Requires(pre): shadow-utils
BuildRequires: nss-devel avahi-devel
%if %{with_openssl}
Requires: openssl
%endif
%if %{with_systemd}
Requires: systemd
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif
%description server
This is the remote script compilation server component of systemtap.
It announces itself to nearby clients with avahi (if available), and
compiles systemtap scripts to kernel objects on their demand.

%package devel
Summary: Programmable system-wide instrumentation system - development headers, tools
License: GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-only AND BSD-2-Clause
URL: https://sourceware.org/systemtap/
Requires: kernel-devel-uname-r
Requires: gcc make
Requires: elfutils-devel >= %{elfutils_version}
Conflicts: systemtap-client < %{version}-%{release}
Conflicts: systemtap-server < %{version}-%{release}
Conflicts: systemtap-runtime < %{version}-%{release}
%description devel
This package contains the components needed to compile a systemtap
script from source form into executable (.ko) forms.  It may be
installed on a self-contained developer workstation (along with the
systemtap-client and systemtap-runtime packages), or on a dedicated
remote server (alongside the systemtap-server package).  It includes
a copy of the standard tapset library and the runtime library C files.

%package runtime
Summary: Programmable system-wide instrumentation system - runtime
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires(pre): shadow-utils
Conflicts: systemtap-devel < %{version}-%{release}
Conflicts: systemtap-server < %{version}-%{release}
Conflicts: systemtap-client < %{version}-%{release}
%description runtime
SystemTap runtime contains the components needed to execute
a systemtap script that was already compiled into a module
using a local or remote systemtap-devel installation.

%package client
Summary: Programmable system-wide instrumentation system - client
License: GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-only AND GFDL-1.2-or-later AND BSD-2-Clause
URL: https://sourceware.org/systemtap/
Requires: zip unzip
Requires: systemtap-runtime = %{version}-%{release}
Requires: coreutils grep sed unzip zip
Requires: openssh-clients
Conflicts: systemtap-devel < %{version}-%{release}
Conflicts: systemtap-server < %{version}-%{release}
Conflicts: systemtap-runtime < %{version}-%{release}
%if %{with_mokutil}
Requires: mokutil
%endif
%description client
This package contains/requires only the components needed to
use systemtap scripts by compiling them using a local or a remote
systemtap-server service, then run them using a local or
remote systemtap-runtime.  It includes script samples and
documentation, and a copy of the tapset library for reference.
It does NOT include all the components for running a systemtap
script in a self-contained fashion; for that, use the -devel
subpackage instead.

%package initscript
Summary: Systemtap Initscripts
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap = %{version}-%{release}
%if %{with_systemd}
Requires: systemd
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif
%description initscript
This package includes a SysVinit script to launch selected systemtap
scripts at system startup, along with a dracut module for early
boot-time probing if supported.

%package sdt-devel
Summary: Static probe support header files
License: GPL-2.0-or-later AND CC0-1.0
URL: https://sourceware.org/systemtap/
%description sdt-devel
This package includes the <sys/sdt.h> header file used for static
instrumentation compiled into userspace programs.

%package sdt-dtrace
Summary: Static probe support dtrace tool
License: GPL-2.0-or-later AND CC0-1.0
URL: https://sourceware.org/systemtap/
Provides: dtrace = %{version}-%{release}
%if %{with_pyparsing}
%if %{with_python3}
Requires: python3-pyparsing
%else
Requires: python2-pyparsing
%endif
%endif
%description sdt-dtrace
This package includes the dtrace-compatibility preprocessor
to process related .d files into tracing-macro-laden .h headers.

%package testsuite
Summary: Instrumentation System Testsuite
License: GPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-or-later AND MIT
URL: https://sourceware.org/systemtap/
Requires: systemtap = %{version}-%{release}
Requires: systemtap-sdt-devel = %{version}-%{release}
Requires: systemtap-server = %{version}-%{release}
Requires: dejagnu which elfutils grep nc wget
%if %{with_debuginfod}
Requires: elfutils-debuginfod
%endif
%ifarch x86_64
Conflicts: systemtap-testsuite = %{version}-%{release}.i686
%endif
%ifarch i686
Conflicts: systemtap-testsuite = %{version}-%{release}.x86_64
%endif
Requires: gcc gcc-c++ make glibc-devel
Requires: strace
Requires: /usr/bin/nc
%ifnarch ia64 ppc64le aarch64
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
Requires: prelink
%endif
%endif
Requires: avahi
%if %{with_crash}
Requires: crash
%endif
%if %{with_java}
Requires: systemtap-runtime-java = %{version}-%{release}
%endif
%if %{with_python2_probes}
Requires: systemtap-runtime-python2 = %{version}-%{release}
%endif
%if %{with_python3_probes}
Requires: systemtap-runtime-python3 = %{version}-%{release}
%endif
%ifarch x86_64
Requires: /usr/lib/libc.so
%endif
Requires: perf
%description testsuite
This package includes the dejagnu-based systemtap stress self-testing
suite.  This may be used by system administrators to thoroughly check
systemtap on the current system.

%if %{with_java}
%package runtime-java
Summary: Systemtap Java Runtime Support
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-runtime = %{version}-%{release}
%ifarch x86_64
Conflicts: systemtap-runtime = %{version}-%{release}.i686
%endif
%ifarch i686
Conflicts: systemtap-runtime = %{version}-%{release}.x86_64
%endif
Requires: byteman > 2.0
Requires: iproute
Requires: java-devel
%description runtime-java
This package includes support files needed to run systemtap scripts
that probe Java processes running on the OpenJDK runtimes using Byteman.
%endif

%if %{with_python2_probes}
%package runtime-python2
Summary: Systemtap Python 2 Runtime Support
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-runtime = %{version}-%{release}
%description runtime-python2
This package includes support files needed to run systemtap scripts
that probe python 2 processes.
%endif

%if %{with_python3_probes}
%package runtime-python3
Summary: Systemtap Python 3 Runtime Support
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-runtime = %{version}-%{release}
%if ! (%{with_python2_probes})
Obsoletes: %{name}-runtime-python2 < %{version}-%{release}
%endif
%description runtime-python3
This package includes support files needed to run systemtap scripts
that probe python 3 processes.
%endif

%if %{with_python3_probes}
%package exporter
Summary: Systemtap-prometheus interoperation mechanism
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-runtime = %{version}-%{release}
%description exporter
This package includes files for a systemd service that manages
systemtap sessions and relays prometheus metrics from the sessions
to remote requesters on demand.
%endif

%if %{with_virtguest}
%package runtime-virtguest
Summary: Systemtap Cross-VM Instrumentation - guest
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap-runtime = %{version}-%{release}
%if %{with_systemd}
Requires(post): findutils coreutils
Requires(preun): grep coreutils
Requires(postun): grep coreutils
%else
Requires(post): chkconfig initscripts
Requires(preun): chkconfig initscripts
Requires(postun): initscripts
%endif
%description runtime-virtguest
This package installs the services necessary on a virtual machine for a
systemtap-runtime-virthost machine to execute systemtap scripts.
%endif

%package jupyter
Summary: ISystemtap jupyter kernel and examples
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Requires: systemtap = %{version}-%{release}
%description jupyter
This package includes files needed to build and run
the interactive systemtap Jupyter kernel, either locally
or within a container.

# ------------------------------------------------------------------------

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%if %{with_dyninst}
%global dyninst_config --with-dyninst
%else
%global dyninst_config --without-dyninst
%endif
%if %{with_Werror}
%global Werror_config --enable-Werror
%else
%global Werror_config --disable-Werror
%endif
%if %{with_sqlite}
%global sqlite_config --enable-sqlite
%else
%global sqlite_config --disable-sqlite
%endif
%if %{with_debuginfod}
%global debuginfod_config --with-debuginfod
%else
%global debuginfod_config --without-debuginfod
%endif
%if %{with_crash}
%global crash_config --enable-crash
%else
%global crash_config --disable-crash
%endif
%if %{with_rpm}
%global rpm_config --with-rpm
%else
%global rpm_config --without-rpm
%endif
%if %{with_docs}
%if %{with_htmldocs}
%global docs_config --enable-docs --enable-htmldocs
%else
%global docs_config --enable-docs --disable-htmldocs
%endif
%else
%global docs_config --enable-docs=prebuilt
%endif
%if %{with_java}
%global java_config --with-java=%{_jvmdir}/java
%else
%global java_config --without-java
%endif
%if %{with_python3}
%global python3_config --with-python3
%else
%global python3_config --without-python3
%endif
%if %{with_python2_probes}
%global python2_probes_config --with-python2-probes
%else
%global python2_probes_config --without-python2-probes
%endif
%if %{with_python3_probes}
%global python3_probes_config --with-python3-probes
%else
%global python3_probes_config --without-python3-probes
%endif
%global virt_config --disable-virt
%if %{with_dracut}
%global dracut_config --with-dracutstap=%{dracutstap} --with-dracutbindir=%{dracutbindir}
%else
%global dracut_config %{nil}
%endif
%if %{with_httpd}
%global httpd_config --enable-httpd
%else
%global httpd_config --disable-httpd
%endif
%if %{with_bpf}
%global bpf_config --with-bpf
%else
%global bpf_config --without-bpf
%endif
%global py_auto_byte_compile 0
%configure %{Werror_config} %{dyninst_config} %{sqlite_config} %{crash_config} %{docs_config} %{rpm_config} %{java_config} %{virt_config} %{dracut_config} %{python3_config} %{python2_probes_config} %{python3_probes_config} %{httpd_config} %{bpf_config} %{debuginfod_config} --disable-silent-rules --with-extra-version="rpm %{version}-%{release}"
make %{?_smp_mflags} V=1
%install
make DESTDIR=$RPM_BUILD_ROOT install
%if ! (%{with_python3})
rm -v $RPM_BUILD_ROOT%{_bindir}/stap-profile-annotate
%endif
%find_lang %{name}
for dir in $(ls -1d $RPM_BUILD_ROOT%{_mandir}/{??,??_??}) ; do
    dir=$(echo $dir | sed -e "s|^$RPM_BUILD_ROOT||")
    lang=$(basename $dir)
    echo "%%lang($lang) $dir/man*/*" >> %{name}.lang
done
%if %{with_sysusers}
mkdir -p %{buildroot}%{_sysusersdir}
echo '%_systemtap_runtime_preinstall' > %{buildroot}%{_sysusersdir}/systemtap-runtime.conf
echo '%_systemtap_server_preinstall' > %{buildroot}%{_sysusersdir}/systemtap-server.conf
echo '%_systemtap_testsuite_preinstall' > %{buildroot}%{_sysusersdir}/systemtap-testsuite.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
echo '%_systemtap_server_preinstall_tmpfiles' > %{buildroot}%{_tmpfilesdir}/systemtap-server.conf
%endif
ln -s %{_datadir}/systemtap/examples
find $RPM_BUILD_ROOT%{_datadir}/systemtap/examples -type f -name '*.stp' -print0 | xargs -0 sed -i -r -e '1s@^#!.+stap@#!%{_bindir}/stap@'
find testsuite -type f -name '.gitignore' -print0 | xargs -0 rm -f
chmod 755 $RPM_BUILD_ROOT%{_bindir}/staprun
cp -rp testsuite $RPM_BUILD_ROOT%{_datadir}/systemtap
mkdir docs.installed
mv $RPM_BUILD_ROOT%{_datadir}/doc/systemtap/*.pdf docs.installed/
%if %{with_docs}
%if %{with_htmldocs}
mv $RPM_BUILD_ROOT%{_datadir}/doc/systemtap/tapsets docs.installed/
mv $RPM_BUILD_ROOT%{_datadir}/doc/systemtap/SystemTap_Beginners_Guide docs.installed/
%endif
%endif
install -D -m 644 macros.systemtap $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.systemtap
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/stap-server
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/stap-server
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/stap-server/.systemtap
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/stap-server
touch $RPM_BUILD_ROOT%{_localstatedir}/log/stap-server/log
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/systemtap
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/systemtap
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 initscript/logrotate.stap-server $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/stap-server
%if %{with_systemd}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
touch $RPM_BUILD_ROOT%{_unitdir}/systemtap.service
mkdir -p $RPM_BUILD_ROOT%{_presetdir}
echo 'enable systemtap.service' > $RPM_BUILD_ROOT%{_presetdir}/42-systemtap.preset
install -m 644 initscript/systemtap.service $RPM_BUILD_ROOT%{_unitdir}/systemtap.service
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -m 755 initscript/systemtap $RPM_BUILD_ROOT%{_sbindir}/systemtap-service
%else
mkdir -p $RPM_BUILD_ROOT%{initdir}
install -m 755 initscript/systemtap $RPM_BUILD_ROOT%{initdir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{initdir}/systemtap $RPM_BUILD_ROOT%{_sbindir}/systemtap-service
%endif
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemtap
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemtap/conf.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemtap/script.d
install -m 644 initscript/config.systemtap $RPM_BUILD_ROOT%{_sysconfdir}/systemtap/config
%if %{with_systemd}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
touch $RPM_BUILD_ROOT%{_unitdir}/stap-server.service
install -m 644 stap-server.service $RPM_BUILD_ROOT%{_unitdir}/stap-server.service
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
install -m 644 stap-server.conf $RPM_BUILD_ROOT%{_tmpfilesdir}/stap-server.conf
%else
install -m 755 initscript/stap-server $RPM_BUILD_ROOT%{initdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/stap-server/conf.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 initscript/config.stap-server $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/stap-server
%endif
%if %{with_emacsvim}
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}
install -p -m 644 emacs/systemtap-mode.el* $RPM_BUILD_ROOT%{_emacs_sitelispdir}
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -p -m 644 emacs/systemtap-init.el $RPM_BUILD_ROOT%{_emacs_sitestartdir}/systemtap-init.el
for subdir in ftdetect ftplugin indent syntax
do
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/$subdir
    install -p -m 644 vim/$subdir/*.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/$subdir
done
%endif
%if %{with_virtguest}
   mkdir -p $RPM_BUILD_ROOT%{udevrulesdir}
   %if %{with_systemd}
      install -p -m 644 staprun/guest/99-stapsh.rules $RPM_BUILD_ROOT%{udevrulesdir}
      mkdir -p $RPM_BUILD_ROOT%{_unitdir}
      install -p -m 644 staprun/guest/stapsh@.service $RPM_BUILD_ROOT%{_unitdir}
   %else
      install -p -m 644 staprun/guest/99-stapsh-init.rules $RPM_BUILD_ROOT%{udevrulesdir}
      install -p -m 755 staprun/guest/stapshd $RPM_BUILD_ROOT%{initdir}
      mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/systemtap
      install -p -m 755 staprun/guest/stapsh-daemon $RPM_BUILD_ROOT%{_libexecdir}/systemtap
      mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/modules
      install -p -m 755 staprun/guest/virtio_console.modules $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/modules
   %endif
%endif
%if %{with_dracut}
   mkdir -p $RPM_BUILD_ROOT%{dracutstap}
   install -p -m 755 initscript/99stap/module-setup.sh $RPM_BUILD_ROOT%{dracutstap}
   install -p -m 755 initscript/99stap/install $RPM_BUILD_ROOT%{dracutstap}
   install -p -m 755 initscript/99stap/check $RPM_BUILD_ROOT%{dracutstap}
   install -p -m 755 initscript/99stap/start-staprun.sh $RPM_BUILD_ROOT%{dracutstap}
   touch $RPM_BUILD_ROOT%{dracutstap}/params.conf
%endif
%if %{with_specific_python}
%py3_shebang_fix %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with_check}
make check RUNTESTFLAGS=environment_sanity.exp
%endif
%pre runtime

%if %{with_sysusers}
%else
getent group stapusr >/dev/null || groupadd -f -g 156 -r stapusr
getent group stapsys >/dev/null || groupadd -f -g 157 -r stapsys
getent group stapdev >/dev/null || groupadd -f -g 158 -r stapdev
getent passwd stapunpriv >/dev/null || \
  useradd -c "Systemtap Unprivileged User" -u 159 -g stapunpriv -d %{_localstatedir}/lib/stapunpriv -r -s /sbin/nologin stapunpriv 2>/dev/null || \
  useradd -c "Systemtap Unprivileged User" -g stapunpriv -d %{_localstatedir}/lib/stapunpriv -r -s /sbin/nologin stapunpriv
exit 0
%endif
%pre server

%if %{with_sysusers}
%else
getent group stap-server >/dev/null || groupadd -f -g 155 -r stap-server
getent passwd stap-server >/dev/null || \
  useradd -c "Systemtap Compile Server" -u 155 -g stap-server -d %{_localstatedir}/lib/stap-server -r -s /sbin/nologin stap-server 2>/dev/null || \
  useradd -c "Systemtap Compile Server" -g stap-server -d %{_localstatedir}/lib/stap-server -r -s /sbin/nologin stap-server
exit 0
%endif
%pre testsuite

%if %{with_sysusers}
%else
getent passwd stapusr >/dev/null || \
    useradd -c "Systemtap 'stapusr' User" -g stapusr -r -s /sbin/nologin stapusr
getent passwd stapsys >/dev/null || \
    useradd -c "Systemtap 'stapsys' User" -g stapsys -G stapusr -r -s /sbin/nologin stapsys
getent passwd stapdev >/dev/null || \
    useradd -c "Systemtap 'stapdev' User" -g stapdev -G stapusr -r -s /sbin/nologin stapdev
exit 0
%endif
%post server

test -e ~stap-server && chmod 750 ~stap-server
if [ ! -f ~stap-server/.systemtap/rc ]; then
  mkdir -p ~stap-server/.systemtap
  chown stap-server:stap-server ~stap-server/.systemtap
  numcpu=`/usr/bin/getconf _NPROCESSORS_ONLN`
  if [ -z "$numcpu" -o "$numcpu" -lt 1 ]; then numcpu=1; fi
  nproc=`expr $numcpu \* 30`
  echo "--rlimit-as=4294967296 --rlimit-cpu=60 --rlimit-nproc=$nproc --rlimit-stack=1024000 --rlimit-fsize=51200000" > ~stap-server/.systemtap/rc
  chown stap-server:stap-server ~stap-server/.systemtap/rc
fi
test -e %{_localstatedir}/log/stap-server/log || {
     touch %{_localstatedir}/log/stap-server/log
     chmod 644 %{_localstatedir}/log/stap-server/log
     chown stap-server:stap-server %{_localstatedir}/log/stap-server/log
}
%if %{with_systemd}
     /bin/systemd-tmpfiles --create %{_tmpfilesdir}/stap-server.conf >/dev/null 2>&1 || :
%else
    /sbin/chkconfig --add stap-server
%endif
exit 0
%triggerin client -- systemtap-server

if test -e ~stap-server/.systemtap/ssl/server/stap.cert; then
   %{_libexecdir}/systemtap/stap-authorize-cert ~stap-server/.systemtap/ssl/server/stap.cert %{_sysconfdir}/systemtap/ssl/client >/dev/null
   %{_libexecdir}/systemtap/stap-authorize-cert ~stap-server/.systemtap/ssl/server/stap.cert %{_sysconfdir}/systemtap/staprun >/dev/null
fi
exit 0
%preun server

if [ $1 = 0 ] ; then
    %if %{with_systemd}
       /bin/systemctl --no-reload disable stap-server.service >/dev/null 2>&1 || :
       /bin/systemctl stop stap-server.service >/dev/null 2>&1 || :
    %else
        /sbin/service stap-server stop >/dev/null 2>&1
        /sbin/chkconfig --del stap-server
    %endif
fi
exit 0
%postun server

if [ "$1" -ge "1" ] ; then
    %if %{with_systemd}
        /bin/systemctl condrestart stap-server.service >/dev/null 2>&1 || :
    %else
        /sbin/service stap-server condrestart >/dev/null 2>&1 || :
    %endif
fi
exit 0
%post initscript

%if %{with_systemd}
%else
    /sbin/chkconfig --add systemtap
%endif
exit 0
%preun initscript

if [ $1 = 0 ] ; then
    %if %{with_systemd}
        /bin/systemctl --no-reload disable systemtap.service >/dev/null 2>&1 || :
        /bin/systemctl stop systemtap.service >/dev/null 2>&1 || :
    %else
        /sbin/service systemtap stop >/dev/null 2>&1
        /sbin/chkconfig --del systemtap
    %endif
fi
exit 0
%postun initscript

if [ "$1" -ge "1" ] ; then
    %if %{with_systemd}
        /bin/systemctl condrestart systemtap.service >/dev/null 2>&1 || :
    %else
        /sbin/service systemtap condrestart >/dev/null 2>&1 || :
    %endif
fi
exit 0
%post runtime-virtguest

%if %{with_systemd}
   if [ -d /dev/virtio-ports ]; then
      (find /dev/virtio-ports -iname 'org.systemtap.stapsh.[0-9]*' -type l \
         | xargs -n 1 basename \
         | xargs -n 1 -I {} /bin/systemctl start stapsh@{}.service) >/dev/null 2>&1 || :
   fi
%else
   /sbin/chkconfig --add stapshd
   /sbin/chkconfig stapshd on
   /sbin/service stapshd start >/dev/null 2>&1 || :
%endif
exit 0
%preun runtime-virtguest

if [ $1 = 0 ]; then
   %if %{with_systemd}
      for service in `/bin/systemctl --full | grep stapsh@ | cut -d ' ' -f 1`; do
         /bin/systemctl stop $service >/dev/null 2>&1 || :
      done
   %else
      /sbin/service stapshd stop >/dev/null 2>&1
      /sbin/chkconfig --del stapshd
   %endif
fi
exit 0
%postun runtime-virtguest

if [ "$1" -ge "1" ]; then
   %if %{with_systemd}
      for service in `/bin/systemctl --full | grep stapsh@ | cut -d ' ' -f 1`; do
         /bin/systemctl condrestart $service >/dev/null 2>&1 || :
      done
   %else
      /sbin/service stapshd condrestart >/dev/null 2>&1
   %endif
fi
exit 0
%if %{with_python3_probes}
%if %{with_systemd}
%preun exporter

if [ $1 = 0 ] ; then
  /bin/systemctl stop stap-exporter.service >/dev/null 2>&1 || :
  /bin/systemctl disable stap-exporter.service >/dev/null 2>&1 || :
fi
exit 0
%postun exporter

if [ "$1" -ge "1" ]; then
   /bin/systemctl condrestart stap-exporter >/dev/null 2>&1 || :
fi
exit 0
%endif
%endif
%post

(make -C %{_datadir}/systemtap/runtime/uprobes clean) >/dev/null 2>&1 || true
(/sbin/rmmod uprobes) >/dev/null 2>&1 || true
%preun

(make -C %{_datadir}/systemtap/runtime/uprobes clean) >/dev/null 2>&1 || true
(/sbin/rmmod uprobes) >/dev/null 2>&1 || true
%files -f %{oreon_filedir}/main.list
%files -n systemtap-server -f %{oreon_filedir}/systemtap-server.list
%files -n systemtap-devel -f %{oreon_filedir}/systemtap-devel.list
%files -n systemtap-runtime -f %{oreon_filedir}/systemtap-runtime.list
%files -n systemtap-client -f %{oreon_filedir}/systemtap-client.list
%files -n systemtap-initscript -f %{oreon_filedir}/systemtap-initscript.list
%files -n systemtap-sdt-devel -f %{oreon_filedir}/systemtap-sdt-devel.list
%files -n systemtap-sdt-dtrace -f %{oreon_filedir}/systemtap-sdt-dtrace.list
%files -n systemtap-testsuite -f %{oreon_filedir}/systemtap-testsuite.list
%files -n systemtap-runtime-python3 -f %{oreon_filedir}/systemtap-runtime-python3.list
%files -n systemtap-exporter -f %{oreon_filedir}/systemtap-exporter.list
%files -n systemtap-runtime-virtguest -f %{oreon_filedir}/systemtap-runtime-virtguest.list
%files -n systemtap-jupyter -f %{oreon_filedir}/systemtap-jupyter.list

%changelog

%autochangelog
