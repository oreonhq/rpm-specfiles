%global source6_hash 5783ebb6b7d3a3d67abd1aa71ec961f0116a88149ea688ed08f898a218bf06d5
%global source5_hash 2629c020c081e3453523761bc6ee52903b173ea42f5faca342d545b4fc368224
%global source4_hash 9a70c136946c1d18d5355c41516f1bdc95d4321938919e69065533e2aeb51e0e
%global source3_hash 373eb96344f805f7c7c42733aaeca6adde289f00135ff2c167d301c43925b382
%global source1_hash 0f29a91241b51e0eddbb5515f1ec7881c9ded230d4dc8f3a7d501d4c3b5136ff
%global source0_hash 20e5e0f2c917acfb51120eec2fba9a4ba4e1e10fd28465067cc87a7d81a829a3
%global source3_key_fpr 43387825DDB1BB97EC36BA5D007C8D7C15D87369
%global source4_key_fpr D6786CE303D9A9022998DC6CC8464D549AF75C0A
%global source5_key_fpr 7338973069ED3F443F4D37DFA64FD5B17ADB39A8
%global source6_key_fpr 13C82A63B603576156E30A4EA0EA981B66B0D967
%global  _hardened_build     1
%global  nginx_user          nginx
%undefine _strict_symbol_defs_build
%bcond_with geoip
%ifnarch s390 s390x ppc64 ppc64le
%global with_gperftools 1
%endif
%global with_aio 1
%bcond_without engine
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%global with_ktls 1
%endif
%global nginx_abiversion %{version}
%global nginx_moduledir %{_libdir}/nginx/modules
%global nginx_moduleconfdir %{_datadir}/nginx/modules
%global nginx_srcdir %{_usrsrc}/%{name}-%{version}-%{release}
%global __provides_exclude_from ^%{nginx_srcdir}/.*$
%global __requires_exclude_from ^%{nginx_srcdir}/.*$
Name:              nginx
Epoch:             2
Version:           1.28.2
Release:        1%{?dist}
Summary:        A high performance web server and reverse proxy server
License:           BSD-2-Clause
URL:               https://nginx.org
Source0:        https://nginx.org/download/nginx-%{version}.tar.gz
Source1:        https://nginx.org/download/nginx-%{version}.tar.gz.asc
Source3:        https://nginx.org/keys/arut.key
Source4:        https://nginx.org/keys/pluknet.key
Source5:        https://nginx.org/keys/sb.key
Source6:        https://nginx.org/keys/thresh.key
Source10:        nginx.service
Source11:        nginx.logrotate
Source12:        nginx.conf
Source13:        nginx-upgrade
Source14:          nginx-upgrade.8
Source15:        macros.nginxmods.in
Source16:        nginxmods.attr
Source17:        nginx-ssl-pass-dialog
Source18:       nginx@.service
Source19:        nginx.sysusers
Source20:        nginx.tmpfiles
Source102:        nginx-logo.png
Source200:        README.dynamic
Source220:        instance.conf
Patch0:        0001-remove-Werror-in-upstream-build-scripts.patch
Patch1:        0002-fix-PIDFile-handling.patch
Patch2:        0003-Add-SSL-passphrase-dialog.patch
Patch3:        0004-Disable-ENGINE-support.patch
Patch4:        0005-Compile-perl-module-with-O2.patch
Patch5:            0006-Clarify-binding-behavior-of-t-option.patch
%if 0%{?with_gperftools}
%endif
Requires:          nginx-filesystem = %{epoch}:%{version}-%{release}
Requires:          system-logos-httpd
Provides:          webserver
Recommends:        logrotate
Requires:          %{name}-core = %{epoch}:%{version}-%{release}
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  gnupg2
BuildRequires:  gperftools-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Nginx is a web server and a reverse proxy server for HTTP, SMTP, POP3 and
IMAP protocols, with a strong focus on high concurrency, performance and low
memory usage.

%package core
Summary: nginx minimal core
%if 0%{?with_mailcap_mimetypes}
Requires:          nginx-mimetypes
%endif
Requires:          openssl%{?openssl_pkgversion}-libs
Requires(pre):     nginx-filesystem
Conflicts:         nginx < 1:1.20.2-4
Provides:          nginx(abi) = %{nginx_abiversion}
%description core
nginx minimal core

