%global source0_hash a01b23196ee2c4867198dfba1faf1e7610e549425fe007178646e7d3434dc3b5
%bcond_with autoreconf
%bcond_with authorcheck
%global unbundle_from_with() \
  bundled_dir="%{buildroot}%1" \
  bundled_files="$(find "${bundled_dir}" -maxdepth 1 -type f -printf '%f\\n')" \
  original_dir="%2" \
  for file in ${bundled_files} \
  do \
    if [ -f "${original_dir}/${file}" ] \
    then \
      rm -f "${bundled_dir}/${file}" \
      ln -s "${original_dir}/${file}" "${bundled_dir}/${file}" \
    fi \
  done
%global unbundle_fontawesome       0%{?fc39}
%global unbundle_raleway           0
%global unbundle_foundation        0
%global unbundle_html5shiv         0
%global unbundle_jquery            0%{?fedora}%{?el8}%{?el9}%{?el10}
%global unbundle_jquery_migrate    0
%global unbundle_jquery_minicolors 0
%global unbundle_jquery_ui         0%{?fedora}%{?el8}%{?el9}%{?el10}
%global unbundle_jqplot            0
%global unbundle_respond           0
%global licenses_bundled     %{nil} 
%if ! %{unbundle_fontawesome}
%global licenses_bundled %{licenses_bundled} AND (OFL-1.1-RFN AND MIT)
%endif
%if ! %{unbundle_raleway}
%global licenses_bundled %{licenses_bundled} AND OFL-1.1-RFN
%endif
%if ! %{unbundle_foundation} || ! %{unbundle_jquery} || ! %{unbundle_jquery_migrate} || ! %{unbundle_jquery_minicolors} || ! %{unbundle_jquery_ui} || ! %{unbundle_respond}
%global licenses_bundled %{licenses_bundled} AND MIT
%endif
%if ! %{unbundle_html5shiv} || ! %{unbundle_jqplot}
%global licenses_bundled %{licenses_bundled} and (MIT OR GPL-2.0-only)
%endif
%global static_content %{_datadir}/sympa/static_content
Name:        sympa
Version:     6.2.80
Release:        1%{?dist}
Summary:        Powerful multilingual List Manager
Summary(fr): Gestionnaire de listes électroniques
Summary(ja): 高機能で多言語対応のメーリングリスト管理ソフトウェア
License:     GPL-2.0-or-later%{licenses_bundled}
URL:         http://www.sympa.org
Source0:        https://github.com/%{name}-community/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source101:   sympa-httpd24-spawn_fcgi.conf
Source102:   sympa-lighttpd.conf
Source103:   sympa-nginx-spawn_fcgi.conf
Source106:   sympa-rsyslog.conf
Source107:   sympa-logrotate.conf
Source113:   sympa-systemd-README.RPM.md
Source114:   aliases.sympa.sendmail
Source115:   aliases.sympa.postfix
Source129:   sympa.service.d-dependencies.conf
Source130:   sympa-sysconfig
Patch13:     sympa-6.2.57b.1-confdef.patch
%if %{with autoreconf}
%endif
%if %{with authorcheck}
%endif
%{?systemd_requires}
Requires:    smtpdaemon
Requires:    mhonarc
Requires:    logrotate
Requires:    perl(DBD::mysql)
Requires:    perl(FCGI)
Requires:    perl(Archive::Zip::SimpleZip)
Requires:    perl(AuthCAS)
Requires:    perl(Clone)
Requires:    perl(Crypt::CipherSaber)
Requires:    perl(Crypt::Eksblowfish)
Requires:    perl(Crypt::OpenSSL::X509)
Requires:    perl(Crypt::SMIME)
Requires:    perl(Data::Password)
Requires:    perl(DateTime::TimeZone)
Requires:    perl(DBD::CSV)
Requires:    perl(Encode::Locale)
Requires:    perl(Encode::EUCJPASCII)
Requires:    perl(Encode::HanExtra)
Requires:    perl(IO::Socket::IP)
Requires:    perl(IO::Socket::SSL)
Requires:    perl(List::Util::XS)
Requires:    perl(LWP::Protocol::https)
Requires:    perl(Mail::DKIM::Verifier)
Requires:    perl(Net::DNS)
Requires:    perl(Net::SMTP)
Requires:    perl(Unicode::Normalize)
Requires:    perl(Unicode::UTF8)
%if %{unbundle_fontawesome}
Requires:      fontawesome-fonts-web >= 6.4.0
%else
Provides:      bundled(fontawesome-fonts) = 6.4.0
%endif
Provides:      bundled(impallari-raleway-fonts) = 3.0
Provides:      bundled(js-foundation) = 6.4.2
Provides:      bundled(js-what-input) = 4.2.0
Provides:      bundled(js-html5shiv) = 3.7.2
%if %{unbundle_jquery}
Requires:      js-jquery3 >= 3.5.0
%else
Provides:      bundled(js-jquery) = 3.6.0
%endif
Provides:      bundled(js-jquery-migrate) = 1.4.1
Provides:      bundled(js-jquery-minicolors) = 2.3.6
%if %{unbundle_jquery_ui}
Requires:      js-jquery-ui >= 1.13.2
%else
Provides:      bundled(js-jquery-ui) = 1.13.2
%endif
Provides:      bundled(js-jquery-jqplot) = 1.0.8
Provides:      bundled(js-respond) = 1.4.2
%global __requires_exclude perl\\(Conf\\)
%global __provides_exclude perl\\(Conf\\)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  js-jquery-ui
BuildRequires:  js-jquery3
BuildRequires:  make
BuildRequires:  perl(Archive::Zip::SimpleZip)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(CGI::Fast)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Singleton)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Password)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Encode::MIME::Header)
BuildRequires:  perl(English)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::NFSLock)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::StripScripts::Parser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Locale::Messages)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Charset)
BuildRequires:  perl(MIME::EncWords)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Field::ParamVal)
BuildRequires:  perl(MIME::Head)
BuildRequires:  perl(MIME::Lite::HTML)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(MIME::Tools)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(SOAP::Transport::HTTP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Template)
BuildRequires:  perl(Term::ProgressBar)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Net::LDAP)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::LineFold)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::UTF8)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  tzdata
# /oreon:deps
%description
Sympa is scalable and highly customizable mailing list manager. It
can cope with big lists (200,000 subscribers) and comes with a
complete (user and admin) Web interface. It is internationalized,
and supports the us, fr, de, es, it, fi, and chinese locales. A
scripting language allows you to extend the behavior of commands.
Sympa can be linked to an LDAP directory or an RDBMS to create
dynamic mailing lists. Sympa provides S/MIME-based authentication
and encryption.

