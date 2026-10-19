%global source0_hash 2c5912e6b9a5064710deb8bf059e5058eae26114f6065de79be586ac4c89513e
%global with_akonadi 0
Summary:        SyncML client for evolution
Name:          syncevolution
Epoch:         1
Version:       2.0.0
Release:        1%{?dist}
License:       LGPL-2.0-or-later
URL:           http://syncevolution.org/
Source0:        http://downloads.syncevolution.org/%{name}/sources/%{name}-%{version}.tar.gz
Patch1:        syncevolution-1.5.1-libical2.patch
Patch2:        syncevolution-1.5.3-autoconf-2.71.patch
Patch3:        003-pcre2.patch
Patch4:        004-cpp-curl.patch
Patch5:        005-gcc-c23-changes.patch
Patch6:        006-evolution-data-server-3.59.1-api-change.patch
%if 0%{with_akonadi}
%else
Obsoletes: %{name}-libs-akonadi < 2.0.0-10
%endif
%ifnarch s390 s390x
%endif
Requires: python3-dbus
Requires: python3-twisted
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  boost-devel
BuildRequires:  cppunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  evolution-data-server-devel
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libical-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  neon-devel
BuildRequires:  openobex-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  python3
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  systemd
BuildRequires:  unique3-devel
# /oreon:deps
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
%if !0%{with_akonadi}
rm %{buildroot}%{_libdir}/syncevolution/backends/syncakonadi.so
%endif
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/sync.desktop
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n syncevolution-libs -f %{oreon_filedir}/syncevolution-libs.list
%files -n syncevolution-devel -f %{oreon_filedir}/syncevolution-devel.list
%files -n syncevolution-gtk -f %{oreon_filedir}/syncevolution-gtk.list
%files -n syncevolution-perl -f %{oreon_filedir}/syncevolution-perl.list

%changelog

%autochangelog