%package all-modules
Summary:           A meta package that installs all available Nginx modules
BuildArch:         noarch
%if %{with geoip}
Requires:          nginx-mod-http-geoip = %{epoch}:%{version}-%{release}
%endif
Requires:          nginx-mod-http-image-filter = %{epoch}:%{version}-%{release}
Requires:          nginx-mod-http-perl = %{epoch}:%{version}-%{release}
Requires:          nginx-mod-http-xslt-filter = %{epoch}:%{version}-%{release}
Requires:          nginx-mod-mail = %{epoch}:%{version}-%{release}
Requires:          nginx-mod-stream = %{epoch}:%{version}-%{release}
%description all-modules
Meta package that installs all available nginx modules.

%package filesystem
Summary:           The basic directory layout for the Nginx server
BuildArch:         noarch
%{?sysusers_requires_compat}
%description filesystem
The nginx-filesystem package contains the basic directory layout
for the Nginx server including the correct permissions for the
directories.

%if %{with geoip}
%package mod-http-geoip
Summary:           Nginx HTTP geoip module
BuildRequires:     GeoIP-devel
Requires:          nginx(abi) = %{nginx_abiversion}
Requires:          GeoIP
%description mod-http-geoip
%{summary}.
%endif

%package mod-http-image-filter
Summary:           Nginx HTTP image filter module
BuildRequires:     gd-devel
Requires:          nginx(abi) = %{nginx_abiversion}
Requires:          gd
%description mod-http-image-filter
%{summary}.

%package mod-http-perl
Summary:           Nginx HTTP perl module
BuildRequires:     perl-devel
BuildRequires:     perl-generators
BuildRequires:     perl(ExtUtils::Embed)
Requires:          nginx(abi) = %{nginx_abiversion}
Requires:          perl(constant)
%description mod-http-perl
%{summary}.

%package mod-http-xslt-filter
Summary:           Nginx XSLT module
BuildRequires:     libxslt-devel
Requires:          nginx(abi) = %{nginx_abiversion}
%description mod-http-xslt-filter
%{summary}.

%package mod-mail
Summary:           Nginx mail modules
Requires:          nginx(abi) = %{nginx_abiversion}
%description mod-mail
%{summary}.

%package mod-stream
Summary:           Nginx stream modules
Requires:          nginx(abi) = %{nginx_abiversion}
%description mod-stream
%{summary}.

%package mod-devel
Summary:           Nginx module development files
Requires:          nginx = %{epoch}:%{version}-%{release}
Requires:          make
Requires:          gcc
Requires:          gd-devel
%if 0%{?with_gperftools}
Requires:          gperftools-devel
%endif
%if %{with geoip}
Requires:          GeoIP-devel
%endif
Requires:          libxslt-devel
Requires:          openssl%{?openssl_pkgversion}-devel
Requires:          pcre2-devel
Requires:          perl-devel
Requires:          perl(ExtUtils::Embed)
Requires:          zlib-devel
%description mod-devel
%{summary}.

%prep

%(test -z "%{source3_key_fpr}" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source3_key_fpr}" || { echo "oreon: Source3 key fingerprint mismatch" >&2; exit 1; }; })
%(test -z "%{source4_key_fpr}" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source4_key_fpr}" || { echo "oreon: Source4 key fingerprint mismatch" >&2; exit 1; }; })
%(test -z "%{source5_key_fpr}" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source5_key_fpr}" || { echo "oreon: Source5 key fingerprint mismatch" >&2; exit 1; }; })
%(test -z "%{source6_key_fpr}" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source6_key_fpr}" || { echo "oreon: Source6 key fingerprint mismatch" >&2; exit 1; }; })
# Combine all keys from upstream into one file
cat %{S:3} %{S:4} %{S:5} %{S:6} > %{_builddir}/%{name}.gpg
%{gpgverify} --keyring='%{_builddir}/%{name}.gpg' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp %{SOURCE200} %{SOURCE10} %{SOURCE12} %{SOURCE18} %{SOURCE220} .

%if 0%{?openssl_pkgversion}
sed \
  -e 's|\(ngx_feature_path=\)$|\1%{_includedir}/openssl%{openssl_pkgversion}|' \
  -e 's|\(ngx_feature_libs="\)|\1-L%{_libdir}/openssl%{openssl_pkgversion} |' \
  -i auto/lib/openssl/conf
%endif

# Prepare template config for instances
sed -e '/^error_log /s|error\.log|@INSTANCE@_error.log|' \
    -e '/^pid /s|nginx\.pid|nginx-@INSTANCE@.pid|' \
    -e '/^ *access_log/s|access\.log|@INSTANCE@_access.log|' \
    nginx.conf >> instance.conf
