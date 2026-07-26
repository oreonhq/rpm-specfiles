%global source0_hash fa9bb86782b915c6d730bb723f876dc9b345a617db375aaf3416ec22553cd64e

%{?!with_cache: %global with_cache 0}

Name: jwhois
Version: 4.0
Release: 83%{?dist}
URL: http://www.gnu.org/software/jwhois/
Source0: ftp://ftp.gnu.org/gnu/jwhois/jwhois-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/robert-scheck/jwhois/2bd561e06ca37cf6c2ef9f0a2e957e09f58e6972/example/jwhois.conf
Patch0: jwhois-4.0-connect.patch
Patch1: jwhois-4.0-ipv6match.patch
Patch2: jwhois-4.0-fclose.patch
Patch3: jwhois-4.0-select.patch
Patch5: jwhois-4.0-multi-homed.patch
Patch6: jwhois-4.0-libidn2.patch
Patch7: jwhois-4.0-idna.patch
Patch8: jwhois-4.0-idnfail.patch
# Patch9: adds options to force querying on ipv4 or ipv6, see rhbz#1551215
Patch9: jwhois-4.0-ipv4_ipv6.patch
Patch10: jwhois-configure-c99.patch
Patch11: jwhois-c99.patch
Patch12: jwhois-4.0-gcc15-fix.patch
License: GPL-3.0-only
Summary: Internet whois/nicname client
BuildRequires: gcc, libidn2-devel, autoconf, automake
%if %{with_cache}
BuildRequires: gdbm-devel
%endif
BuildRequires: make
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%global genname whois
%global alternative jwhois

%description
A whois client that accepts both traditional and finger-style queries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

iconv -f iso-8859-1 -t utf-8 < doc/sv/jwhois.1 > doc/sv/jwhois.1_
mv doc/sv/jwhois.1_ doc/sv/jwhois.1

cp -pf %{SOURCE1} example/jwhois.conf

autoreconf

# Create a sysusers.d config file
cat >jwhois.sysusers.conf <<EOF
g jwhois -
EOF

%build
%if %{with_cache}
%configure --enable-sgid --localstatedir=%{_localstatedir}/cache/jwhois
%else
%configure
%endif
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%if %{with_cache}
echo 'cachefile = "/var/cache/jwhois/jwhois.db";' >> $RPM_BUILD_ROOT/etc/jwhois.conf
install -m0775 -d $RPM_BUILD_ROOT/%{_localstatedir}/cache/jwhois
touch $RPM_BUILD_ROOT/%{_localstatedir}/cache/jwhois/jwhois.db
%endif

rm -f "$RPM_BUILD_ROOT"%{_infodir}/dir
%find_lang jwhois

# Make "whois.{%%alternative}" jwhois (because of localized manual pages).
echo .so man1/jwhois.1 > $RPM_BUILD_ROOT/%{_mandir}/man1/whois.%{alternative}.1

# Rename to alternative names
touch $RPM_BUILD_ROOT%{_bindir}/whois
chmod 755 $RPM_BUILD_ROOT%{_bindir}/whois
touch $RPM_BUILD_ROOT%{_mandir}/man1/whois.1

install -m0644 -D jwhois.sysusers.conf %{buildroot}%{_sysusersdir}/jwhois.conf

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%if %{with_cache}
%attr(2755,root,jwhois) %{_bindir}/jwhois
%attr(2775,root,jwhois) %{_localstatedir}/cache/jwhois/jwhois.db
%else
%attr(0755,root,root) %{_bindir}/jwhois
%endif
%ghost %verify(not md5 size mtime) %{_bindir}/whois
%{_mandir}/man1/jwhois.1*
%lang(sv) %{_mandir}/sv/man1/jwhois.1*
%{_mandir}/man1/whois.%{alternative}.*
%ghost %verify(not md5 size mtime) %{_mandir}/man1/whois.1.gz
%{_infodir}/jwhois.info.*
%config(noreplace) %{_sysconfdir}/jwhois.conf
%{_sysusersdir}/jwhois.conf

%if %{with_cache}
%pre
%endif

%post
%if 0%{?rhel} && 0%{?rhel} <= 7
if [ -f %{_infodir}/jwhois.info ]; then # --excludedocs?
    /sbin/install-info %{_infodir}/jwhois.info %{_infodir}/dir || :
fi
%endif
rm -f /usr/share/man/man1/whois.1.gz
%{_sbindir}/update-alternatives \
    --install %{_bindir}/whois \
        %{genname} %{_bindir}/jwhois 60 \
    --slave %{_mandir}/man1/whois.1.gz \
        %{genname}-man %{_mandir}/man1/whois.%{alternative}.1.gz

%preun
if [ $1 = 0 ]; then
%if 0%{?rhel} && 0%{?rhel} <= 7
    if [ -f %{_infodir}/jwhois.info ]; then # --excludedocs?
        /sbin/install-info --delete %{_infodir}/jwhois.info %{_infodir}/dir || :
    fi
%endif
    %{_sbindir}/update-alternatives --remove \
            %{genname} %{_bindir}/jwhois
fi

%changelog
%autochangelog