%description -l ja
Sympa はスケーラブルで高いカスタマイズ性を持つメーリングリスト管理
ソフトウェアです。巨大なリスト (登録者数 200,000) にも適用でき、完
全な (一般ユーザ用および管理者用) ウェブインタフェースをそなえてい
ます。国際化されており、多数の言語に対応します。内蔵のスクリプティ
ング言語でコマンドの動作を拡張できます。Sympa はまた、LDAP ディレ
クトリや RDBMS と連携して動的なメーリングリストを作成できます。ま
た、S/MIME に基づく認証や暗号化もできます。

%package httpd
Summary:  Sympa with Apache HTTP Server
Summary(fr): Sympa avec Serveur HTTP Apache
Summary(ja): SympaのApache HTTP Server対応
Requires: %{name} = %{version}-%{release}
Requires: httpd
Requires: multiwatch
Conflicts: %{name}-lighttpd, %{name}-nginx
%description httpd
Apache HTTP Server support for Sympa.

%description httpd -l ja
Sympa の Apache HTTP Server 対応。

%package lighttpd
Summary:  Sympa with lighttpd
Summary(fr): Sympa avec lighttpd
Summary(ja): Sympaのlighttpd対応
Requires: %{name} = %{version}-%{release}
Requires: lighttpd
Requires: lighttpd-fastcgi
Conflicts: %{name}-httpd, %{name}-nginx
%description lighttpd
lighttpd support for Sympa.

%description lighttpd -l ja
Sympa の lighttpd 対応。

%package nginx
Summary:  Sympa with nginx
Summary(fr): Sympa avec nginx
Summary(ja): Sympaのnginx対応
Requires: %{name} = %{version}-%{release}
Requires: nginx
Requires: multiwatch
Conflicts: %{name}-httpd, %{name}-lighttpd
%description nginx
nginx support for Sympa.

%description nginx -l ja
Sympa の nginx 対応。

%package devel-doc
Summary: Sympa devel doc
Requires: %{name} = %{version}-%{release}
%description devel-doc
Sympa documentation for developers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?pre_rel}
%patch -P13 -p0 -b .confdef

# Create a sysusers.d config file
cat >sympa.sysusers.conf <<EOF
u sympa - 'System User for Sympa' %{_localstatedir}/lib/sympa -
EOF

%build