touch -r %{SOURCE12} instance.conf

# Prepare sources for installation
cp -a ../%{name}-%{version} ../%{name}-%{version}-%{release}-src
mv ../%{name}-%{version}-%{release}-src .

%build

export DESTDIR=%{buildroot}
nginx_ldopts="$RPM_LD_FLAGS -Wl,-E -O2"
if ! ./configure \
    --prefix=%{_datadir}/nginx \
    --sbin-path=%{_sbindir}/nginx \
    --modules-path=%{nginx_moduledir} \
    --conf-path=%{_sysconfdir}/nginx/nginx.conf \
    --error-log-path=%{_localstatedir}/log/nginx/error.log \
    --http-log-path=%{_localstatedir}/log/nginx/access.log \
    --http-client-body-temp-path=%{_localstatedir}/lib/nginx/tmp/client_body \
    --http-proxy-temp-path=%{_localstatedir}/lib/nginx/tmp/proxy \
    --http-fastcgi-temp-path=%{_localstatedir}/lib/nginx/tmp/fastcgi \
    --http-uwsgi-temp-path=%{_localstatedir}/lib/nginx/tmp/uwsgi \
    --http-scgi-temp-path=%{_localstatedir}/lib/nginx/tmp/scgi \
    --pid-path=/run/nginx.pid \
    --lock-path=/run/lock/subsys/nginx \
    --user=%{nginx_user} \
    --group=%{nginx_user} \
    --with-compat \
    --with-debug \
%if 0%{?with_aio}
    --with-file-aio \
%endif
%if 0%{?with_gperftools}
    --with-google_perftools_module \
%endif
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_degradation_module \
    --with-http_flv_module \
%if %{with geoip}
    --with-http_geoip_module=dynamic \
    --with-stream_geoip_module=dynamic \
%endif
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_image_filter_module=dynamic \
    --with-http_mp4_module \
    --with-http_perl_module=dynamic \
    --with-http_random_index_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_v3_module \
    --with-http_xslt_module=dynamic \
    --with-mail=dynamic \
    --with-mail_ssl_module \
%if 0%{?with_ktls}
    --with-openssl-opt=enable-ktls \
%endif
%if %{without engine}
    --without-engine \
%endif
    --with-pcre \
    --with-pcre-jit \
    --with-stream=dynamic \
    --with-stream_realip_module \
    --with-stream_ssl_module \
    --with-stream_ssl_preread_module \
    --with-threads \
    --with-cc-opt="%{optflags} $(pcre2-config --cflags)" \
    --with-ld-opt="$nginx_ldopts"; then
  : configure failed
  cat objs/autoconf.err
  exit 1
fi
%make_build
%install
%make_install INSTALLDIRS=vendor
find %{buildroot} -type f -name .packlist -exec rm -f '{}' \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f '{}' \;
find %{buildroot} -type f -empty -exec rm -f '{}' \;
find %{buildroot} -type f -iname '*.so' -exec chmod 0755 '{}' \;
install -p -D -m 0644 ./nginx.service \
    %{buildroot}%{_unitdir}/nginx.service
install -p -D -m 0644 ./nginx@.service \
    %{buildroot}%{_unitdir}/nginx@.service
install -p -D -m 0644 %{SOURCE11} \
    %{buildroot}%{_sysconfdir}/logrotate.d/nginx
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/systemd/system/nginx.service.d
install -p -d -m 0755 %{buildroot}%{_unitdir}/nginx.service.d
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nginx/conf.d
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nginx/default.d
install -p -d -m 0700 %{buildroot}%{_localstatedir}/lib/nginx
install -p -d -m 0700 %{buildroot}%{_localstatedir}/lib/nginx/tmp
install -p -d -m 0700 %{buildroot}%{_localstatedir}/log/nginx
install -p -d -m 0755 %{buildroot}%{_datadir}/nginx/html
install -p -d -m 0755 %{buildroot}%{nginx_moduleconfdir}
install -p -d -m 0755 %{buildroot}%{nginx_moduledir}
install -p -m 0644 ./nginx.conf \
    %{buildroot}%{_sysconfdir}/nginx
rm -f %{buildroot}%{_datadir}/nginx/html/index.html
rm -f %{buildroot}%{_datadir}/nginx/html/50x.html
ln -s ../../testpage/index.html \
      %{buildroot}%{_datadir}/nginx/html/index.html
