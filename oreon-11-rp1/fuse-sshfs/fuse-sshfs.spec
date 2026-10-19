%global source1_hash 1682d94dac6fa82ed900ecd62e408c6403228dbf4f5b037739587efbded68363
%global source0_hash 6a1bcb31450a077e9cb1b7ff158c71de34db697c3c0da6cb362502131e495893
%global source2_key_fpr 9C113099DF707BD240A192D4C6E054D074D5DD2B
Name:           fuse-sshfs
Version:        3.7.6
Release:        1%{?dist}
Summary:        FUSE-Filesystem to access remote filesystems via SSH
License:        GPL-2.0-only
URL:            https://github.com/libfuse/sshfs
Source0:        https://github.com/libfuse/sshfs/releases/download/sshfs-%{version}/sshfs-%{version}.tar.xz
Source1:        https://github.com/libfuse/sshfs/releases/download/sshfs-%{version}/sshfs-%{version}.tar.xz.asc
Source2:        A56509CB6B3585A814B1A735C76141536EC77B36.gpg
Patch1:         sshfs-0001-Refer-to-mount.fuse3-instead-of-mount.fuse.patch
Provides:       sshfs = %{version}-%{release}
Requires:       fuse3 >= 3.1.0
Requires:       openssh-clients
Recommends:     openssh-askpass
# oreon:deps
BuildRequires:  fuse3
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  openssh-clients
BuildRequires:  python3-docutils
BuildRequires:  python3-pytest
# /oreon:deps
%description
This is a FUSE-filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to set
up: i.e. on the server side there's nothing to do.  On the client side
mounting the filesystem is as easy as logging into the server with ssh.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n sshfs-%{version}
# fix tests
sed -i "s/'fusermount'/'fusermount3'/g" test/util.py

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

cd %{_vpath_builddir}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.7.5-3
- Prepare for Oreon 11 (RP1)