%if %{with autoreconf}
autoreconf --install
%endif
%configure \
    --enable-fhs \
    --prefix=%{_prefix} \
    --bindir=%{_libexecdir}/sympa \
    --docdir=%{_docdir}/%{name} \
    --libexecdir=%{_libexecdir}/sympa \
    --localstatedir=%{_localstatedir} \
    --sysconfdir=%{_sysconfdir}/sympa \
    --with-cgidir=%{_libexecdir}/sympa \
    --with-confdir=%{_sysconfdir}/sympa \
    --without-initdir \
    --with-unitsdir=%{_unitdir} \
    --with-piddir=%{_rundir}/sympa \
    --with-smrshdir=%{_sysconfdir}/smrsh \
    --with-aliases_file=%{_localstatedir}/lib/sympa/sympa_aliases \
    --with-perl=%{_bindir}/perl \
    --with-staticdir=%{static_content} \
    --with-cssdir=%{_localstatedir}/lib/sympa/css \
    --with-picturesdir=%{_localstatedir}/lib/sympa/pictures \
    INSTALL_DATA='install -c -p -m 644'
%make_build
rm -f previous_sympa_version
pushd po/sympa; rm -f stamp-po; make; popd
pushd po/web_help; rm -f stamp-po; make; popd
%install
%make_install
%find_lang %{name}
%find_lang web_help
%if %{unbundle_fontawesome}
%unbundle_from_with %{static_content}/fonts/font-awesome/webfonts %{_datadir}/fontawesome/webfonts
%unbundle_from_with %{static_content}/fonts/font-awesome/css %{_datadir}/fontawesome/css
%endif
%if %{unbundle_jquery}
%unbundle_from_with %{static_content}/js %{_datadir}/javascript/jquery/3
%endif
%if %{unbundle_jquery_ui}
%unbundle_from_with %{static_content}/js/jquery-ui %{_datadir}/javascript/jquery-ui
%endif
mv %{buildroot}%{_sysconfdir}/sympa/data_structure.version \
    %{buildroot}%{_sysconfdir}/sympa/data_structure.current_version
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/httpd/conf.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd/conf.d
install -m 0644 %{SOURCE102} %{buildroot}%{_sysconfdir}/lighttpd/conf.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -m 0644 %{SOURCE103} %{buildroot}%{_sysconfdir}/nginx/conf.d/sympa.conf
install -m 0644 service/wwsympa-multiwatch.service \
    %{buildroot}%{_unitdir}/wwsympa.service
install -m 0644 service/wwsympa-multiwatch.socket \
    %{buildroot}%{_unitdir}/wwsympa.socket
install -m 0644 service/sympasoap-multiwatch.service \
    %{buildroot}%{_unitdir}/sympasoap.service
install -m 0644 service/sympasoap-multiwatch.socket \
    %{buildroot}%{_unitdir}/sympasoap.socket
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d
cat > %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-httpd.conf << EOF
[Socket]
SocketUser=apache
EOF
cat > %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-nginx.conf << EOF
[Socket]
SocketUser=nginx
EOF
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d
cat > %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-httpd.conf << EOF
[Socket]
SocketUser=apache
EOF
cat > %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-nginx.conf << EOF
[Socket]
SocketUser=nginx
EOF
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 service/sympa-tmpfiles.conf \
    %{buildroot}%{_tmpfilesdir}/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d
install -m 0644 %{SOURCE129} \
    %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d/dependencies.conf
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE130} %{buildroot}%{_sysconfdir}/sysconfig/sympa
mv %{buildroot}%{_docdir}/%{name} __doc
cp -p AUTHORS.md CONTRIBUTING.md NEWS.md README.md __doc/
cp -p %{SOURCE113} __doc/README.RPM.md
mv %{buildroot}%{_sysconfdir}/sympa/README __doc/
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_sysconfdir}/sympa/README
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_datadir}/sympa/default/README
install -m 0644 %{SOURCE114} %{SOURCE115} %{buildroot}%{_sysconfdir}/sympa/
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.sendmail.db
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.postfix.db
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
install -m 0644 %{SOURCE106} %{buildroot}%{_sysconfdir}/rsyslog.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE107} %{buildroot}%{_sysconfdir}/logrotate.d/sympa
for conffile in \
    auth.conf charset.conf create_list.conf \
    edit_list.conf nrcpt_by_domain.conf topics.conf \
    mime.types sympa.wsdl ;
    do cp -a %{buildroot}%{_datadir}/%{name}/default/$conffile \
        %{buildroot}%{_sysconfdir}/%{name}/;
