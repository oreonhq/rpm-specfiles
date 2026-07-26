%global source0_hash 5b028f79183659d441d1b340deb88341a7f29335ae7370eff4b3c094fbe90bc4

Name:       reprepro
Version:    5.4.4
Release:    6%{?dist}
Summary:    Tool to handle local repositories of Debian packages
# filecntl.c, md5.c, md5.h are Public Domain
# dpkgversions.c is GPLv2+
# docs/sftp.py is MIT
# Rest is GPLv2
# Automatically converted from old format: GPLv2 and GPLv2+ and MIT - review is highly recommended.
License:    GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:        https://salsa.debian.org/debian/reprepro
Source0:    https://salsa.debian.org/debian/reprepro/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  automake
%if 0%{?el6}
BuildRequires: db4-devel
%else
BuildRequires: libdb-devel
%endif
BuildRequires: zlib-devel
BuildRequires: gpgme-devel
BuildRequires: bzip2-devel
BuildRequires: libarchive-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel

%description
reprepro is a tool to manage a repository of Debian packages (.deb).  It
stores files either being injected manually or downloaded from some other
repository (partially) mirrored into one pool/ hierarchy.  Managed packages
and files are stored in a Berkeley DB, so no database server is needed.
Checking signatures of mirrored repositories and creating signatures of the
generated Package indexes is supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

# files in docs should not have executable permissions
find docs -type f -exec chmod -x {} +

# Remove py3 shebang since RHEL 7 does not provide /usr/bin/python3.
for f in docs/outstore.py docs/outsftphook.py; do
  sed -i -e 's|#!/usr/bin/python3|#!/usr/bin/python|' $f
done

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

pushd docs

# Shell completion files
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv reprepro.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/reprepro
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
mv reprepro.zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_reprepro

rm Makefile{,.am,.in} changestool.1 rredtool.1 reprepro.1

# Note: Upstream sources contain tests/test.sh, but Fedora lacks some
# dependencies to run this.

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc docs/ AUTHORS README NEWS
%{_mandir}/man1/changestool.1*
%{_mandir}/man1/reprepro.1*
%{_mandir}/man1/rredtool.1*
%{_bindir}/changestool
%{_bindir}/reprepro
%{_bindir}/rredtool
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/reprepro
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_reprepro

%changelog
%autochangelog
