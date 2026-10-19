%global source1_hash 016ee33b15879a96e14932a9209d03ee9e3da69b3f3bd6b82c800f43345f064d
%global source0_hash cc1917db207628c34d2222f1b6c416481f72f185ac3bc9e49b9a53db94fe1e1d
%define _hardened_build 1
%define selinux_variants mls strict targeted
%global selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)
%define logwatch_root %{_datadir}/logwatch
%define logwatch_conf %{logwatch_root}/dist.conf
%define logwatch_scripts %{logwatch_root}/scripts
Name: crossfire
Version: 1.71.0
Release:        1%{?dist}
Summary:        Server for hosting crossfire games
License: GPL-2.0-or-later and MIT
URL: http://crossfire.real-time.com
Source0:        http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.bz2
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
Patch2:  crossfire-1.71.0-snprintf-formatting.patch
Patch3: crossfire-c99.patch
Requires:       crossfire-maps
Requires: %{name}-plugins
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: crossfire-devel = %{version}-%{release}
Obsoletes: crossfire-devel < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  checkpolicy
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hardlink
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  perl(FileHandle)
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Crossfire is a highly graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

This package contains the server for hosting crossfire games over a
public or private network.

%package doc
Summary: Documentation files for Crossfire
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

%configure --localstatedir=%{_var}/games --disable-static
make CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
pushd SELinux
for variant in %{selinux_variants}
do
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile
    mv %{name}.pp %{name}.pp.${variant}
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd
cd lib && adm/collect_images.pl -archive
%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
tar xf %{name}-images.tar -C $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}-client/README
install -pD -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/crossfire.service
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/tools
mv $RPM_BUILD_ROOT%{_bindir}/crossloop.web $RPM_BUILD_ROOT%{_datadir}/%{name}/tools
mv $RPM_BUILD_ROOT%{_bindir}/player_dl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la
mkdir -p $RPM_BUILD_ROOT%{_var}/log/%{name}
install -p -D -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}
mkdir $RPM_BUILD_ROOT%{_var}/games/%{name}/tmp
pushd SELinux
for variant in %{selinux_variants}
do
    install -d $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}
    install -p -m 644 %{name}.pp.${variant} \
           $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}/%{name}.pp
done
popd
/usr/bin/hardlink -cv $RPM_BUILD_ROOT%{_datadir}/selinux
install -pD -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0755 %{SOURCE9} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf
install -m0644 -D crossfire.sysusers.conf %{buildroot}%{_sysusersdir}/crossfire.conf
%oreon_autofiles crossfire-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crossfire-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crossfire-client-images usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crossfire-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crossfire-logwatch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

if [ $1 -eq 1 ] ; then 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post selinux

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
    /bin/systemctl --no-reload disable crossfire.service > /dev/null 2>&1 || :
    /bin/systemctl stop crossfire.service > /dev/null 2>&1 || :
fi
%preun selinux

if [ "$1" -lt "1" ] ; then
    /usr/sbin/semanage port -d -t %{name}_port_t -p tcp 13327 >/dev/null 2>&1 || :
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -s ${variant} -r %{name} &> /dev/null || :
    done
    /sbin/fixfiles -R %{name} restore || :
fi
%postun

/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    /bin/systemctl try-restart crossfire.service >/dev/null 2>&1 || :
fi
%postun selinux

if [ "$1" -ge "1" ] ; then
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -u %{_datadir}/selinux/${variant}/%{name}.pp || :
    done
fi
%files -f %{oreon_filedir}/main.list
%files -n crossfire-doc -f %{oreon_filedir}/crossfire-doc.list
%files -n crossfire-plugins -f %{oreon_filedir}/crossfire-plugins.list
%files -n crossfire-client-images -f %{oreon_filedir}/crossfire-client-images.list
%files -n crossfire-selinux -f %{oreon_filedir}/crossfire-selinux.list
%files -n crossfire-logwatch -f %{oreon_filedir}/crossfire-logwatch.list

%changelog

%autochangelog
