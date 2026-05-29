%global source0_hash 0e45db63c2d00919db3174134fa234c6e0682d6fe573c46312d1d53d1d61a8bb

Name:           fuse-sshfs
Version:        3.7.5
Release:        3%{?dist}
Summary:        FUSE-Filesystem to access remote filesystems via SSH
License:        GPL-2.0-only
URL:            https://github.com/libfuse/sshfs
Source0:        https://github.com/libfuse/sshfs/releases/download/sshfs-3.7.5/sshfs-3.7.5.tar.xz
Source1:        https://github.com/libfuse/sshfs/releases/download/sshfs-3.7.5/sshfs-3.7.5.tar.xz.asc
# Find which key was used for signing the release:
#
# $ LANG=C gpg --verify sshfs-3.7.3.tar.xz.asc sshfs-3.7.3.tar.xz
# gpg: Signature made Thu May 26 15:23:53 2022 CEST
# gpg:                using RSA key ED31791B2C5C1613AF388B8AD113FCAC3C4E599F
# gpg: Can't check signature: No public key
#
# Now export the key required as follows:
#
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key ED31791B2C5C1613AF388B8AD113FCAC3C4E599F
# gpg --no-default-keyring --keyring ./keyring.gpg  --output ED31791B2C5C1613AF388B8AD113FCAC3C4E599F.gpg --export
Source2:        A56509CB6B3585A814B1A735C76141536EC77B36.gpg

Patch1:         sshfs-0001-Refer-to-mount.fuse3-instead-of-mount.fuse.patch

Provides:       sshfs = %{version}-%{release}
Requires:       fuse3 >= 3.1.0
Requires:       openssh-clients
Recommends:     openssh-askpass

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  fuse3-devel >= 3.1.0
BuildRequires:  glib2-devel >= 2.0
BuildRequires:  openssh-clients
# for man page
BuildRequires:  python3-docutils
# for tests
BuildRequires:  fuse3
BuildRequires:  python3-pytest


%description
This is a FUSE-filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to set
up: i.e. on the server side there's nothing to do.  On the client side
mounting the filesystem is as easy as logging into the server with ssh.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n sshfs-%{version}
# fix tests
sed -i "s/'fusermount'/'fusermount3'/g" test/util.py


%build
%meson
%meson_build


%install
%meson_install


%check
cd %{_vpath_builddir}
# FIXME requires sshd running? Previously tests were just skipped.
#python3 -m pytest test/


%files
%doc AUTHORS README.md ChangeLog.rst
%license COPYING
%{_bindir}/sshfs
%{_sbindir}/mount.sshfs
%{_sbindir}/mount.fuse.sshfs
%{_mandir}/man1/sshfs.1.gz


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.7.5-3
- Prepare for Oreon 11 (RP1)
