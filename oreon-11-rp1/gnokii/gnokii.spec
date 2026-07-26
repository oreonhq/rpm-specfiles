%global source0_hash 8f5a083b05c1a66a3402ca5cd80084e14c2c0632c991bb53b03c78e9adb02501

%global _hardened_build 1
# TODO: merge patches upstream where applicable

Name:           gnokii
Version:        0.6.31
Release:        47%{?dist}
Summary:        Linux/Unix tool suite for various mobile phones

License:        GPL-2.0-or-later
URL:            https://www.gnokii.org/
Source0:        https://www.gnokii.org/download/gnokii/%{name}-%{version}.tar.bz2
Source2:        %{name}-smsd.service
Source3:        %{name}-smsd.sysconfig
Source4:        %{name}-smsd.logrotate
Source5:        %{name}-smsd2mail.sh
Source6:        %{name}-smsd-README.smsd2mail
# Patch to make gnokii use "htmlview" instead of "mozilla" as default browser
Patch0:         %{name}-htmlview.patch
# Patch to remove port locking and apply the system-wide /usr/sbin directory
# to the path instead of the default /usr/local
Patch1:         %{name}-config.patch
Patch2:         %{name}-0.6.31-sqlite3.patch
Patch3:         %{name}-0.6.31-gcc5.patch
Patch4:         %{name}-0.6.31-gcc7.patch
Patch5: gnokii-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  libpq-devel
%else
BuildRequires:  postgresql-devel
%endif
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires:  bluez-libs-devel
%if 0%{?fedora} >= 37 || 0%{?rhel} > 9
BuildRequires:  libusb-compat-0.1-devel
%else
BuildRequires:  libusb-devel
%endif
BuildRequires:  libical-devel >= 0.24
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel 
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  perl(XML::Parser) intltool
BuildRequires:  make
BuildRequires:  chrpath

%description
Gnokii provides tools and a user space driver for use with mobile
phones under Linux, various unices and Win32. With gnokii you can do
such things as make data calls, update your address book, change
calendar entries, send and receive SMS messages and load ring tones
depending on the phone you have.

%package     -n xgnokii
Summary:        Graphical Linux/Unix tool suite for various mobile phones
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n xgnokii
Xgnokii is graphical Linux/Unix tool suite for various mobile
phones. It allows you to edit your contacts book, send/read SMS's
from/in computer and more other features.

%package        smsd
Summary:        Gnokii SMS daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  systemd

%description    smsd
The Gnokii SMS daemon receives and sends SMS messages.

%package        smsd-pgsql
Summary:        PostgreSQL support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-smsd-postgresql < 0.6.4-0.lvn.2

%description    smsd-pgsql
%{summary}.

%package        smsd-mysql
Summary:        MySQL support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}

%description    smsd-mysql
%{summary}.

%package        smsd-sqlite
Summary:        SQLite support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}

%description    smsd-sqlite
%{summary}.

%package        devel
Summary:        Gnokii development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%patch0 -p0
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
install -pm 644 %{SOURCE5} smsd2mail.sh
install -pm 644 %{SOURCE6} README.smsd2mail

# Create sysusers.d config files
cat >gnokii.sysusers.conf <<EOF
g gnokii -
EOF
cat >gnokii-smsd.sysusers.conf <<EOF
u gnokii - "Gnokii system user" - -
EOF

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --enable-security --disable-static --disable-rpath
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' -i libtool
sed -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' -i libtool
%make_build
pushd xgnokii
%make_build
popd 

%install
%make_install

# Rename smsd to gnokii-smsd
mv $RPM_BUILD_ROOT%{_bindir}/{,gnokii-}smsd
mv $RPM_BUILD_ROOT%{_mandir}/man8/{,gnokii-}smsd.8
sed -i 's,smsd ,gnokii-smsd ,' $RPM_BUILD_ROOT%{_mandir}/man8/gnokii-smsd.8
sed -i 's,smsd.,gnokii-smsd.,' $RPM_BUILD_ROOT%{_mandir}/man8/gnokii-smsd.8

