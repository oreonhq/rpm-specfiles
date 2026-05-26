# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c7f11cb5e217a500d87ee3b5d26c58a8652edbc0d3291688bb792b010fae43ac
%global source1_sha256 db0332605d859748a29a0c3c04cefd9163b6890f55c640bcf9602930e467fe37
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global _use_internal_dependency_generator 0

%global contentdir       %{_localstatedir}/www/%{name}
%global libdir           %{_localstatedir}/lib/mrtg

# defining macros needed by SELinux
%global with_selinux 1
%global selinuxtype targeted
%global modulename mrtg

Summary:   Multi Router Traffic Grapher
Name:      mrtg
Version:   2.17.10
Release:   13%{?dist}
URL:       http://oss.oetiker.ch/mrtg/
Source0:   http://oss.oetiker.ch/mrtg/pub/mrtg-%{version}.tar.gz
Source1:   http://oss.oetiker.ch/mrtg/pub/mrtg-%{version}.tar.gz.md5
# Source2: configuration file example
Source2:   mrtg.cfg
# Source3: script for filtering out false perl requires
Source3:   filter-requires-mrtg.sh
# Source4: configuration for Apache
Source5:   mrtg-httpd.conf
# Source6: script for filtering out false perl provides
Source6:   filter-provides-mrtg.sh
# Source7: tmpfiles rule
Source7:   mrtg.tmpfiles
# Source8: systemd service file
Source8:   mrtg.service
# Source9: systemd timer file
Source9:   mrtg.timer
# Source100-102: selinux policy for mrtg, extracted
# from https://github.com/fedora-selinux/selinux-policy
Source100: %{modulename}.te
Source101: %{modulename}.if
Source102: %{modulename}.fc
Patch0:    mrtg-2.15.0-lib64.patch
Patch1:    mrtg-2.17.2-socket6-fix.patch
# Patch2: some devices return 2**32-2 on ifSpeed (e. g. IBM FibreChannel switches)
Patch2:    mrtg-2.17.4-cfgmaker-ifhighspeed.patch
Patch3:    mrtg-configure-c99.patch
License:   GPL-2.0-or-later
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires:  perl-Socket6 perl-IO-Socket-INET6 perl-locale
Requires:  gd
%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
BuildRequires: make
BuildRequires: gd-devel, libpng-devel
BuildRequires: perl-generators
BuildRequires: systemd-units
BuildRequires: gcc

%global __find_requires %{SOURCE3}
%global __find_provides %{SOURCE6}

%description
The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
load on network-links. MRTG generates HTML pages containing PNG
images which provide a LIVE visual representation of this traffic.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:   mrtg SELinux policy
BuildArch: noarch
Requires:  selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires: selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module
%endif

%prep
%oreon_verify_sources
%setup -q
%patch -P0 -p1 -b .lib64
%patch -P1 -p1 -b .socket6
%patch -P2 -p1 -b .ifhighspeed
%patch -P3 -p1 -b .c99

for i in doc/mrtg-forum.1 doc/mrtg-squid.1 CHANGES; do
    iconv -f iso-8859-1 -t utf-8 < "$i" > "${i}_"
    mv "${i}_" "$i"
done

# Remove contribution useful on Windows only
rm -rf contrib/nt-services

%build
%configure
# Don't link rateup statically, don't link to indirect dependencies
# LIBS derived from autodetected by removing -Wl,-B(static|dynamic), -lpng, -lz
make LIBS='-lgd -lm'
find contrib -type f -exec \
    %{__perl} -e 's,^#!/\s*\S*perl\S*,#!%{__perl},gi' -p -i \{\} \;
find contrib -name "*.pl" -exec %{__perl} -e 's;\015;;gi' -p -i \{\} \;
find contrib -type f | xargs chmod a-x

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p %{SOURCE100} %{SOURCE101} %{SOURCE102} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif

%install
rm -rf   $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mrtg
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/mrtg
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lock/mrtg
mkdir -p $RPM_BUILD_ROOT%{contentdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d

install -m 644 images/*   $RPM_BUILD_ROOT%{contentdir}/
sed 's,@CONTENTDIR@,%{contentdir},g; s,@LIBDIR@,%{_localstatedir}/lib/mrtg,g' \
    %{SOURCE2} > $RPM_BUILD_ROOT%{_sysconfdir}/mrtg/mrtg.cfg
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/mrtg/mrtg.cfg

install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/mrtg.conf

mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -p -D -m 644 %{SOURCE7} $RPM_BUILD_ROOT/%{_tmpfilesdir}/mrtg.conf

# install systemd files
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/mrtg.service
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/mrtg.timer

# Add mrtg-traffic-sum here when upstream decides to install it
for i in mrtg cfgmaker indexmaker mrtg-traffic-sum; do
    sed -i 's;@@lib@@;%{_lib};g' "$RPM_BUILD_ROOT"%{_bindir}/"$i"
done

sed -i 's;@@lib@@;%{_lib};g' "$RPM_BUILD_ROOT"%{_mandir}/man1/*.1

%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

%post
install -d -m 0755 -o root -g root /var/lock/mrtg
%systemd_post mrtg.service

%preun
if [ $1 -eq 0 ]; then
  # Package removal, not upgrade
  rm -rf /var/lock/mrtg
fi
%systemd_preun mrtg.service

%postun
%systemd_postun_with_restart mrtg.service 

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the service needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart mrtg.service &> /dev/null || :
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%files
%license COPYING
%doc contrib CHANGES COPYRIGHT README THANKS
%dir %{_sysconfdir}/mrtg
%config(noreplace) %{_sysconfdir}/mrtg/mrtg.cfg
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mrtg.conf
%{contentdir}
%{_bindir}/*
%{_libdir}/mrtg2
%exclude %{_libdir}/mrtg2/Pod
%{_mandir}/*/*
%exclude %{_datadir}/mrtg2/icons
%exclude %{_datadir}/doc/mrtg2
%dir %{_localstatedir}/lib/mrtg
%{_tmpfilesdir}/mrtg.conf
%ghost /var/lock/mrtg
%{_unitdir}/mrtg.service
%{_unitdir}/mrtg.timer

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.10-13
- Prepare for Oreon 11 (RP1)
