%global source0_hash f71711db9831d1e58d0fccf01cf2db83315b58da00300334d214e4de90b1759e
%global nixbld_group nixbld
%bcond docs 1
%bcond tests 0
Name:           nix
Version:        2.35.2
Release:        1%{?dist}
Summary:        A purely functional package manager
License:        LGPL-2.1-or-later
URL:            https://github.com/NixOS/nix
Source0:        https://github.com/NixOS/nix/archive/%{version}/nix-%{version}.tar.gz
Source1:        nix.conf
Source2:        registry.json
Source3:        README.md
Source4:        nix.sysusers
Source5:        nix-filesystem.conf
Patch6:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14922.patch
%ifarch x86_64 aarch64 ppc64le
%endif
%if %{with docs}
%endif
%if %{with tests}
%endif
%if %{with tests}
%endif
Requires:       nix-core = %{version}-%{release}
Requires:       nix-system = %{version}-%{release}
Recommends:     (nix-daemon = %{version}-%{release} if systemd)
Recommends:     nix-legacy = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  blake3-devel
BuildRequires:  boost-devel
BuildRequires:  boost-url
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  jq
BuildRequires:  json-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgit2-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libsodium-devel
BuildRequires:  lowdown
BuildRequires:  lowdown-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  rsync
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  toml11-devel
BuildRequires:  xz-devel
# /oreon:deps
%description
Nix is a purely functional package manager.
It allows multiple versions of a package to be installed side-by-side,
ensures that dependency specifications are complete,
supports atomic upgrades and rollbacks,
allows non-root users to install software, and has many other features.
It is the basis of the NixOS Linux distribution,
but it can be used equally well under other Unix systems.

See the README.fedora.md file for setup instructions.

%package        core
Summary:        Core nix tool
Requires:       nix-libs%{?_isa} = %{version}-%{release}
%ifarch x86_64 aarch64 ppc64le
Recommends:     busybox
%endif
%description    core
This package provides the core nix tool for modern flake-based commands.

Most users should probably install nix-legacy as well,
or the main nix package for a complete default setup.

See the README.fedora.md file for setup instructions.

%package daemon
Summary:        The nix daemon for multiuser mode
BuildArch:      noarch
Requires:       nix-core = %{version}-%{release}
Requires:       nix-system = %{version}-%{release}
Requires:       systemd
%description daemon
This package provides nix-daemon and associated files.

%package devel
Summary:        Development files for nix
Requires:       nix-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains library and header files for
developing applications that use nix.

Note the API is considered unstable and upstream does not recommend its usage.

%if %{with docs}
%package doc
Summary:        Documentation files for nix
BuildArch:      noarch
%description doc
This package contains documentation files for nix.
%endif

%package        filesystem
Summary:        Filesystem for nix
BuildArch:      noarch
Obsoletes:      nix-singleuser < %{version}-%{release}
%description    filesystem
The package provides the /nix root directory for the nix package manager.

%package        legacy
Summary:        Nix classical commands
BuildArch:      noarch
Requires:       nix-core = %{version}-%{release}
%description    legacy
This package provides the symlinks for the older nix-* commands.

%package libs
Summary:        Runtime libraries for nix
%description libs
The package provides the the runtime libraries for nix.

%if %{with tests}
%package test
Summary:        Nix test programs
Requires:       nix%{?_isa} = %{version}-%{release}
%description test
This package provides the nix-test programs.
%endif

%package        system
Summary:        Nix directories and sysusers setup
BuildArch:      noarch
Requires:       nix-filesystem = %{version}-%{release}
%description    system
This package sets up the nix directories and sysusers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

install -p -m 0644 %{SOURCE3} README.fedora.md

%build

MESON_OPTS=(
    --sysconfdir=%{_sysconfdir}
    --localstatedir=/nix/var
    --libexecdir=%{_libexecdir}
    -Dbindings=false
    -Ddoc-gen=%[%{with docs}?"true":"false"]
    -Dlibcmd:readline-flavor=readline
    -Dlibstore:sandbox-shell=%{_bindir}/busybox
    -Dnix:profile-dir=%{_sysconfdir}/profile.d
    -Dunit-tests=%[%{with tests}?"true":"false"]
    -Dlibstore:s3-aws-auth=disabled
    -Dnix-manual:html-manual=false
    -Djson-schema-checks=false
%ifarch x86_64
%else
    -Dlibutil:cpuid=disabled
%endif
    )
%meson "${MESON_OPTS[@]}"
%meson_build
%install
%meson_install
mkdir -p %{buildroot}/etc/nix
cp %{SOURCE1} %{SOURCE2} %{buildroot}/etc/nix/
mkdir -p %{buildroot}/nix/store
mkdir -p %{buildroot}/nix/var/log/nix/drvs
mkdir -p %{buildroot}/nix/var/nix
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/nix.conf
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/nix-filesystem.conf
sed -i -e '/^\.UR [@#.]/,/^\.UE/{ /^\.UR [@#.]/d; /^\.UE/d}' %{buildroot}%{_mandir}/man*/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/nix --help
%if %{with tests}
%meson_test
%endif
%post daemon

%systemd_post nix-daemon.service
%preun daemon

%systemd_preun nix-daemon.service
%postun daemon

%systemd_postun_with_restart nix-daemon.service
%files -f %{oreon_filedir}/main.list
%files -n nix-core -f %{oreon_filedir}/nix-core.list
%files -n nix-daemon -f %{oreon_filedir}/nix-daemon.list
%files -n nix-devel -f %{oreon_filedir}/nix-devel.list
%files -n nix-doc -f %{oreon_filedir}/nix-doc.list
%files -n nix-filesystem -f %{oreon_filedir}/nix-filesystem.list
%files -n nix-legacy -f %{oreon_filedir}/nix-legacy.list
%files -n nix-libs -f %{oreon_filedir}/nix-libs.list
%files -n nix-test -f %{oreon_filedir}/nix-test.list
%files -n nix-system -f %{oreon_filedir}/nix-system.list

%changelog

%autochangelog
