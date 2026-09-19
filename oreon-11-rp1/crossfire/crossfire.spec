%global source0_hash 016ee33b15879a96e14932a9209d03ee9e3da69b3f3bd6b82c800f43345f064d

%define _hardened_build 1
%define selinux_variants mls strict targeted
%global selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)

%define logwatch_root %{_datadir}/logwatch
%define logwatch_conf %{logwatch_root}/dist.conf
%define logwatch_scripts %{logwatch_root}/scripts

Name: crossfire
Version: 1.71.0
Release: 35%{?dist}
Summary: Server for hosting crossfire games
# All files GPLv2+ except server/daemon.c which also has MIT attributions
License: GPL-2.0-or-later and MIT
URL: http://crossfire.real-time.com

Source0: http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.bz2
Source1: http://downloads.sourceforge.net/crossfire/%{name}-%{version}.arch.tar.bz2
Source2: crossfire.service
Source3: crossfire.sysconfig
Source4: crossfire.logrotate
Source5: crossfire.te
Source6: crossfire.fc
Source7: crossfire.if
Source8: logwatch.logconf.crossfire
Source9: logwatch.script.crossfire
Source10: logwatch.serviceconf.crossfire
#Patch0:  crossfire-1.10.0-log-login.patch
#Patch1:  crossfire-1.11.0-curl.patch
Patch2:  crossfire-1.71.0-snprintf-formatting.patch
Patch3: crossfire-c99.patch
Requires:       crossfire-maps
BuildRequires:  gcc
BuildRequires:  checkpolicy perl-generators selinux-policy-devel hardlink
BuildRequires:  libXt-devel
BuildRequires:  libXext-devel
BuildRequires:  libXaw-devel
BuildRequires:  perl(FileHandle)
BuildRequires:  python3-devel
BuildRequires:  autoconf flex
BuildRequires:  systemd-rpm-macros
BuildRequires: make
BuildRequires: libxcrypt-devel
Requires: %{name}-plugins

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: crossfire-devel = %{version}-%{release}
Obsoletes: crossfire-devel < %{version}-%{release}

%description
Crossfire is a highly graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

This package contains the server for hosting crossfire games over a
public or private network.

%package doc
Summary: Documentation files for Crossfire
# Don't require the base package.  The docs can be used without the
# base package, and in fact include docs for both the client and
# server packages.
%description doc
Documentation files for the crossfire game.

#%package devel
#Summary: Development files for writing crossfire plugins
#Requires: %%{name} = %%{version}-%%{release}
#%description devel
#Development files for writing crossfire plugins.

%package plugins
Summary: Plugin modules for the crossfire game server
Requires: %{name} = %{version}-%{release}
%description plugins
Plugin modules for the crossfire game server.

%package client-images
Summary: Image cache for crossfire clients
# No version dependency for the client since the images are pretty
# ignorant of the client version.
Requires: crossfire-client
%description client-images
Image files that can be used with the crossfire clients so that they
don't have to be downloaded from the server.

%package selinux
Summary: SELinux policy files for crossfire
Requires: %{name} = %{version}-%{release}
Requires:       selinux-policy >= %{selinux_policyver}
Requires(post):         /usr/sbin/semodule /usr/sbin/semanage /sbin/fixfiles
Requires(preun):        /usr/sbin/semodule /usr/sbin/semanage /sbin/fixfiles
Requires(postun):       /usr/sbin/semodule
%description selinux
selinux policy files for the Crossfire game server

%package logwatch
Summary: logwatch scripts for the Crossfire game server
Requires: %{name} = %{version}-%{release} logwatch
%description logwatch
logwatch scripts for the Crossfire game server

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn crossfire-server-%{version}
%setup -q -a 1 -n crossfire-server-%{version}
#%%patch0 -p0
#%patch1 -p0
%patch -P2 -p0
%patch -P3 -p1
mkdir SELinux
cp  %{SOURCE5} %{SOURCE6} %{SOURCE7} SELinux

mv arch/ lib/

sed -i 's#\r##' utils/player_dl.pl.in
# Don't use a hardcoded /tmp directory for building the image archive
sed -i "s#^\$TMPDIR=.*#\$TMPDIR=\"`pwd`\";#" lib/adm/collect_images.pl
# Don't map stdio streams to /
# This is fixed in CVS, but didn't make it into the 1.9.1 release.
sed -i 's#    (void) open ("/", O_RDONLY);#    (void) open ("/var/log/crossfire/crossfire.log", O_RDONLY);#' server/daemon.c

# Change the location of the tmp directory
sed -i "s@^#define TMPDIR \"/tmp\"@#define TMPDIR \"%{_var}/games/%{name}/tmp\"@" include/config.h

# Create a sysusers.d config file
cat >crossfire.sysusers.conf <<EOF
u crossfire - 'Daemon account for the crossfire server' %{_datadir}/%{name} -
EOF

%build
# Change the localstatedir so that the variable data files are
# put in /var/games/crossfire instead of /var/crossfire.  This is
# in agreement with the FHS.
%configure --localstatedir=%{_var}/games --disable-static

#make %%{?_smp_mflags} # parallel build is broken
make CFLAGS="$RPM_OPT_FLAGS -std=gnu17"

# Build the selinux policy file
pushd SELinux
for variant in %{selinux_variants}
do
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile
    mv %{name}.pp %{name}.pp.${variant}
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd

