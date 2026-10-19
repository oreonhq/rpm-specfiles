%global source0_hash c7f11cb5e217a500d87ee3b5d26c58a8652edbc0d3291688bb792b010fae43ac
%global source1_hash db0332605d859748a29a0c3c04cefd9163b6890f55c640bcf9602930e467fe37
%global _use_internal_dependency_generator 0
%global contentdir       %{_localstatedir}/www/%{name}
%global libdir           %{_localstatedir}/lib/mrtg
%global with_selinux 1
%global selinuxtype targeted
%global modulename mrtg
Summary:        Multi Router Traffic Grapher
Name:      mrtg
Version:   2.17.10
Release:        1%{?dist}
URL:       http://oss.oetiker.ch/mrtg/
Source0:        http://oss.oetiker.ch/mrtg/pub/mrtg-%{version}.tar.gz
Source1:        http://oss.oetiker.ch/mrtg/pub/mrtg-%{version}.tar.gz.md5
Source2:   mrtg.cfg
Source3:   filter-requires-mrtg.sh
Source5:   mrtg-httpd.conf
Source6:   filter-provides-mrtg.sh
Source7:   mrtg.tmpfiles
Source8:   mrtg.service
Source9:   mrtg.timer
Source100: %{modulename}.te
Source101: %{modulename}.if
Source102: %{modulename}.fc
Patch0:    mrtg-2.15.0-lib64.patch
Patch1:    mrtg-2.17.2-socket6-fix.patch
Patch2:    mrtg-2.17.4-cfgmaker-ifhighspeed.patch
Patch3:    mrtg-configure-c99.patch
License:   GPL-2.0-or-later
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires:  perl-Socket6 perl-IO-Socket-INET6 perl-locale
Requires:  gd
%if 0%{?with_selinux}
Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
%global __find_requires %{SOURCE3}
%global __find_provides %{SOURCE6}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-units
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
make LIBS='-lgd -lm'
find contrib -type f -exec \
    %{__perl} -e 's,^#!/\s*\S*perl\S*,#!%{__perl},gi' -p -i \{\} \;
find contrib -name "*.pl" -exec %{__perl} -e 's;\015;;gi' -p -i \{\} \;
find contrib -type f | xargs chmod a-x
%if 0%{?with_selinux}
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
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/mrtg.service
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/mrtg.timer
for i in mrtg cfgmaker indexmaker mrtg-traffic-sum; do
    sed -i 's;@@lib@@;%{_lib};g' "$RPM_BUILD_ROOT"%{_bindir}/"$i"
done
sed -i 's;@@lib@@;%{_lib};g' "$RPM_BUILD_ROOT"%{_mandir}/man1/*.1
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

install -d -m 0755 -o root -g root /var/lock/mrtg
%systemd_post mrtg.service
%preun

if [ $1 -eq 0 ]; then
  rm -rf /var/lock/mrtg
fi
%systemd_preun mrtg.service
%postun

%systemd_postun_with_restart mrtg.service 
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart mrtg.service &> /dev/null || :
fi
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n mrtg-selinux -f %{oreon_filedir}/mrtg-selinux.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.10-13
- Prepare for Oreon 11 (RP1)
