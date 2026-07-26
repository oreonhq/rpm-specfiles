%global source0_hash ed9415340ae60de1d76fb15ef142798fe227195909c97b0b1a32456d1c9b0d3e

%define          mainver   2.16
#%%define          betatag   dev-20160114
%define          dwfdate   20251228

%define          baserelease 1

%define          rel        %{?betatag:0.}%{baserelease}%{?betatag:.%(echo %betatag | sed -e 's|-||g')}

%if 0%{?fedora} >= 42
%global          use_systemd_sysusers  1
%else
# Drop this when F41 gets EOF
%global          use_systemd_sysusers  0
%endif

Summary:         Calculate tide all over the world
Name:            xtide
Version:         %{mainver}
Release:         %{rel}%{?dist}

URL:             http://www.flaterco.com/xtide/
Source0:         https://flaterco.com/files/xtide/%{name}-%{version}%{?betatag:-%betatag}.tar.xz

Source14:        xtide-get_harmonics-data.sh
Source20:        %{name}.desktop
Source30:        xtide-README.fedora

# Source41 is created by Harminics-dwf-create-regal-OK.sh in
# Source40
#
# (Updated: 2007-Nov-23) 
# Upstream now splitted free and non-free harmonics data
#                     
#Source40:        Harminics-USpart-recreate-sh.tar.bz2
#Source41:        harmonics-dwf-%%{dwfdate}-dump-US.tar.bz2
Source42:        https://flaterco.com/files/xtide/harmonics-dwf-%{dwfdate}-free.tar.xz

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later

BuildRequires:   make
BuildRequires:   gcc-c++
BuildRequires:   libXaw-devel
BuildRequires:   Xaw3d-devel
BuildRequires:   libXext-devel
BuildRequires:   libpng-devel
BuildRequires:   zlib-devel
BuildRequires:   desktop-file-utils
BuildRequires:   libdstr-devel
BuildRequires:   libtcd-devel
BuildRequires:   gpsd-devel >= 3
BuildRequires:   systemd
BuildRequires:   systemd-devel
# By SOURCE1
BuildRequires:   automake
BuildRequires:   autoconf
BuildRequires:   libtool
# By SOURCE3
BuildRequires:   byacc
BuildRequires:   flex
# Explicit for %%PATCH1
BuildRequires:   %{_bindir}/pkg-config

Requires:        wvs-data
Requires:        xorg-x11-fonts-misc
Requires:        xtide-common = %{version}-%{release}
Requires:        libxtide%{?_isa} = %{version}-%{release}

%if ! %{use_systemd_sysusers}
Requires(pre):      shadow-utils
%endif
Requires(preun):    systemd
Requires(postun):   systemd
Requires(post):     systemd

%package -n      libxtide
Summary:         XTide library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later

%package -n      libxtide-devel
Summary:         Development files for libxtide
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:         GPL-3.0-or-later
Requires:        libxtide%{?_isa} = %{version}-%{release}

%package         common
Summary:         Xtide common files
# Automatically converted from old format: Public Domain - needs further work
License:         LicenseRef-Callaway-Public-Domain
Requires:        bzip2
Requires:        wget
BuildArch:       noarch

%description
XTide is a package that provides tide and current
predictions in a wide variety of formats.  Graphs, text listings, and
calendars can be generated, or a tide clock can be provided on your
desktop.

XTide can work with X-windows, plain text terminals, or the web. This
is accomplished with three separate programs: the interactive
interface (xtide), the non-interactive or command line interface
(tide), and the web interface.

The algorithm that XTide uses to predict tides is the one used by the
National Ocean Service in the U.S.  It is significantly more accurate
than the simple tide clocks that can be bought in novelty stores.
However, it takes more to predict tides accurately than just a spiffy
algorithm -- you also need some special data for each and every
location for which you want to predict tides.  XTide reads this data
from harmonics files.  See http://www.flaterco.com/xtide/files.html
for details on where to get these 

NOTE:
Please also see README.fedora in xtide-common package for Fedora 
specific issue.

%description -n libxtide
The libxtide package provides library files used for XTide.

%description -n libxtide-devel
The libxtide-devel package contains libraries and header files for
developing applications that use libxtide.

%description common
This package contains common files needed by xtide, xttpd and
tideEditor.
Please read README.fedora for Fedora specific issue.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?betatag:1}
%setup -q -n %{name}-%{version}-DEVELOPMENT -a 42
%else
%setup -q -n %{name}-%{version}%{?betatag:-%{betatag}} -a 42
%endif

# Systemd stuff
sed -i scripts/systemd/xttpd.socket \
	-e 's|ListenStream=80|ListenStream=8080|'

cat > scripts/systemd/xttpd.service.conf <<EOF
HFILE_PATH=%{_datadir}/%{name}-harmonics
XTTPD_FEEDBACK=xtide-maintainer@fedoraproject.org
EOF

sed -i scripts/systemd/xttpd.service.in \
	-e 's|^EnvironmentFile=.*$|EnvironmentFile=-%{_sysconfdir}/sysconfig/xttpd.service.conf|'

# Dstr -> Dstr.h
grep -rl 'include.*<Dstr>' . | while read f ; do
	sed -i.name -e 's|\(include.*\)<Dstr>|\1<Dstr.h>|' $f
done

autoreconf -i

# Embed version
sed -i.ver \
	-e "\@^PACKAGE_VERSION=@s|'.*'$|'%{version}-%{release}'|" \
	-e "\@^PACKAGE_STRING=@s|'\(XTide \).*'$|'\1%{version}-%{release}'|" \
	-e "\@^[ \t]*VERSION=@s|'.*'$|'%{version}-%{release}'|" \
	configure

