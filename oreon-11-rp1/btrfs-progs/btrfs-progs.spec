%global source0_hash d1f55cc2971398c9142eaa79d203e63d586a3b4b867f956664a1d68322cd4e34

%global source2_key_fpr F2B41200C54EFB30380C1756C565D5F9D76D583B

# Local definition of version_no_tilde when it doesn't exist
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

Name:           btrfs-progs
Version:        7.1
Release:        1%{?dist}
Summary:        Userspace programs for btrfs

License:        GPL-2.0-only
URL:            https://btrfs.readthedocs.io
Source0:        https://www.kernel.org/pub/linux/kernel/people/kdave/%{name}/%{name}-v%{version_no_tilde}.tar.xz
Source1:        https://www.kernel.org/pub/linux/kernel/people/kdave/%{name}/%{name}-v%{version_no_tilde}.tar.sign
Source2:        gpgkey-F2B41200C54EFB30380C1756C565D5F9D76D583B.gpg

# Special patch source, conditionally applied
## Disable RAID56 modes (RHEL-only)
Source1001:        1001-balance-mkfs-Disable-raid56-modes.patch

BuildRequires:  gnupg2
BuildRequires:  gcc, autoconf, automake, make
BuildRequires:  git-core
BuildRequires:  e2fsprogs-devel
BuildRequires:  libacl-devel, lzo-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libgcrypt) >= 1.8.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libzstd) >= 1.0.0
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  systemd
BuildRequires:  python3-devel >= 3.4

%description
The btrfs-progs package provides all the userspace programs needed to create,
check, modify and correct any inconsistencies in the btrfs filesystem.

%package -n libbtrfs
Summary:        btrfs filesystem-specific runtime libraries
License:        GPL-2.0-only
# Upstream deprecated this library
Provides:       deprecated()
# This was not properly split out before
Conflicts:      %{name} < 4.20.2

%description -n libbtrfs
libbtrfs contains the main library used by btrfs
filesystem-specific programs.

%package -n libbtrfsutil
Summary:        btrfs filesystem-specific runtime utility libraries
License:        LGPL-2.1-or-later
# This was not properly split out before
Conflicts:      %{name}-devel < 4.20.2

%description -n libbtrfsutil
libbtrfsutil contains an alternative utility library used by btrfs
filesystem-specific programs.

%package devel
Summary:        btrfs filesystem-specific libraries and headers
# libbtrfsutil is LGPLv2+
License:        GPL-2.0-only and LGPL-2.1-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       libbtrfs%{?_isa} = %{version}-%{release}
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}

%description devel
btrfs-progs-devel contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

It includes development files for two libraries:
- libbtrfs (GPLv2)
- libbtrfsutil (LGPLv2+)

You should install btrfs-progs-devel if you want to develop
btrfs filesystem-specific programs.

%package -n python3-btrfsutil
Summary:        Python 3 bindings for libbtrfsutil
License:        LGPL-2.1-or-later
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-btrfsutil}

%description -n python3-btrfsutil
python3-btrfsutil contains Python 3 bindings to the libbtrfsutil library,
which can be used for btrfs filesystem-specific programs in Python.

You should install python3-btrfsutil if you want to use or develop
btrfs filesystem-specific programs in Python.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -n %{name}-v%{version_no_tilde} -S git_am

%if 0%{?rhel}
# Specially apply this source
%{?__scm_source_timestamp:GIT_COMMITTER_DATE=%{__scm_source_timestamp}} git am --reject %{SOURCE1001}
%endif

# this generates version.py so we have to run it early
./autogen.sh
%configure CFLAGS="%{optflags} -fno-strict-aliasing" --with-crypto=libgcrypt --disable-python

%generate_buildrequires
pushd libbtrfsutil/python >/dev/null
%pyproject_buildrequires
popd >/dev/null


%build
%make_build

pushd libbtrfsutil/python
%pyproject_wheel
popd


%install
%make_install mandir=%{_mandir} bindir=%{_sbindir} libdir=%{_libdir} incdir=%{_includedir}
install -Dpm0644 btrfs-completion %{buildroot}%{_datadir}/bash-completion/completions/btrfs
# Nuke the static lib
rm -v %{buildroot}%{_libdir}/*.a

pushd libbtrfsutil/python >/dev/null
%pyproject_install
%pyproject_save_files -L btrfsutil
popd >/dev/null


%files
%license COPYING
%{_sbindir}/btrfsck
%{_sbindir}/fsck.btrfs
%{_sbindir}/mkfs.btrfs
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-select-super
%{_sbindir}/btrfstune
%{_sbindir}/btrfs
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-find-root
%{_mandir}/man5/*btrfs*
%{_mandir}/man8/*btrfs*
%{_udevrulesdir}/64-btrfs-dm.rules
%{_udevrulesdir}/64-btrfs-zoned.rules
%{_datadir}/bash-completion/completions/btrfs

%files -n libbtrfs
%license COPYING
%{_libdir}/libbtrfs.so.0*

%files -n libbtrfsutil
%license libbtrfsutil/COPYING
%{_libdir}/libbtrfsutil.so.1*

%files devel
%{_includedir}/btrfs/
%{_includedir}/btrfsutil.h
%{_libdir}/libbtrfs.so
%{_libdir}/libbtrfsutil.so
%{_libdir}/pkgconfig/libbtrfsutil.pc
%{_mandir}/man2/*btrfs*

%files -n python3-btrfsutil -f %{pyproject_files}
%license libbtrfsutil/COPYING


%changelog
%autochangelog
