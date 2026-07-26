%global source0_hash 928b8260eb2d433fdd86f78a56d15f5ed804a27e75022c978f81b2c02f3aab6a

Name:           dgit
Version:        14.11
Release:        %autorelease
Summary:        Integration between git and Debian-style archives
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://browse.dgit.debian.org/dgit.git/
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
Requires:       coreutils
Requires:       curl
Requires:       devscripts
Requires:       dpkg-dev
Requires:       git
Requires:       tar
BuildArch:      noarch

%description
dgit (with the associated infrastructure) makes it possible to
treat the Debian archive as a git repository:

"dgit push" constructs uploads from git commits

"dgit clone" and "dgit fetch" construct git commits from uploads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n work

%build

%check
# dput is not packaged,
# possibly need Internet connectivity anyway
#EMAIL=jello.biafra@dead.kennedys \
#       tests/using-intree make -f tests/Makefile

%install
# We don't do an install-infra, not sure if the Debian specific
# infrastructure tools would make sense to be packaged in Fedora.
make install DESTDIR="%{buildroot}" \
        prefix="%{_prefix}" \
        bindir="%{_bindir}" \
        mandir="%{_mandir}" \
        perldir="%{perl_vendorlib}" \
        infraexamplesdir="%{_pkgdocdir}/examples"

%files
%{_bindir}/dgit
%{_bindir}/git-playtree-setup
%{_bindir}/mini-git-tag-fsck
%{_bindir}/tag2upload-fetch-inputs
%{_bindir}/tag2upload-obtain-origs
%{_datadir}/%{name}
%{_mandir}/man1/dgit*.1*
%{_mandir}/man7/dgit*.7*
%{perl_vendorlib}/Debian
%doc debian/changelog README.*
%license debian/copyright

%changelog
%autochangelog
