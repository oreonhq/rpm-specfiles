%global source0_hash 928b8260eb2d433fdd86f78a56d15f5ed804a27e75022c978f81b2c02f3aab6a
Name:           dgit
Version:        16.9.git
Release:        1%{?dist}
Summary:        Integration between git and Debian-style archives
License:        GPL-3.0-or-later
URL:            https://browse.dgit.debian.org/dgit.git/
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
Requires:       coreutils
Requires:       curl
Requires:       devscripts
Requires:       dpkg-dev
Requires:       git
Requires:       tar
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
# /oreon:deps
%description
dgit (with the associated infrastructure) makes it possible to
treat the Debian archive as a git repository:

"dgit push" constructs uploads from git commits

"dgit clone" and "dgit fetch" construct git commits from uploads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir work
%oreon_prep
%build

%check

%install
make install DESTDIR="%{buildroot}" \
        prefix="%{_prefix}" \
        bindir="%{_bindir}" \
        mandir="%{_mandir}" \
        perldir="%{perl_vendorlib}" \
        infraexamplesdir="%{_pkgdocdir}/examples"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
