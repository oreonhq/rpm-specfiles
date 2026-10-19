%global source2_hash 60cf2af97fbcc789d4a40b3ba92b9072d254ee6db96d21cd22915295efc6b7b1
%global source1_hash e58b6a2b08fbd29c8fdb7ce51d09401d126b0fba25b8cb9e1394afabdf0f7f70
%global source0_hash d6646b630879e1acd9b053ffa12f46667f907145f29af1df0f82749ef3032a94
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
Summary:        World's most popular Open Source IRC bot
Name:           eggdrop
Version:        1.10.2
Release:        1%{?dist}
License:        GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.eggheads.org/
Source0:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz
Source1:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/E01C240484DE7DBE190FE141E7667DE1D1A39AFF
Patch0:         eggdrop-1.6.17-langdir.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3.12-devel
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
make
%install
mkdir -p $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir},%{_mandir}/man1}/
%make_install DEST=$RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{README,doc,eggdrop*,filesys,logs,modules,scripts/CONTENTS}
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -e 's@doc/@%{_pkgdocdir}/@g' doc/man1/%{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
touch -c -r doc/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
mv -f $RPM_BUILD_ROOT{%{_datadir}/%{name}/modules-%{version},%{_libdir}/%{name}}/
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
