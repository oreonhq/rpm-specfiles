%global source0_hash 59ab7ce2877e211ab627350544b0c21cd639ee46191d0b0d804320e539c246b2
Summary:        The BOINC client
Name:          boinc-client
Version:       8.2.15
Release:        1%{?dist}
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://boinc.berkeley.edu/
%global major_version %(v=%{version}; echo ${v:0:3})
%global commit c0b8b6fd37687aa1b93102129a054837b84cc032
%global gittag client_release/%{major_version}/%{version}
%global gittag_custom client_release-%{major_version}-%{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/BOINC/boinc/archive/client_release/%{major_version}/%{version}/%{name}-%{version}.tar.gz
SOURCE1:       boinc-client-logrotate-d
SOURCE3:       36x11-common_xhost-boinc
SOURCE4:       config.properties
SOURCE5:       edu.berkeley.BOINC.metainfo.xml
Patch1:        disable_idle_time_detection.patch
Requires:         logrotate
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%if 0%{?el8}
ExcludeArch: s390x
%endif
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  docbook2X
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXmu-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  systemd-rpm-macros
BuildRequires:  wxGTK-devel
# /oreon:deps
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
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/Xsession.d/36x11-common_xhost-boinc
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/boinc-client/config.properties
install -p -m644 packages/generic/sea/boincmgr.16x16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/boincmgr.png
install -p -m644 packages/generic/sea/boincmgr.48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/boincmgr.png
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_metainfodir}/edu.berkeley.BOINC.metainfo.xml
%find_lang BOINC-Manager
%find_lang BOINC-Client
install -p -m644 client/scripts/boinc.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/boinc-client
install -m0644 -D boinc-client.sysusers.conf %{buildroot}%{_sysusersdir}/boinc-client.conf
%oreon_autofiles boinc-manager usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles boinc-client-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles boinc-client-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles boinc-client-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{?ldconfig}
%systemd_post boinc-client.service
%preun

%systemd_preun boinc-client.service
%postun

%{?ldconfig}
%systemd_postun_with_restart boinc-client.service  
%files -f %{oreon_filedir}/main.list
%files -n boinc-manager -f %{oreon_filedir}/boinc-manager.list
%files -n boinc-client-devel -f %{oreon_filedir}/boinc-client-devel.list
%files -n boinc-client-static -f %{oreon_filedir}/boinc-client-static.list
%files -n boinc-client-doc -f %{oreon_filedir}/boinc-client-doc.list

%changelog

%autochangelog
