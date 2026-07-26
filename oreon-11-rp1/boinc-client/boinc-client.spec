%global source0_hash none

# ========== README ==========
#
# BOINC client is not released with Github releases, it is released using
# Github tags.
# When a new BOINC client Github tag is released, replace
# 1) Version
# 2) Release (obviously)
# 3) commit, you can take it from the URL you get on Github when you pass the
# mousepointer on shortcommit (7 chars string)
# 
# BOINC release URLs are troublesome, to download the tar.gz use the following command
# spectool -g -s 0 boinc-client.spec
#
# Do not move the %%global foo block of code in the upper part of the spec
# file, otherwise it will not work because it will try to read macros not
# yet defined like %%{version}

Summary:       The BOINC client
Name:          boinc-client
Version:       8.2.4
Release:       3%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://boinc.berkeley.edu/

%global major_version %(v=%{version}; echo ${v:0:3})
%global commit c0b8b6fd37687aa1b93102129a054837b84cc032
%global gittag client_release/%{major_version}/%{version}
# gittag_custom is needed in %%setup process because tar.gz unpacks a folder
# named for example boinc-client_release-7.14-7.14.2
%global gittag_custom client_release-%{major_version}-%{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Source0:       https://github.com/BOINC/boinc/archive/%{gittag}/%{name}-%{version}.tar.gz
SOURCE1:       boinc-client-logrotate-d
SOURCE3:       36x11-common_xhost-boinc
SOURCE4:       config.properties
SOURCE5:       edu.berkeley.BOINC.metainfo.xml
%if 0%{?fedora} > 35
#Patch0:        openssl3.patch
%endif
Patch1:        disable_idle_time_detection.patch
# On Linux distributions, BOINC runs as a service. Users must not be able to
# try stopping the service from exit menu entry.
# This leads to unexpected behaviour, like:
# - service being killed;
# - service still running.
# Moreover, the Manager will no longer be able to connect to the client, unless
# the user connects to 127.0.0.1. Then if the Manager is connected to the client
# by using 127.0.0.1 address, the "Exit from BOINC Manager" entry will not
# show any frame asking the user if he wants to stop the service.
# upstream pull request https://github.com/BOINC/boinc/pull/3094 has ben merged
# and unmerged later
#Patch4:        manager_exit_menu_entry_removal.patch

Requires:         logrotate
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%if ! ((%{defined rhel} && 0%{?rhel} >= 10) || (%{defined fedora} && 0%{?fedora} >= 42))
Requires(pre):    shadow-utils
%endif

BuildRequires: curl-devel
BuildRequires: freeglut-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk3-devel
BuildRequires: docbook2X
BuildRequires: libXmu-devel
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libnotify)
BuildRequires: libtool
%if ! (%{defined rhel} && 0%{?rhel} >= 10)
BuildRequires: libXScrnSaver-devel
%endif
BuildRequires: mesa-libGLU-devel
BuildRequires: pkgconfig(openssl)
%if %{defined fedora} && 0%{?fedora} > 40
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
#
# We have raised the possibility of removing OpenSSL engine support upstream:
#   Remove OpenSSL engine support
#   https://github.com/BOINC/boinc/pull/5991
# However, it’s difficult to test this thoroughly, so it makes sense to wait
# for upstream feedback and/or for the next major-version update before
# patching this downstream. For now, we just add the necessary BuildRequires to
# keep supporting engines.
BuildRequires: openssl-devel-engine
%endif
%if %{defined fedora}
BuildRequires: pkgconfig(sqlite)
%else
BuildRequires: sqlite-devel
%endif
BuildRequires: systemd-rpm-macros
BuildRequires: wxGTK-devel
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(libunwind)
BuildRequires: make

# EPEL8 webkit2gtk3 is missing for s390x, aarch64
%if 0%{?el8}
ExcludeArch: s390x
%endif
%description 
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs the BOINC client software, which will allow your
computer to participate in one or more BOINC projects, using your spare
computer time to search for cures for diseases, model protein folding, study
global warming, discover sources of gravitational waves, and many other types
of scientific and mathematical research.

%package -n boinc-manager
Summary:    GUI to control and monitor %{name}
Requires:   hicolor-icon-theme
Requires:   %{name} = %{version}-%{release}

%description -n boinc-manager
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   openssl-devel
Requires:   mariadb-connector-c-devel

%description devel
This package contains development files for %{name}.

%package static
Summary:    Static libraries for %{name}
Requires:   %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for %{name}.

%package doc
Summary:    Documentation files for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n boinc-%{gittag_custom}

# Fix encoding
for file in $(ls | grep checkin_notes_20); do
    iconv -f ISO-8859-1 -t UTF-8 -o ${file}.utf8 ${file}
    mv ${file}.utf8 ${file}
done

# Fix file permissions
for file in $(ls clientgui | grep .cpp$ ) $(ls clientgui | grep .h$ ); do 
    chmod 644 clientgui/${file}