# Remove libtool droppings
rm $RPM_BUILD_ROOT%{_libdir}{,/smsd}/lib*.la

# Fix up the default desktop file
desktop-file-install \
  --delete-original \
  --vendor "" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  --add-category X-Fedora \
  xgnokii/xgnokii.desktop

install -D -m 755 xgnokii/.libs/xgnokii $RPM_BUILD_ROOT%{_bindir}

install -D -m 644 common/gnokii.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gnokii.pc
install -D -m 644 xgnokii/xgnokii.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/xgnokii.pc

# Convert the default icons to PNG
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert Docs/sample/logo/gnokii.xpm \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/xgnokii.png
chmod 644 $RPM_BUILD_ROOT%{_datadir}/pixmaps/xgnokii.png

# Install the configuration files
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/gnokii-smsd.service
install -Dpm 640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/gnokii-smsd
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/gnokii-smsd
cp -a Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/

# Install the docs
mv $RPM_BUILD_ROOT%{_datadir}/doc/gnokii/ temporary-gnokii-docs/

# Use last resort to remove -rpath usage that can't be removed from Makefiles
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/{gnokii,gnokiid,gnokii-smsd,xgnokii}

install -m0644 -D gnokii.sysusers.conf %{buildroot}%{_sysusersdir}/gnokii.conf
install -m0644 -D gnokii-smsd.sysusers.conf %{buildroot}%{_sysusersdir}/gnokii-smsd.conf

%find_lang %{name}

%ldconfig_scriptlets

%post smsd
%systemd_post gnokii-smsd.service

%preun smsd
%systemd_preun gnokii-smsd.service

%postun smsd
%systemd_postun_with_restart gnokii-smsd.service

%files -f %{name}.lang
%license COPY*
%doc ChangeLog MAINTAINERS TODO temporary-gnokii-docs/*
%config(noreplace) %{_sysconfdir}/gnokiirc
%attr(4750,root,gnokii) %{_sbindir}/mgnokiidev
%{_bindir}/gnokii
%{_bindir}/sendsms
%{_bindir}/gnokiid
%{_libdir}/libgnokii.so.*
%{_mandir}/man1/gnokii.1*
%{_mandir}/man1/sendsms.1*
%{_mandir}/man8/gnokiid.8*
%{_mandir}/man8/mgnokiidev.8*
%{_sysusersdir}/gnokii.conf

%files -n xgnokii
%doc xgnokii/ChangeLog xgnokii/README.vcard
%{_bindir}/xgnokii
%{_datadir}/pixmaps/xgnokii.png
%{_datadir}/applications/*xgnokii.desktop
%{_mandir}/man1/xgnokii.1*

%files smsd
%doc smsd/action smsd/ChangeLog smsd/README README.smsd2mail smsd2mail.sh
%attr(-,gnokii,gnokii) %config(noreplace) %{_sysconfdir}/sysconfig/gnokii-smsd
%config(noreplace) %{_sysconfdir}/logrotate.d/gnokii-smsd
%{_unitdir}/gnokii-smsd.service
%{_bindir}/gnokii-smsd
%{_mandir}/man8/gnokii-smsd.8*
%dir %{_libdir}/smsd/
%{_libdir}/smsd/libsmsd_file.so
%{_sysusersdir}/gnokii-smsd.conf

%files smsd-pgsql
%doc smsd/sms.tables.pq.sql
%{_libdir}/smsd/libsmsd_pq.so

%files smsd-mysql
%doc smsd/sms.tables.mysql.sql
%{_libdir}/smsd/libsmsd_mysql.so

%files smsd-sqlite
%doc smsd/sms.tables.sqlite.sql
%{_libdir}/smsd/libsmsd_sqlite.so

%files devel
%{_includedir}/gnokii*
%{_libdir}/libgnokii.so
%{_libdir}/pkgconfig/gnokii.pc
%{_libdir}/pkgconfig/xgnokii.pc

%changelog
%autochangelog
