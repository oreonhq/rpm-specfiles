%global source0_hash 23e4686e5848c74cb680c09c2811f0357739ecfe641f9c4072ee42399092c97b

%define _hardened_build 1
%define privoxyconf %{_sysconfdir}/%{name}
%define privoxy_uid 73
%define privoxy_gid 73
%define beta_or_stable stable
#define beta_or_stable beta

Name: privoxy
Version: 4.1.0
Release: 2%{?dist}
Summary: Privacy enhancing proxy
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/ijbswa/%{name}-%{version}-%{beta_or_stable}-src.tar.gz
Source1: privoxy.service
Source2: privoxy.logrotate
URL: http://www.privoxy.org/
BuildRequires: make
BuildRequires: libtool autoconf pcre2-devel zlib-devel systemd

%description 
Privoxy is a web proxy with advanced filtering capabilities for
protecting privacy, filtering web page content, managing cookies,
controlling access, and removing ads, banners, pop-ups and other
obnoxious Internet junk. Privoxy has a very flexible configuration and
can be customized to suit individual needs and tastes. Privoxy has application
for both stand-alone systems and multi-user networks.

Privoxy is based on the Internet Junkbuster.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{beta_or_stable}

# Create a sysusers.d config file
cat >privoxy.sysusers.conf <<EOF
g privoxy %{privoxy_gid}
u privoxy %{privoxy_uid}:%{privoxy_gid} - %{privoxyconf} -
EOF

%build
rm -rf autom4te.cache
autoreconf
# lets test how it works with dynamic pcre:
#configure --disable-dynamic-pcre
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sbindir} \
         %{buildroot}%{_mandir}/man8 \
         %{buildroot}%{_localstatedir}/log/%{name} \
         %{buildroot}%{privoxyconf}/templates \
         %{buildroot}%{_unitdir}

install -p -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -p -m 644 {config,*.action,default.filter,trust} %{buildroot}%{privoxyconf}/
install -p -m 644 templates/* %{buildroot}%{privoxyconf}/templates
install -p -m 644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -m 711 -d %{buildroot}%{_localstatedir}/log/%{name}

# Customize the configuration file
sed -i -e 's@^confdir.*@confdir %{privoxyconf}@g' %{buildroot}%{privoxyconf}/config
sed -i -e 's@^logdir.*@logdir %{_localstatedir}/log/%{name}@g' %{buildroot}%{privoxyconf}/config

touch %{buildroot}%{_sysconfdir}/privoxy/user.filter

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d
cp -p %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}

install -m0644 -D privoxy.sysusers.conf %{buildroot}%{_sysusersdir}/privoxy.conf

%post
%systemd_post privoxy.service

if [[ ! -f %{_sysconfdir}/privoxy/user.filter ]]
then
    touch %{_sysconfdir}/privoxy/user.filter
fi

%preun
%systemd_preun privoxy.service

%postun
%systemd_postun_with_restart privoxy.service

%files
%defattr(-,%{name},%{name},-)
%dir %{_localstatedir}/log/%{name}

# Owned by root
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/privoxy/user.filter
%attr(0755,root,root)%{_sbindir}/%{name}
%config(noreplace) %{privoxyconf}
%attr(0644,root,root) %{_unitdir}/%{name}.service
%{_mandir}/man8/%{name}.*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%doc README AUTHORS ChangeLog LICENSE 
%doc doc
%{_sysusersdir}/privoxy.conf

%changelog
%autochangelog
