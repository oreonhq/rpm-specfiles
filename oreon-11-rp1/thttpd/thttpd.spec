%global source0_hash 99c09f47da326b1e7b5295c45549d2b65534dce27c44812cf7eef1441681a397
%global webroot /var/www/thttpd
Name:           thttpd
Version:        2.29
Release:        23%{?dist}
Summary:        A tiny, turbo, throttleable lightweight HTTP server
License:        LicenseRef-Callaway-BSD
URL:            http://www.acme.com/software/thttpd/
Source0:        http://www.acme.com/software/thttpd/thttpd-%{version}.tar.gz
Source1:        thttpd.service
Source2:        thttpd.logrotate
Source10:       index.html
Source11:       thttpd_powered_3.png
Source12:       poweredby.png
Patch0:         thttpd-2.25b-CVE-2005-3124.patch
Patch1:         thttpd-2.25b-CVE-2012-5640-check_crypt_return_value.patch
Patch2:         thttpd-fix-world-readable-log.patch
Patch3:         thttpd-c99.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Thttpd is a very compact no-frills httpd serving daemon that can handle
very high loads. While lacking many of the advanced features of Apache, 
thttpd operates without forking and is extremely efficient in memory use. 
Basic support for cgi scripts, authentication, and ssi is provided for. 
Advanced features include the ability to throttle traffic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .CVE-2005-3124
%patch -P1 -p1 -b .CVE-2012-5640
%patch -P2 -p1 -b .rhbz924857
%patch -P3 -p1 -b .c99
# Convert man pages to UTF8
for man in *.8 */*.8 */*.1; do
    iconv -f iso8859-1 -t utf-8 -o tmp ${man}
    mv -f tmp ${man}
done

# Create a sysusers.d config file
cat >thttpd.sysusers.conf <<EOF
g www -
u thttpd -:www 'Thttpd Web Server User' %{webroot} -
EOF

%build

%configure
sed -i.old -e 's/-o bin -g bin//g' Makefile
sed -i.old -e 's/-m 444/-m 644/g; s/-m 555/-m 755/g' Makefile
sed -i.old -e 's/.*chgrp.*//g; s/.*chmod.*//g' extras/Makefile
%{?_without_indexes:      sed -i.old -e 's/#define GENERATE_INDEXES/#undef GENERATE_INDEXES/g' config.h}
%{!?_with_showversion:    sed -i.old -e 's/#define SHOW_SERVER_VERSION/#undef SHOW_SERVER_VERSION/g' config.h}
%{!?_with_expliciterrors: sed -i.old -e 's/#define EXPLICIT_ERROR_PAGES/#undef EXPLICIT_ERROR_PAGES/g' config.h}
%{make_build} \
    SUBDIRS="extras" WEBDIR=%{webroot} STATICFLAG="" \
    CCOPT="%{optflags} -D_FILE_OFFSET_BITS=64"
%install
mkdir -p %{buildroot}%{webroot}          \
         %{buildroot}%{_mandir}/man{1,8} \
         %{buildroot}%{_sbindir}         \
         %{buildroot}%{_unitdir}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/thttpd
make install SUBDIRS="extras" \
    BINDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir} \
    WEBDIR=%{buildroot}%{webroot}
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_sbindir}/htpasswd \
        %{buildroot}%{_bindir}/thtpasswd
mv %{buildroot}%{_mandir}/man1/htpasswd.1 \
        %{buildroot}%{_mandir}/man1/thtpasswd.1
install -pm0644 %{SOURCE10} %{SOURCE11} %{SOURCE12}\
                %{buildroot}%{webroot}/
cat << EOF > %{buildroot}%{_sysconfdir}/thttpd.conf
dir=%{webroot}
chroot
user=thttpd         # default = nobody
logfile=/var/log/thttpd.log
pidfile=/var/run/thttpd.pid
EOF
install -m0644 -D thttpd.sysusers.conf %{buildroot}%{_sysusersdir}/thttpd.conf
%oreon_autofiles main

%post

%systemd_post thttpd.service
%preun

%systemd_preun thttpd.service
%postun

%systemd_postun thttpd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
