%global source0_hash d100efbc6084f494400892ef53fa476fd6f201dba3b2fddee11ef90dd9d6111d

Name:           bees
Version:        0.10
Release:        %autorelease
Summary:        Best-Effort Extent-Same, a btrfs dedupe agent

License:        GPL-3.0-only AND MIT AND Zlib
URL:            https://github.com/Zygo/bees

Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

# https://github.com/Zygo/bees/pull/286
Patch0:         286.patch

# https://github.com/Zygo/bees/pull/309
Patch1:         309.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  btrfs-progs-devel
BuildRequires:  systemd-rpm-macros

%description
bees is a block-oriented userspace deduplication agent designed for
large btrfs filesystems. It is an offline dedupe combined with an
incremental data scan capability to minimize time data spends on disk
from write to dedupe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
cat <<EOF > localconf
BEES_VERSION=v%{version}
DEFAULT_MAKE_TARGET=all
LIBEXEC_PREFIX=%{_libexecdir}/%{name}
LIB_PREFIX=%{_libdir}
PREFIX=%{_prefix}
BINDIR=bin
SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir}
EOF

%build
%make_build

%install
%make_install

%post
%systemd_post 'bees@*.service'
 
%preun
%systemd_preun 'bees@*.service'

%postun
%systemd_postun_with_restart 'bees@*.service'

%check
make test

%files
%license COPYING
%doc README.md
%{_bindir}/beesd
%{_libexecdir}/%{name}
%{_unitdir}/beesd@.service
%{_sysconfdir}/%{name}/
%config %{_sysconfdir}/%{name}/beesd.conf.sample

%changelog
%autochangelog
