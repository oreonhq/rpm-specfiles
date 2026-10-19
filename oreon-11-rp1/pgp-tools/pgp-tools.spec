%global source0_hash 52264331726025f413db8747795d33ef36fef318b3191a1baedfb5f59a6b534f
%global tarballname signing-party
Name:           pgp-tools
Version:        2.11
Release:        1%{?dist}
Summary:        Collection of several utilities related to OpenPGP
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
URL:            https://salsa.debian.org/stappers/pgp-tools
Source0:        http://ftp.debian.org/debian/pool/main/s/%{tarballname}/%{tarballname}_%{version}.orig.tar.gz
Patch0:         0001-pgpring-port-to-OpenSSL.patch
Patch1:         gpgwrap_makefile.diff
Requires:       %{_bindir}/gpg
Recommends:     %{_sbindir}/sendmail
Recommends:     %{_bindir}/paperconf
# oreon:deps
BuildRequires:  //bin/aclocal
BuildRequires:  //bin/autoreconf
BuildRequires:  //bin/pod2man
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(GnuPG::Interface)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl-generators
# /oreon:deps
%description
This is a collection of several projects relating to OpenPGP.

* caff: CA - Fire and Forget signs and mails a key
* pgp-clean: removes all non-self signatures from key
* pgp-fixkey: removes broken packets from keys
* gpg-mailkeys: simply mail out a signed key to its owner
* gpg-key2ps: generate PostScript file with fingerprint paper slips
* gpgdir: recursive directory encryption tool
* gpglist: show who signed which of your UIDs
* gpgsigs: annotates list of GnuPG keys with already done signatures
* gpgparticipants: create list of party participants for the organiser
* gpgwrap: a passphrase wrapper
* keyanalyze: minimum signing distance (MSD) analysis on keyrings
* keylookup: ncurses wrapper around gpg --search
* sig2dot: converts a list of GnuPG signatures to a .dot file
* springgraph: creates a graph from a .dot file
* keyart: creates a random ASCII art of a PGP key file
* gpg-key2latex: generate LaTeX file with fingerprint paper slips

For more information on each of these tools, please see their respective
manpages. Please note that each individual project has its own license,
consult the licensing information in the subdirectories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarballname}-%{version}
# fix gpgdir library path lookup as we're using system-provided libraries
sed -i -e "s,/usr/lib/gpgdir,," gpgdir/gpgdir
%patch -P0 -p1
%patch -P1 -p1

%build

%make_build \
    CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" STRIP=: CC=%{__cc}
%install
%make_install
for f in caff/{caff,pgp-clean,pgp-fixkey} \
         gpglist/gpglist \
         gpg-key2ps/gpg-key2ps \
         gpg-key2latex/gpg-key2latex \
         gpg-mailkeys/gpg-mailkeys \
         gpgparticipants/gpgparticipants{,-prefill} \
         gpgdir/gpgdir \
         gpgwrap/bin/gpgwrap \
         keyanalyze/pgpring/pgpring
do
  %{__install} -Dpm0755 -t %{buildroot}%{_bindir} $f
done
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 */*.1 */*/*.1
mv %{buildroot}%{_docdir}/{signing-party,%{expand:%{_docdir_fmt}}}
for f in $(find -type f \( -iname COPYING -o -iname LICENSE \))
do
  mv $f $(basename $f).$(basename $(dirname $f))
done
%oreon_autofiles main

%check

pushd gpgdir/test
  ./gpgdir_test.pl
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