# Kill rpath, ah!
sed -i.rpath configure \
	-e 's|hardcode_libdir_flag_spec=|kill_hardcode_libdir_flag_spec=|' \
	-e 's|hardcode_libdir_flag_spec_CXX=|kill_hardcode_libdir_flag_spec_CXX=|' \
	%{nil}
sed -i.rpath ltmain.sh \
	-e 's|\$finalize_rpath|\$finalize_no_rpath|' \
	%{nil}

%if %{use_systemd_sysusers}
# Create a sysusers.d config file
cat >xtide.sysusers.conf <<EOF
u xttpd - 'XTide web server' %{_sysconfdir}/%{name} -
EOF
%endif

%build
%configure \
   --enable-systemd \
%if 0
   --enable-moon-age \
%endif
   --with-xttpd-user=xttpd \
   --with-xttpd-group=xttpd

%{__make} %{?_smp_mflags} -k

echo "%{_datadir}/xtide-harmonics/" > %{name}.conf
echo "%{_datadir}/wvs-data/" >> %{name}.conf

%install
# 1. install xtide
%{__make} \
   DESTDIR=$RPM_BUILD_ROOT \
   INSTALL="%{__install} -p" \
   install

%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}

# xttpd treatment
# xttpd is wrapped
%{__sed} -e 's|20081228|%{dwfdate}|' %{SOURCE14} \
   > xtide-get_harmonics-data.sh
%{__install} -c -p -m 755 xtide-get_harmonics-data.sh \
   $RPM_BUILD_ROOT%{_sbindir}

# ensure xttpd binary installation directory (original
# wrapper script is hardcorded)
%{__sed} -i -e 's|/usr/libexec|%{_libexecdir}|' \
   $RPM_BUILD_ROOT%{_sbindir}/xttpd

# Install systemd unit file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.socket \
	scripts/systemd/xttpd.service \
	${RPM_BUILD_ROOT}%{_unitdir}
%{__ln_s} -f \
	%{_sysconfdir}/sysconfig/xttpd.socket \
	${RPM_BUILD_ROOT}%{_unitdir}/xttpd.socket
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.service.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
%{__install} -c -p -m 644 \
	scripts/systemd/xttpd.socket \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/xttpd.socket

# 1A Install harmonics file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/%{name}-harmonics

# 1B Add configuration file
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sysconfdir}
%{__install} -c -p -m 644 %{name}.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/

# 1C Add desktop entry (xtide)
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   %{SOURCE20}

# 1D Install icon
for f in iconsrc/icon_*_orig.png ; do
   %{__install} -c -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/%{name}/
done
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
%{__ln_s} -f ../../../../%{name}/icon_16x16_orig.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__ln_s} -f ../../../../%{name}/icon_48x48_orig.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# 1E install xttpd conf file
%{__mkdir_p} $RPM_BUILD_ROOT%{_initddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/xtide

# 1F and others
%{__install} -c -p -m 644 %{SOURCE30} README.fedora

# 1G tcd data
%{__install} -c -p -m 644 harmonics-dwf-%{dwfdate}/*tcd \
   $RPM_BUILD_ROOT%{_datadir}/xtide-harmonics/

# 2 Documentation
for f in AUTHORS ChangeLog NEWS README ; do
   iconv -f ISO-8859-1 -t UTF-8 $f > $f.tmp && \
      ( touch -r $f $f.tmp ; mv -f $f.tmp $f ) || rm -f $f.tmp
done

rm -rf harmonics-dwf
mkdir harmonics-dwf
cp -a harmonics-dwf-%{dwfdate}/[A-Z]* \
	harmonics-dwf/

# 3 cleanup
rm -rf $RPM_BUILD_ROOT%{_libdir}/libxtide.{a,la}

%if %{use_systemd_sysusers}
install -m0644 -D xtide.sysusers.conf %{buildroot}%{_sysusersdir}/xtide.conf
%endif

%post
%systemd_post xttpd.socket xttpd.service
exit 0

%postun
%systemd_postun xttpd.socket xttpd.service
exit 0

%pre
%if ! %{use_systemd_sysusers}
getent group xttpd &>/dev/null || \
   %{_sbindir}/groupadd -r xttpd
getent passwd xttpd &> /dev/null || \
   %{_sbindir}/useradd \
   -c "XTide web server" \
   -g xttpd \
   -d %{_sysconfdir}/%{name} \
   -r \
   -s /sbin/nologin \
   xttpd 2>/dev/null
%endif
exit 0

%preun
%systemd_preun xttpd.socket xttpd.service
exit 0

%ldconfig_scriptlets -n libxtide

%files common
%doc README.fedora
%doc harmonics-dwf/
%config(noreplace) %{_sysconfdir}/%{name}.conf

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}-harmonics
%dir %{_sysconfdir}/%{name}

%{_sbindir}/xtide-get*.sh

# Now include tcd data
%{_datadir}/%{name}-harmonics/*.tcd

%files -n libxtide
%{_libdir}/libxtide.so.2{,.*}

%files -n libxtide-devel
%{_libdir}/libxtide.so
%{_includedir}/libxtide/

%files
%defattr(-,root,root,-)

%doc AUTHORS README README-QUICK
%license COPYING
# xtide
%{_mandir}/man1/*tide.1*

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/icon_*_orig.png

%{_bindir}/*tide

# xttpd
%config(noreplace) %{_sysconfdir}/sysconfig/xttpd.service.conf
%config(noreplace) %{_sysconfdir}/sysconfig/xttpd.socket
%{_unitdir}/xttpd.service
%{_unitdir}/xttpd.socket

%{_sbindir}/xttpd
%{_datadir}/man/man8/xttpd.8*
%if %{use_systemd_sysusers}
%{_sysusersdir}/xtide.conf
%endif

%changelog
%autochangelog