done

# Create a sysusers.d config file
cat >boinc-client.sysusers.conf <<EOF
u boinc - 'BOINC client account.' %{_localstatedir}/lib/boinc -
EOF

%build

%ifarch %{ix86}
%global boinc_platform i686-pc-linux-gnu
%endif
%ifarch powerpc ppc
%global boinc_platform powerpc-linux-gnu
%endif
%ifarch powerpc64 ppc64
%global boinc_platform ppc64-linux-gnu
%endif
%ifarch aarch64
%global boinc_platform aarch64-unknown-linux-gnu
%endif

%if %{defined boinc_platform}
%global confflags --with-boinc-platform=%{boinc_platform}
%endif

./_autosetup

%configure %{?confflags} \
  --disable-silent-rules \
  --enable-dynamic-client-linkage \
  --disable-server \
  --disable-fcgi \
  --enable-unicode \
  --with-wx-config=/usr/bin/wx-config-3.2 \
  --with-ssl \
  --with-x \
  STRIP=: \
  DOCBOOK2X_MAN=/usr/bin/db2x_docbook2man \
  "CXXFLAGS=$(pkg-config gtk+-x11-3.0 --cflags --libs) ${RPM_OPT_FLAGS} -DNDEBUG"

# Disable rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/boinc
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xsession.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/boinc-client

make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT

# Set up links to correct log locations
#ln -s /var/log/boinc/ %%{_localstatedir}/log/boinc.log 
#ln -s /var/log/boinc/ %%{_localstatedir}/log/boincerr.log 

# Remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# Use custom systemd script and logrotate configuration file
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xsession.d/36x11-common_xhost-boinc
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/boinc-client/config.properties

# Install Icons
install -p -m644 packages/generic/sea/boincmgr.16x16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png

# Install AppStream metainfo file
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_metainfodir}/edu.berkeley.BOINC.metainfo.xml

%find_lang BOINC-Manager
%find_lang BOINC-Client

# bash-completion
install -p -m644 client/scripts/boinc.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/boinc-client

install -m0644 -D boinc-client.sysusers.conf %{buildroot}%{_sysusersdir}/boinc-client.conf

%if ! (0%{?fedora} >= 42 || 0%{?rhel} >= 10)
# Create BOINC user and group
getent group boinc >/dev/null || groupadd -r boinc
getent passwd boinc >/dev/null || \
useradd -r -g boinc -d %{_localstatedir}/lib/boinc -s /sbin/nologin \
    -c "BOINC client account." boinc
exit 0
%endif

%post
%{?ldconfig}
%systemd_post boinc-client.service

%preun
%systemd_preun boinc-client.service

%postun
%{?ldconfig}
%systemd_postun_with_restart boinc-client.service  

%if 0%{?rhel} && 0%{?rhel} <= 7
%post -nboinc-manager
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n boinc-manager
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans -n boinc-manager
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files -f BOINC-Client.lang
%doc COPYING COPYRIGHT
%{_bindir}/boinc
%{_bindir}/boinc_client
%{_bindir}/boinccmd
#%{_bindir}/switcher
%{_unitdir}/%{name}.service
%{_mandir}/man1/boinccmd.1.gz
%{_mandir}/man1/boinc.1.gz
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/logrotate.d/boinc-client
%config(noreplace) %{_sysconfdir}/bash_completion.d/boinc-client
%attr(-,boinc,boinc) %{_localstatedir}/lib/boinc/
%{_sysconfdir}/X11/Xsession.d/36x11-common_xhost-boinc
%{_sysconfdir}/boinc-client/config.properties
%{_sysusersdir}/boinc-client.conf

%files doc
%doc checkin_notes checkin_notes_*

%files -n boinc-manager -f BOINC-Manager.lang
%{_bindir}/boincmgr
%{_bindir}/boincscr
%{_datadir}/applications/boinc.desktop
%{_metainfodir}/edu.berkeley.BOINC.metainfo.xml
%{_datadir}/boinc-manager/skins/*
%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png
%{_datadir}/icons/hicolor/64x64/apps/boinc.png
%{_datadir}/icons/hicolor/scalable/apps/boinc.svg
%{_mandir}/man1/boincmgr.1.gz

%files static
%{_libdir}/libboinc.a
%{_libdir}/libboinc_api.a
%{_libdir}/libboinc_crypt.a
%{_libdir}/libboinc_graphics2.a
%{_libdir}/libboinc_opencl.a

%files devel
%{_libdir}/*.so
%{_includedir}/boinc
%{_libdir}/pkgconfig/libboinc.pc
%{_libdir}/pkgconfig/libboinc_api.pc
%{_libdir}/pkgconfig/libboinc_crypt.pc
%{_libdir}/pkgconfig/libboinc_graphics2.pc
%{_libdir}/pkgconfig/libboinc_opencl.pc

%changelog
%autochangelog
