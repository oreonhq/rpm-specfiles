%global source0_hash a5cdf7444d781c2ff4f5d0be14202f5d0971e00387181a49b725057fe95312d5

# Private libraries must not be exposed globally by RPM
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Summary:        World's most popular Open Source IRC bot
Name:           eggdrop
Version:        1.10.1
Release:        2%{?dist}
# Eggdrop itself is GPL-2.0-or-later but uses other source codes, breakdown:
# GPL-2.0-only: src/mod/pbkdf2.mod/{pbkdf2,tclpbkdf2}.c
# BSD-3-Clause: src/compat/inet_aton.c
# ISC: src/compat/{base64,explicit_bzero,inet_aton,strlcpy}.c
# LicenseRef-Fedora-Public-Domain: src/md5/{md5.h,md5c.c}
# MIT: doc/html/_static/{jquery,underscore}.js
License:        GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.eggheads.org/
Source0:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz
Source1:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/E01C240484DE7DBE190FE141E7667DE1D1A39AFF
Patch0:         eggdrop-1.6.17-langdir.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel >= 8.5
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  python-devel >= 3.8.0
%else
# Application Stream supported until EOL of RHEL 8
BuildRequires:  python3.12-devel
%endif

%description
Eggdrop is the world's most popular Open Source IRC bot, designed
for flexibility and ease of use. It is extendable with Tcl scripts
and/or C modules, has support for the big five IRC networks and is
able to form botnets, share partylines and userfiles between bots.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .langdir
touch -c -r doc/man1/%{name}.1{.langdir,}

%build
%configure
make config
# Parallel builds are not supported
make

%install
mkdir -p $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir},%{_mandir}/man1}/
%make_install DEST=$RPM_BUILD_ROOT%{_datadir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{README,doc,eggdrop*,filesys,logs,modules,scripts/CONTENTS}
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

# Fix paths while installing man page
sed -e 's@doc/@%{_pkgdocdir}/@g' doc/man1/%{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
touch -c -r doc/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Move modules into /usr/lib*
mv -f $RPM_BUILD_ROOT{%{_datadir}/%{name}/modules-%{version},%{_libdir}/%{name}}/

# Fix paths of example eggdrop(-basic).conf
for conf in eggdrop.conf eggdrop-basic.conf; do
  sed -e '2d' -e '1s@^.*@#!%{_bindir}/%{name}@' \
      -e 's@scripts/@%{_datadir}/%{name}/scripts/@g' \
      -e 's@help/@%{_datadir}/%{name}/help/@g' \
      -e 's@modules/@%{_libdir}/%{name}/@g' \
      -e 's@text/"@%{_datadir}/%{name}/text/"@g' \
      -e 's@/etc/ssl/@%{_sysconfdir}/pki/tls/certs/@g' \
      -e 's@^#\(set ssl-cafile\) ""@\1 "%{_sysconfdir}/pki/tls/certs/ca-bundle.crt"@g' \
      ${conf} > ${conf}.mod
  touch -c -r ${conf}{,.mod}; mv -f ${conf}{.mod,}
done

%files
%license COPYING
%doc FEATURES NEWS README doc/Changes1.10 eggdrop.conf eggdrop-basic.conf
%doc doc/ABOUT doc/ACCOUNTS doc/AUTOSCRIPTS doc/BANS doc/BOTNET doc/BUG-REPORT
%doc doc/FIRST-SCRIPT doc/IPV6 doc/IRCv3 doc/PARTYLINE doc/PBKDF2 doc/TLS
%doc doc/TRICKS doc/TWITCH doc/USERS doc/tcl-commands.doc doc/settings doc/html
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
