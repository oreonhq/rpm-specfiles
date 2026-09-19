%global source0_hash 99c09f47da326b1e7b5295c45549d2b65534dce27c44812cf7eef1441681a397

# Where the default web root will be configured and default files installed
%global webroot /var/www/thttpd

Name:           thttpd
Version:        2.29
Release:        23%{?dist}
Summary:        A tiny, turbo, throttleable lightweight HTTP server

# Automatically converted from old format: BSD - review is highly recommended.
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
BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  systemd gcc
%{?systemd_requires}

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
# Hacks :-)
sed -i.old -e 's/-o bin -g bin//g' Makefile
sed -i.old -e 's/-m 444/-m 644/g; s/-m 555/-m 755/g' Makefile
sed -i.old -e 's/.*chgrp.*//g; s/.*chmod.*//g' extras/Makefile
# Config changes
%{?_without_indexes:      sed -i.old -e 's/#define GENERATE_INDEXES/#undef GENERATE_INDEXES/g' config.h}
%{!?_with_showversion:    sed -i.old -e 's/#define SHOW_SERVER_VERSION/#undef SHOW_SERVER_VERSION/g' config.h}
%{!?_with_expliciterrors: sed -i.old -e 's/#define EXPLICIT_ERROR_PAGES/#undef EXPLICIT_ERROR_PAGES/g' config.h}

%{make_build} \
    SUBDIRS="extras" WEBDIR=%{webroot} STATICFLAG="" \
    CCOPT="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
# Prepare required directories
mkdir -p %{buildroot}%{webroot}          \
         %{buildroot}%{_mandir}/man{1,8} \
         %{buildroot}%{_sbindir}         \
         %{buildroot}%{_unitdir}

# Install init script and logrotate entry
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/thttpd

# Main install (list SUBDIRS to exclude "cgi-src")
make install SUBDIRS="extras" \
    BINDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir} \
    WEBDIR=%{buildroot}%{webroot}

# Rename htpasswd in case apache is installed too
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_sbindir}/htpasswd \
        %{buildroot}%{_bindir}/thtpasswd
mv %{buildroot}%{_mandir}/man1/htpasswd.1 \
        %{buildroot}%{_mandir}/man1/thtpasswd.1

# Install the default index.html and related files
install -pm0644 %{SOURCE10} %{SOURCE11} %{SOURCE12}\
                %{buildroot}%{webroot}/

# Symlink for the powered-by-$DISTRO image
# Removed: thttpd does not support symlink outsidedocroot
# See: http://acme.com/software/thttpd/thttpd_man.html#SYMLINKS

# Install a default configuration file
cat << EOF > %{buildroot}%{_sysconfdir}/thttpd.conf
# BEWARE : No empty lines are allowed!
# This section overrides defaults
dir=%{webroot}
chroot
user=thttpd         # default = nobody
logfile=/var/log/thttpd.log
pidfile=/var/run/thttpd.pid
# This section _documents_ defaults in effect
# port=80
# nosymlink         # default = !chroot
# novhost
# nocgipat
# nothrottles
# host=0.0.0.0
# charset=iso-8859-1
EOF

install -m0644 -D thttpd.sysusers.conf %{buildroot}%{_sysusersdir}/thttpd.conf

%post
%systemd_post thttpd.service

%preun
%systemd_preun thttpd.service

%postun
%systemd_postun thttpd.service

%files
%doc README TODO
%{_bindir}/thtpasswd
%if 0%{?_with_makeweb:1}
    %attr(2755,root,www) %{_sbindir}/makeweb
    %{_mandir}/man1/makeweb.1*
%else
    %exclude %{_sbindir}/makeweb
    %exclude %{_mandir}/man1/makeweb.1*
%endif
%{_sbindir}/syslogtocern
%{_sbindir}/thttpd
%{_unitdir}/thttpd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/thttpd
%config(noreplace) %{_sysconfdir}/thttpd.conf
%{webroot}/
%{_mandir}/man1/thtpasswd.1*
%{_mandir}/man8/syslogtocern.8*
%{_mandir}/man8/thttpd.8*
# Hack to own parent directory for the default "webroot". Remove if needed.
%dir /var/www
%{_sysusersdir}/thttpd.conf

%changelog
%autochangelog
