%global source0_hash 2c5912e6b9a5064710deb8bf059e5058eae26114f6065de79be586ac4c89513e

# correct the Obsoletes version in case of disabling it after being enabled
%global with_akonadi 0

Summary:       SyncML client for evolution
Name:          syncevolution
Epoch:         1
Version:       2.0.0
Release:       18%{?dist}
License:       LGPL-2.0-or-later
URL:           http://syncevolution.org/
Source:        http://downloads.syncevolution.org/%{name}/sources/%{name}-%{version}.tar.gz

Patch1:        syncevolution-1.5.1-libical2.patch
Patch2:        syncevolution-1.5.3-autoconf-2.71.patch
Patch3:        003-pcre2.patch
Patch4:        004-cpp-curl.patch
Patch5:        005-gcc-c23-changes.patch
Patch6:        006-evolution-data-server-3.59.1-api-change.patch

BuildRequires: pkgconfig(dbus-glib-1)

%if 0%{with_akonadi}
BuildRequires: pkgconfig(akonadi)
BuildRequires: kdelibs-devel
BuildRequires: kdepimlibs-devel
%else
Obsoletes: %{name}-libs-akonadi < 2.0.0-10
%endif

BuildRequires: perl-generators
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel >= 1.73.0
BuildRequires: cppunit-devel
BuildRequires: evolution-data-server-devel >= 3.45.1
BuildRequires: expat-devel
BuildRequires: glib2-devel
BuildRequires: gnome-online-accounts-devel
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libical-devel >= 2.0.0
BuildRequires: libnotify-devel
BuildRequires: neon-devel
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: python3
BuildRequires: python3-docutils
BuildRequires: python3-pygments
BuildRequires: unique3-devel
%ifnarch s390 s390x
BuildRequires: openobex-devel
%endif

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: make
BuildRequires: systemd

Requires: python3-dbus
Requires: python3-twisted

%description
syncevolution is designed to provide a SyncML client that can
connect to and sync with various SyncML-based servers

%package libs
Summary: Library package for %{name}

%description libs
Libraries for %{name}.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package gtk
Summary: GTK+ GUI for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description gtk
GTK+ GUI for use with %{name}.

%package perl
Summary: Perl utils for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description perl
Perl utils for use with %{name}.

%if 0%{with_akonadi}
%package libs-akonadi
Summary: Akonadi backend package for %{name}

%description libs-akonadi
Akonadi backend for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -S gendiff

# use the ac macros in Makefile.am
sed -i '/^ACLOCAL_AMFLAGS/{ /m4-repo/!s/$/ -I m4-repo/ }' Makefile*.am

%build
autoupdate
intltoolize --automake --copy --force
autoreconf -fiv

pushd src/synthesis
autoupdate
autoreconf -fi
./autogen.sh
popd

%configure --enable-libcurl --disable-libsoup --enable-dbus-service --enable-shared \
    --disable-static --enable-gtk=3 --enable-gui --with-gio-gdbus \
    --enable-dav --disable-static --enable-gtk=3 --enable-gui \
    --enable-gnome-keyring --enable-pbap \
%if 0%{with_akonadi}
     --enable-akonadi \
%else
     --disable-akonadi \
%endif
%ifnarch s390 s390x
    --enable-bluetooth
%else
    --disable-bluetooth
%endif

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g
	s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1
find . -type d -perm 02755 -exec chmod 0755 '{}' \;

%install
make install DESTDIR=%{buildroot} docdir=%{_docdir}
rm -rf %{buildroot}%{_datadir}/doc

# even the build is disabled, there is still created the file with some minimal content
%if !0%{with_akonadi}
rm %{buildroot}%{_libdir}/syncevolution/backends/syncakonadi.so
%endif

#Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/sync.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS README HACKING README.html README.rst
%{_sysconfdir}/xdg/autostart/syncevo-dbus-server.desktop
%{_userunitdir}/syncevo-dbus-server.service
%{_bindir}/syncevolution
%{_bindir}/syncevo-http-server
%{_bindir}/syncevo-phone-config
%{_bindir}/syncevo-webdav-lookup
%{_bindir}/synclog2html
%{_libexecdir}/syncevo-dbus-helper
%{_libexecdir}/syncevo-dbus-server
%{_libexecdir}/syncevo-dbus-server-startup.sh
%{_libexecdir}/syncevo-local-sync
%{_datadir}/syncevolution
%{_datadir}/dbus-1/services/org.syncevolution.service
%{_datadir}/man/man1/syncevolution.1.gz
%exclude %{_datadir}/syncevolution/xml/*.pl

%files libs
%doc COPYING LICENSE.LGPL-21 LICENSE.txt
%{_libdir}/*so.0*
%dir %{_libdir}/syncevolution
%{_libdir}/syncevolution/backends/platformgnome.so
%{_libdir}/syncevolution/backends/platformkde.so
%{_libdir}/syncevolution/backends/platformtde.so
%{_libdir}/syncevolution/backends/providergoa.so
%{_libdir}/syncevolution/backends/syncactivesync.so
%{_libdir}/syncevolution/backends/syncdav.so
%{_libdir}/syncevolution/backends/syncebook.so
%{_libdir}/syncevolution/backends/syncecal.so
%{_libdir}/syncevolution/backends/syncfile.so
%{_libdir}/syncevolution/backends/synckcalextended.so
%{_libdir}/syncevolution/backends/syncmaemocal.so
%{_libdir}/syncevolution/backends/syncpbap.so
%{_libdir}/syncevolution/backends/syncqtcontacts.so
%{_libdir}/syncevolution/backends/syncsqlite.so
%{_libdir}/syncevolution/backends/synctdepimabc.so
%{_libdir}/syncevolution/backends/synctdepimcal.so
%{_libdir}/syncevolution/backends/synctdepimnotes.so
%{_libdir}/syncevolution/backends/syncxmlrpc.so

%if 0%{with_akonadi}
%files libs-akonadi
%{_libdir}/syncevolution/backends/syncakonadi.so
%endif

%files devel
%{_includedir}/syncevo
%{_includedir}/syncevo-dbus
%{_includedir}/synthesis
%{_libdir}/pkgconfig/s*.pc
%{_libdir}/*.so
%{_libdir}/*.a

%files gtk
%{_bindir}/sync-ui
%{_datadir}/applications/sync.desktop
%{_datadir}/icons/hicolor/48x48/apps/sync.png

%files perl
%{_bindir}/synccompare
%{_datadir}/syncevolution/xml/*.pl

%changelog
%autochangelog
