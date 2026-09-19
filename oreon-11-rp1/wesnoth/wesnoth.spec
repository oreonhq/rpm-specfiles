%global source0_hash none

Name:           wesnoth
Version:        1.19.21
Release:        1%{?dist}
Summary:        Turn-based strategy game with a fantasy theme

License:        GPL-2.0-or-later
URL:            http://www.wesnoth.org
Source0:        http://www.%{name}.org/files/%{name}-%{version}.tar.bz2
Source1:        wesnothd.service
Source2:        %{name}.sysconfig
Patch0:         scons-env.patch

Requires:       wesnoth-data = %{version}
BuildRequires:  gcc-c++
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  dbus-devel
BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  fribidi-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  boost-devel
BuildRequires:  pango-devel
BuildRequires:  lua-devel
BuildRequires:  readline-devel
BuildRequires:  python3-scons
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  libvorbis-devel
BuildRequires:  libcurl-devel
BuildRequires:  systemd

%description
The Battle for Wesnoth is a turn-based strategy game with a fantasy theme.

Build up a great army, gradually turning raw recruits into hardened
veterans. In later games, recall your toughest warriors and form a deadly
host against whom none can stand. Choose units from a large pool of
specialists, and hand-pick a force with the right strengths to fight well
on different terrains against all manner of opposition.

Fight to regain the throne of Wesnoth, of which you are the legitimate
heir, or use your dread power over the Undead to dominate the land of
mortals, or lead your glorious Orcish tribe to victory against the humans
who dared despoil your lands. Wesnoth has many different sagas waiting to
be played out. You can create your own custom units, and write your own
scenarios--or even full-blown campaigns. You can also challenge your
friends--or strangers--and fight multi-player epic fantasy battles.

##%ifnarch noarch
%package server
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description server
This package contains the binaries for running a Wesnoth server
for multi-player games.

%package tools
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description tools
This package contains the game editor and development tools.

##%else
%package data
Summary:        %{summary}
Requires:       %{name} = %{version}
Requires:	dejavu-sans-fonts
BuildArch:      noarch

%description data
This package contains the data files for Wesnoth.
##%endif

%prep
%autosetup -p0

# Create a sysusers.d config file.
# Upstream provides a file that we don't like.
cat >wesnoth-server.sysusers.conf <<EOF
u wesnothd - 'Wesnoth server' /run/wesnothd -
EOF

%build
scons wesnoth wesnothd campaignd prefix=%{_prefix} \
          bindir=%{_bindir} \
          libdir=%{_libdir} \
          boostdir=%{_includedir} \
          boostlibdir=%{_libdir} \
          localedirname=locale \
          python_site_packages_dir=%{python3_sitelib}/wesnoth \
          extra_flags_release="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
          luadir=%{_includedir} \
          fifodir=/run/wesnothd \
          systemd=True \
          %{?_smp_mflags}

%install
scons install install-pytools destdir=$RPM_BUILD_ROOT

#Workaround for BZ 1981728
sed -i "s|@FIFO_DIR@|\/run\/wesnothd|g" $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf

#Correct user/group
sed -i "s/_wesnoth/wesnothd/g" $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf

%if 0%{?flatpak}
# Fix install paths for flatpak builds where systemd prefix differs from wesnoth prefix
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system/wesnothd.service $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf $RPM_BUILD_ROOT%{_tmpfilesdir}
%endif

# extra files we provide
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/wesnothd.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/wesnoth

# create this so we can %ghost it
mkdir -p ${RPM_BUILD_ROOT}/run/wesnothd/
touch ${RPM_BUILD_ROOT}/run/wesnothd/socket

%if "%{_sbindir}" != "%{_bindir}"
# move server stuff into sbindir
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
mv $RPM_BUILD_ROOT/%{_bindir}/wesnothd $RPM_BUILD_ROOT/%{_sbindir}
mv $RPM_BUILD_ROOT/%{_bindir}/campaignd $RPM_BUILD_ROOT/%{_sbindir}
%endif

# Wesnoth ships its own fonts, replace with Fedora packaged versions
for f in dejavu-sans-fonts/DejaVuSans-Bold.ttf dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf dejavu-sans-mono-fonts/DejaVuSansMono.ttf dejavu-sans-fonts/DejaVuSans-Oblique.ttf dejavu-sans-fonts/DejaVuSans.ttf ; do
    rm $RPM_BUILD_ROOT%{_datadir}/wesnoth/fonts/$(basename $f)
    ln -s /usr/share/fonts/$f $RPM_BUILD_ROOT%{_datadir}/wesnoth/fonts/$(basename $f)
done

# language stuff
%find_lang %{name} LANGFILES --with-man

install -m0644 -D wesnoth-server.sysusers.conf %{buildroot}%{_sysusersdir}/wesnoth-server.conf

%post server
%systemd_post wesnothd.service

%preun server
%systemd_preun wesnothd.service

%postun server
%systemd_postun_with_restart wesnothd.service

%files
%license COPYING
%doc changelog.md README.md copyright
%docdir %{_docdir}/wesnoth
%{_docdir}/wesnoth
%{_bindir}/%{name}

%files tools
%{_bindir}/wesnoth_addon_manager
%{_bindir}/wml*
%{python3_sitelib}/wesnoth
%{_datadir}/wesnoth/data/tools

%files server
%config(noreplace) %{_sysconfdir}/sysconfig/wesnoth
%{_sbindir}/wesnothd
%{_sbindir}/campaignd
%attr(0700,wesnothd,wesnothd) %dir /run/wesnothd/
%ghost /run/wesnothd/socket
%{_unitdir}/wesnothd.service
%{_tmpfilesdir}/wesnothd.tmpfiles.conf
%exclude %{_prefix}/lib/sysusers.d/wesnothd.sysusers.conf
%{_sysusersdir}/wesnoth-server.conf

%files data -f LANGFILES
%{_datadir}/applications/org.wesnoth.Wesnoth.desktop
%{_datadir}/icons/*
%{_datadir}/metainfo/org.wesnoth.Wesnoth.appdata.xml
%{_datadir}/wesnoth/
%exclude %{_datadir}/wesnoth/data/tools
%{_mandir}/man6/wesnoth*.6*
%{_mandir}/*/man6/wesnoth*.6*

%changelog
%autochangelog