install -p -m 0644 %{SOURCE102} \
    %{buildroot}%{_datadir}/nginx/html
ln -s nginx-logo.png %{buildroot}%{_datadir}/nginx/html/poweredby.png
mkdir -p %{buildroot}%{_datadir}/nginx/html/icons
ln -s ../../../pixmaps/poweredby.png \
      %{buildroot}%{_datadir}/nginx/html/icons/poweredby.png
%if 0%{?with_mailcap_mimetypes}
rm -f %{buildroot}%{_sysconfdir}/nginx/mime.types
%endif
install -p -D -m 0644 %{_builddir}/nginx-%{version}/objs/nginx.8 \
    %{buildroot}%{_mandir}/man8/nginx.8
install -p -D -m 0755 %{SOURCE13} %{buildroot}%{_bindir}/nginx-upgrade
install -p -D -m 0644 %{SOURCE14} %{buildroot}%{_mandir}/man8/nginx-upgrade.8
for i in ftdetect ftplugin indent syntax; do
    install -p -D -m644 contrib/vim/${i}/nginx.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/${i}/nginx.vim
done
%if %{with geoip}
echo 'load_module "%{nginx_moduledir}/ngx_http_geoip_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-http-geoip.conf
%endif
echo 'load_module "%{nginx_moduledir}/ngx_http_image_filter_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-http-image-filter.conf
echo 'load_module "%{nginx_moduledir}/ngx_http_perl_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-http-perl.conf
echo 'load_module "%{nginx_moduledir}/ngx_http_xslt_filter_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-http-xslt-filter.conf
echo 'load_module "%{nginx_moduledir}/ngx_mail_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-mail.conf
echo 'load_module "%{nginx_moduledir}/ngx_stream_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-stream.conf
mkdir -p %{buildroot}%{_usrsrc}
mv %{name}-%{version}-%{release}-src %{buildroot}%{nginx_srcdir}
mkdir -p %{buildroot}%{_rpmmacrodir}
sed -e "s|@@NGINX_ABIVERSION@@|%{nginx_abiversion}|g" \
    -e "s|@@NGINX_MODDIR@@|%{nginx_moduledir}|g" \
    -e "s|@@NGINX_MODCONFDIR@@|%{nginx_moduleconfdir}|g" \
    -e "s|@@NGINX_SRCDIR@@|%{nginx_srcdir}|g" \
    %{SOURCE15} > %{buildroot}%{_rpmmacrodir}/macros.nginxmods
install -Dpm0644 %{SOURCE16} %{buildroot}%{_fileattrsdir}/nginxmods.attr
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -m755 $RPM_SOURCE_DIR/nginx-ssl-pass-dialog \
        $RPM_BUILD_ROOT%{_libexecdir}/nginx-ssl-pass-dialog
install -p -D -m 0644 %{SOURCE19} %{buildroot}%{_sysusersdir}/nginx.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE20} %{buildroot}%{_tmpfilesdir}/nginx.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre filesystem

%sysusers_create_compat %{SOURCE19}
%post

%systemd_post nginx.service
%if %{with geoip}
%post mod-http-geoip

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%endif
%post mod-http-image-filter

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%post mod-http-perl

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%post mod-http-xslt-filter

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%post mod-mail

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%post mod-stream

if [ $1 -eq 1 ]; then
    /usr/bin/systemctl reload nginx.service >/dev/null 2>&1 || :
fi
%preun

%systemd_preun nginx.service
%postun

%systemd_postun nginx.service
if [ $1 -ge 1 ]; then
    /usr/bin/nginx-upgrade >/dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n nginx-core -f %{oreon_filedir}/nginx-core.list
%files -n nginx-all-modules -f %{oreon_filedir}/nginx-all-modules.list
%files -n nginx-filesystem -f %{oreon_filedir}/nginx-filesystem.list
%files -n nginx-mod-http-image-filter -f %{oreon_filedir}/nginx-mod-http-image-filter.list
%files -n nginx-mod-http-perl -f %{oreon_filedir}/nginx-mod-http-perl.list
%files -n nginx-mod-http-xslt-filter -f %{oreon_filedir}/nginx-mod-http-xslt-filter.list
%files -n nginx-mod-mail -f %{oreon_filedir}/nginx-mod-mail.list
%files -n nginx-mod-stream -f %{oreon_filedir}/nginx-mod-stream.list
%files -n nginx-mod-devel -f %{oreon_filedir}/nginx-mod-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.2-1
- Prepare for Oreon 11 (RP1)
