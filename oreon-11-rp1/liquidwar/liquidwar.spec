%global source0_hash dad0aa84dd416cad055421ed9b40df39efae78d3df759c0583c64c54f7f2ff5f
Name:           liquidwar
Version:        6.0.6.3902
Release:        1%{?dist}
Summary:        Multiplayer wargame with liquid armies
License:        GPL-2.0-or-later
URL:            http://www.ufoot.org/liquidwar/v5
Source0:        http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source2:        liquidwar.sysconfig
Source3:        liquidwar.logrotate
Source4:        liquidwar-server.service
Patch0:         liquidwar-5.6.5-python3.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  allegro-devel
BuildRequires:  allegro-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd
# /oreon:deps
%description
Liquid War is a unique multiplayer wargame. You control an army of liquid
and have to try and eat your opponents. A single player mode is available,
but the game is definitely designed to be multiplayer, and has network
support.

%package doc
Summary:        Documentation for the LiquidWar game in additional formats
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains the documentation of LiquidWar in html, pdf, ps and txt
format.

%package server
Summary:        Network game server for the LiquidWar game
Requires:       %{name} = %{version}-%{release}
%description server
This package contains the server for hosting network LiquidWar games.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p0

# don't strip the binaries please
sed -i 's/install\(\s\+-c\)\?\s\+-s/install/g' Makefile.in
# fix README.* encoding
for i in de dk fr; do
  iconv -f ISO-8859-1 -t UTF8 README.$i > $i
  mv $i README.$i
done

# Create a sysusers.d config file
cat >liquidwar.sysusers.conf <<EOF
u liquidwar - 'LiquidWar Server' %{_datadir}/%{name} -
EOF

%build

%configure --disable-target-opt \
  --disable-doc-pdf \
  --disable-doc-ps \
  --disable-doc-info \
%ifnarch %{ix86}
  --disable-asm \
%endif
LDFLAGS="%{__global_ldflags}"
CFLAGS="$RPM_OPT_FLAGS -fcommon -std=gnu17"
LDFLAGS="$LDFLAGS -lm"
PYTHON="%{__python3}"
MAKE_FLAGS="DEBUG_FLAGS= GAMEDIR=%{_bindir} DATADIR=%{_datadir}/%{name}"
make config $MAKE_FLAGS LDFLAGS="$LDFLAGS" CFLAGS="$CFLAGS"
make %{?_smp_mflags} $MAKE_FLAGS LDFLAGS="$LDFLAGS" CFLAGS="$CFLAGS"
iconv -f ISO-8859-1 -t UTF8 doc/man/%{name}.6 | gzip > doc/man/%{name}.6.gz
gzip -cd doc/info/%{name}.info.gz | \
  iconv -f ISO-8859-1 -t UTF8 > doc/info/%{name}.info
gzip -f doc/info/%{name}.info
%install
make install_nolink DESTDIR=$RPM_BUILD_ROOT GAMEDIR=%{_bindir} \
  DATADIR=%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} liquidwardocs
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications        \
  --add-category StrategyGame                          \
  --remove-category Application                        \
  --remove-category ArcadeGame                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{32x32,48x48}/apps
install -p -m 644 misc/%{name}_32x32.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -p -m 644 misc/%{name}.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm
install -p -D -m 755 %{SOURCE4} \
        $RPM_BUILD_ROOT/%{_unitdir}/%{name}-server.service
install -p -D -m 644 %{SOURCE2} \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}-server
install -p -D -m 644 %{SOURCE3} \
        $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}-server
install -m0644 -D liquidwar.sysusers.conf %{buildroot}%{_sysusersdir}/liquidwar.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post liquidwar-server.service
%preun server

%systemd_post liquidwar-server.service
%postun server

%systemd_postun_with_restart liquidwar-server.service
%files -f %{oreon_filedir}/main.list
%files -n liquidwar-doc -f %{oreon_filedir}/liquidwar-doc.list
%files -n liquidwar-server -f %{oreon_filedir}/liquidwar-server.list

%changelog

%autochangelog