done
mkdir -p %{buildroot}%{_localstatedir}/lib/sympa/X509-user-certs
install -m0644 -D sympa.sysusers.conf %{buildroot}%{_sysusersdir}/sympa.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%if %{with authorcheck}
make authorcheck || true
%endif
%pre

if [ $1 -gt 1 ]; then
    if [ -d %{_localstatedir}/lib/%{name}/static_content/css ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/css/* \
            %{_localstatedir}/lib/%{name}/css/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/css/
    fi
    if [ -d %{_localstatedir}/lib/%{name}/static_content/pictures ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/pictures/* \
            %{_localstatedir}/lib/%{name}/pictures/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/pictures/
    fi
    if [ ! -d %{_localstatedir}/lib/%{name}/static_content/css \
        -a ! -d %{_localstatedir}/lib/%{name}/static_content/pictures \
        -a -d %{_localstatedir}/lib/%{name}/static_content ]; then
        rm -r %{_localstatedir}/lib/%{name}/static_content/
    fi
fi
exit 0
%post

%systemd_post sympa.service
function create_cookie {
    cook=`mktemp`
    perl -ne 'chomp $_; print $1 if /^cookie\s+(\S.*)/' \
        %{_sysconfdir}/sympa/sympa.conf > $cook
    if [ '!' -s $cook ]; then
        if [ -e %{_sysconfdir}/sympa/cookies.history ]; then
            cp -p %{_sysconfdir}/sympa/cookies.history $cook
        else
            dd if=/dev/urandom bs=2048 count=1 2>/dev/null | md5sum | \
            cut -d" " -f1 > $cook
        fi
        perl -i -pe '/^#cookie\s/ and $_ = "cookie ".`cat '$cook'`."\n"' \
            %{_sysconfdir}/sympa/sympa.conf
    fi
    rm -f $cook
}
function create_config {
    if [ '!' -e %{_sysconfdir}/sympa/data_structure.version ]; then
        cp -p %{_sysconfdir}/sympa/data_structure.current_version \
            %{_sysconfdir}/sympa/data_structure.version
    fi
    if [ '!' -e %{_localstatedir}/lib/sympa/sympa_aliases ]; then
        touch %{_localstatedir}/lib/sympa/sympa_aliases
        chown sympa:sympa %{_localstatedir}/lib/sympa/sympa_aliases
        chmod 644 %{_localstatedir}/lib/sympa/sympa_aliases
        touch %{_localstatedir}/lib/sympa/sympa_aliases.db
        chown sympa:root %{_localstatedir}/lib/sympa/sympa_aliases.db
        chmod 664 %{_localstatedir}/lib/sympa/sympa_aliases.db
    fi
}
function upgrade_data_structure {
    if systemctl is-active sympa > /dev/null 2>&1; then
        /usr/bin/systemctl stop sympa > /dev/null 2>&1
        ACTIVE="yes"
    fi
    rm -f %{_sysconfdir}/sympa/sympa.conf.bin > /dev/null 2>&1
    if %{_sbindir}/sympa.pl --upgrade > /dev/null 2>&1; then
        if [ "$ACTIVE" == "yes" ]; then
            /usr/bin/systemctl start sympa > /dev/null 2>&1
        fi
    else
        echo ============================================================
        echo Notice: Failed upgrading data structure.  See logfile.
        echo Sympa is stopped.
        echo ============================================================
    fi
}
if [ $1 -eq 1 ]; then
    create_cookie
    create_config
    echo ============================================================
    echo Sympa had been installed successfully.  If you installed
    echo Sympa at first time, please read:
    echo %{_docdir}/%{name}-%{version}/README.RPM.md
    echo ============================================================
fi
if [ $1 -gt 1 ]; then
    upgrade_data_structure
fi
%preun

%systemd_preun sympa.service
%postun

%systemd_postun_with_restart sympa.service
%post httpd

%systemd_post wwsympa.service
%systemd_post sympasoap.service
%preun httpd

%systemd_preun wwsympa.service
%systemd_preun sympasoap.service
%postun httpd

%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service
%systemd_preun wwsympa.service
%systemd_preun sympasoap.service
%post nginx

%systemd_post wwsympa.service
%systemd_post sympasoap.service
%postun nginx

%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service
%files -f %{oreon_filedir}/main.list
%files -n sympa-httpd -f %{oreon_filedir}/sympa-httpd.list
%files -n sympa-lighttpd -f %{oreon_filedir}/sympa-lighttpd.list
%files -n sympa-nginx -f %{oreon_filedir}/sympa-nginx.list
%files -n sympa-devel-doc -f %{oreon_filedir}/sympa-devel-doc.list

%changelog

%autochangelog
