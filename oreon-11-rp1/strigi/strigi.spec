
## include clucene support (not used since fedora 15)
#global clucene 1

Name:		strigi
Summary:        A desktop search program
Version:	0.7.8
Release:	11%{?dist}

License:	LGPL-2.0-or-later
#URL:            https://projects.kde.org/projects/kdesupport/strigi
URL:            http://www.vandenoever.info/software/strigi/
Source0:	https://www.vandenoever.info/software/strigi/strigi-%{version}%{?pre:-%{pre}}.tar.bz2
#Source0:	http://rdieter.fedorapeople.org/strigi/strigi-%{version}%{?pre:-%{pre}}.tar.xz
Source1:	strigiclient.desktop
Source2:	strigi-daemon.desktop

## upstream patches
Patch11: libstreamanalyzer-0001-Fix-for-non-valid-values-in-Exif-field-ISOSpeedRatin.patch
Patch12: libstreamanalyzer-0002-order-matters-for-systems-that-have-things-already-i.patch
Patch13: libstreamanalyzer-0003-Fix-Krazy-issues.patch
Patch14: libstreamanalyzer-0004-ffmpeg-Rename-mutex-to-g_mutex.patch
Patch15: libstreamanalyzer-0005-use-rpath-only-when-needed.patch
Patch21: libstreams-0001-Generate-config.h-after-looking-for-dependencies.patch
Patch22: libstreams-0002-Reduce-noise-in-analysis-tools-complain-about-resour.patch
Patch23: libstreams-0003-Build-fix-for-gcc-4.8.patch
Patch24: libstreams-0004-Fix-Krazy-issues.patch
Patch25: libstreams-0005-use-rpath-only-when-needed.patch
Patch31: strigiclient-0001-use-rpath-only-when-needed.patch
Patch41: strigidaemon-0001-Fix-Krazy-issues.patch
Patch42: strigidaemon-0002-use-rpath-only-when-needed.patch
Patch51: strigiutils-0001-use-rpath-only-when-needed.patch

BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:	cmake >= 2.4.5
%if 0%{?clucene:1}
BuildRequires:	clucene-core-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(dbus-1) dbus-x11
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gamin)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(QtDBus) pkgconfig(QtGui)
BuildRequires:  pkgconfig(zlib)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Strigi is a fast and light desktop search engine. It can handle a large range
of file formats such as emails, office documents, media files, and file
archives. It can index files that are embedded in other files. This means email
attachments and files in zip files are searchable as if they were normal files
on your harddisk.

Strigi is normally run as a background daemon that can be accessed by many
other programs at once. In addition to the daemon, Strigi comes with powerful
replacements for the popular unix commands 'find' and 'grep'. These are called
'deepfind' and 'deepgrep' and can search inside files just like the strigi
daemon can.

%package	devel
Summary:	Development files for the strigi desktop search engine
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
Development files for the strigi desktop search engine

%package	libs
Summary:	Strigi libraries
%description	libs
Strigi search engine libraries


%prep
%setup -q -n %{name}-%{version}%{?pre:-%{pre}}

pushd libstreamanalyzer
%patch11 -p1 -b .11
%patch12 -p1 -b .12
%patch13 -p1 -b .13
%patch14 -p1 -b .14
%patch15 -p1 -b .15
popd
pushd libstreams
%patch21 -p1 -b .21
%patch22 -p1 -b .22
%patch23 -p1 -b .23
%patch24 -p1 -b .24
%patch25 -p1 -b .25
popd
pushd strigiclient
%patch31 -p1 -b .31
popd
pushd strigidaemon
%patch41 -p1 -b .41
%patch42 -p1 -b .42
popd
pushd strigiutils
%patch51 -p1 -b .51
popd


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
%if ! 0%{?clucene:1}
  -DENABLE_CLUCENE:BOOL=OFF \
  -DENABLE_CLUCENE_NG:BOOL=OFF \
%endif
  -DENABLE_DBUS:BOOL=ON \
  -DENABLE_FAM:BOOL=ON \
  -DENABLE_FFMPEG:BOOL=OFF \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast -C %{_target_platform}  DESTDIR=%{buildroot}

desktop-file-install \
  --vendor="%{?dt_vendor}" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Add an autostart desktop file for the strigi daemon
install -p -m644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/autostart/strigi-daemon.desktop


%check
export CTEST_OUTPUT_ON_FAILURE=1
# make non-fatal, some failures on big-endian archs
make test -C %{_target_platform} ||:


%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*
%{_datadir}/applications/*strigiclient.desktop
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/xdg/autostart/strigi-daemon.desktop
%if 0%{?clucene}
%{_libdir}/strigi/strigiindex_clucene.so
%endif

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libstreamanalyzer.pc
%{_libdir}/pkgconfig/libstreams.pc
%dir %{_libdir}/cmake/
%{_libdir}/cmake/Strigi/
%{_libdir}/cmake/LibSearchClient/
%{_libdir}/cmake/LibStreamAnalyzer/
%{_libdir}/cmake/LibStreams/
%{_includedir}/strigi/

%files libs
%{_datadir}/strigi/
%{_libdir}/libsearchclient.so.0*
%{_libdir}/libstreamanalyzer.so.0*
%{_libdir}/libstreams.so.0*
%{_libdir}/libstrigihtmlgui.so.0*
%{_libdir}/libstrigiqtdbusclient.so.0*
%dir %{_libdir}/strigi/
%{_libdir}/strigi/strigiea_*.so
%{_libdir}/strigi/strigila_*.so
%{_libdir}/strigi/strigita_*.so


%changelog
* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.8-11
- Import from Fedora 23 dist-git (provides libstreams), debrand