# This will create a tarball of the images for the client.
cd lib && adm/collect_images.pl -archive

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Install the client images
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
tar xf %{name}-images.tar -C $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
# Nuke the installation instructions for the image archive.
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}-client/README

#install -pD -m 0755 %%{SOURCE2} $RPM_BUILD_ROOT%%{_initrddir}/crossfire
install -pD -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/crossfire.service

# Move some rarely-used binaries out of /usr/bin and into a
# tools directory.
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This utility restarts crossfire at periodic intervals.
#mv $RPM_BUILD_ROOT%{_bindir}/crossloop,pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This submits core files to the developers.
mv $RPM_BUILD_ROOT%{_bindir}/crossloop.web $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# Allows players to download their player files from a web
# server. This feature relies on a properly configured web server
# which is not handled by this rpm release.
mv $RPM_BUILD_ROOT%{_bindir}/player_dl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# Binary for running a crossfire metaserver.  Requires interaction with
# a web server, so we disable this for now.
#rm $RPM_BUILD_ROOT%{_libdir}/%{name}/metaserver.pl

# I have no idea what this is for.
#mv $RPM_BUILD_ROOT%{_libdir}/%{name}/mktable.script $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This is not needed anymore based on comments at the top of
# the file itself.
#rm $RPM_BUILD_ROOT%{_libdir}/%{name}/add_throw.perl

# /usr/bin is a better place for the standalone random map generator
#mv $RPM_BUILD_ROOT/usr/libexec/crossfire/random_map $RPM_BUILD_ROOT%{_bindir}/cross_random_map

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

# Create the log directory
mkdir -p $RPM_BUILD_ROOT%{_var}/log/%{name}

install -p -D -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}

install -p -D -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}

mkdir $RPM_BUILD_ROOT%{_var}/games/%{name}/tmp

# Install selinux policies
pushd SELinux
for variant in %{selinux_variants}
do
    install -d $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}
    install -p -m 644 %{name}.pp.${variant} \
           $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}/%{name}.pp
done
popd
# Hardlink identical policy module packages together
/usr/bin/hardlink -cv $RPM_BUILD_ROOT%{_datadir}/selinux

# Install logwatch files
install -pD -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0755 %{SOURCE9} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf

install -m0644 -D crossfire.sysusers.conf %{buildroot}%{_sysusersdir}/crossfire.conf

%post
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post selinux
# Install SELinux policy modules
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{name}.pp &> /dev/null || :
done
/usr/sbin/semanage port -a -t %{name}_port_t -p tcp 13327 > /dev/null 2>&1 || :
/sbin/fixfiles -R %{name} restore || :
/sbin/service %{name} condrestart > /dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable crossfire.service > /dev/null 2>&1 || :
    /bin/systemctl stop crossfire.service > /dev/null 2>&1 || :
fi

%preun selinux
if [ "$1" -lt "1" ] ; then
    # Unload the module
    /usr/sbin/semanage port -d -t %{name}_port_t -p tcp 13327 >/dev/null 2>&1 || :
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -s ${variant} -r %{name} &> /dev/null || :
    done
    # Set the context back
    /sbin/fixfiles -R %{name} restore || :
fi

%postun
#if [ "$1" -ge "1" ]; then
#    /sbin/service crossfire condrestart >/dev/null 2>&1
#fi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart crossfire.service >/dev/null 2>&1 || :
fi

%postun selinux
if [ "$1" -ge "1" ] ; then
    # Replace the module if it is already loaded. semodule -u also
    # checks the module version
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -u %{_datadir}/selinux/${variant}/%{name}.pp || :
    done
fi

%files
%license COPYING
%doc README NEWS AUTHORS
#%%{_bindir}/crossedit
#%%{_bindir}/crossfire
%{_bindir}/crossfire-server
%{_bindir}/crossloop
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/ban_file
%config(noreplace) %{_sysconfdir}/%{name}/dm_file
%config(noreplace) %{_sysconfdir}/%{name}/exp_table
%config(noreplace) %{_sysconfdir}/%{name}/forbid
%config(noreplace) %{_sysconfdir}/%{name}/motd
%config(noreplace) %{_sysconfdir}/%{name}/news
%config(noreplace) %{_sysconfdir}/%{name}/rules
%config(noreplace) %{_sysconfdir}/%{name}/settings
%config(noreplace) %{_sysconfdir}/%{name}/metaserver2
%config(noreplace) %{_sysconfdir}/%{name}/stat_bonus
%attr(-,crossfire,root) %{_var}/games/%{name}
%attr(-,crossfire,root) %{_var}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man6/*
%{_unitdir}/%{name}.service
%{_sysusersdir}/crossfire.conf

%files doc
%doc doc/Developers doc/playbook* doc/scripts doc/spell-docs doc/spoiler doc/spoiler-html doc/*.txt

#%files devel
#%defattr(-,root,root,-)
#%%{_bindir}/crossfire-config
#%doc doc/plugins

%files plugins
%{_libdir}/%{name}/plugins

%files client-images
%{_datadir}/%{name}-client

%files selinux
%doc SELinux/*.??
%{_datadir}/selinux/*/%{name}.pp

%files logwatch
%{logwatch_conf}/logfiles/%{name}.conf
%{logwatch_conf}/services/%{name}.conf
%{logwatch_scripts}/services/%{name}

%changelog
%autochangelog
