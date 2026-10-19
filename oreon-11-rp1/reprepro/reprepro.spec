%global source0_hash 10b72d436cc33d2519efc14b2e9745b8a2c24bb93c2a01c1010c6fe0ea37111c
Name:       reprepro
Version:    5.5.1
Release:        1%{?dist}
Summary:        Tool to handle local repositories of Debian packages
License:    GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:        https://salsa.debian.org/debian/reprepro
Source0:        https://salsa.debian.org/debian/reprepro/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
%if 0%{?el6}
%else
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  gpgme-devel
BuildRequires:  libarchive-devel
BuildRequires:  libdb-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv reprepro.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/reprepro
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
mv reprepro.zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_reprepro
rm Makefile{,.am,.in} changestool.1 rredtool.1 reprepro.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
