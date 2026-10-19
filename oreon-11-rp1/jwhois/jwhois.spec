%global source1_hash ba0af321476745454d8252feb13e93956dbb55a958483f5db50069e6d47f6c02
%global source0_hash fa9bb86782b915c6d730bb723f876dc9b345a617db375aaf3416ec22553cd64e
%{?!with_cache: %global with_cache 0}
Name: jwhois
Version: 4.0
Release:        1%{?dist}
URL: http://www.gnu.org/software/jwhois/
Source0:        https://ftp.gnu.org/gnu/jwhois/jwhois-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/robert-scheck/jwhois/2bd561e06ca37cf6c2ef9f0a2e957e09f58e6972/example/jwhois.conf
Patch0: jwhois-4.0-connect.patch
Patch1: jwhois-4.0-ipv6match.patch
Patch2: jwhois-4.0-fclose.patch
Patch3: jwhois-4.0-select.patch
Patch5: jwhois-4.0-multi-homed.patch
Patch6: jwhois-4.0-libidn2.patch
Patch7: jwhois-4.0-idna.patch
Patch8: jwhois-4.0-idnfail.patch
Patch9: jwhois-4.0-ipv4_ipv6.patch
Patch10: jwhois-configure-c99.patch
Patch11: jwhois-c99.patch
Patch12: jwhois-4.0-gcc15-fix.patch
License: GPL-3.0-only
Summary:        Internet whois/nicname client
%if %{with_cache}
%endif
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives
%global genname whois
%global alternative jwhois
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libidn2-devel
BuildRequires:  make
# /oreon:deps
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
echo .so man1/jwhois.1 > $RPM_BUILD_ROOT/%{_mandir}/man1/whois.%{alternative}.1
touch $RPM_BUILD_ROOT%{_bindir}/whois
chmod 755 $RPM_BUILD_ROOT%{_bindir}/whois
touch $RPM_BUILD_ROOT%{_mandir}/man1/whois.1
install -m0644 -D jwhois.sysusers.conf %{buildroot}%{_sysusersdir}/jwhois.conf
%oreon_autofiles main

%pre

%endif
%post

rm -f /usr/share/man/man1/whois.1.gz
%{_sbindir}/update-alternatives \
    --install %{_bindir}/whois \
        %{genname} %{_bindir}/jwhois 60 \
    --slave %{_mandir}/man1/whois.1.gz \
        %{genname}-man %{_mandir}/man1/whois.%{alternative}.1.gz
%preun

if [ $1 = 0 ]; then
    %{_sbindir}/update-alternatives --remove \
            %{genname} %{_bindir}/jwhois
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
