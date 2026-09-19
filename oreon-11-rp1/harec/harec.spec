%global source0_hash e2038a6feeadcd6d4dfd7d7ab000bec91f32617720632829f5658916cd3cb17a

%undefine _auto_set_build_flags

%global srcver  0.25.2
%global pkgsrc  %{srcver}%{?srcpre:-%{srcpre}}

Name:           harec
Version:        %{srcver}%{?srcpre:~%{srcpre}}
Release:        %autorelease
Summary:        Hare bootstrap compiler

License:        GPL-3.0-only
URL:            https://git.sr.ht/~sircmpwn/harec
Source0:        %{url}/archive/%{pkgsrc}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  qbe
Requires:       qbe

ExclusiveArch:  %hare_arches

%description
This is a Hare compiler written in C11 for POSIX-compatible systems.
It is intended as a bootstrap compiler and using the Hare standard
library is recommended for production use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{pkgsrc}

%conf
# This is a modified copy of the configs/linux.mk template stripped of
# developer flags, relying on RPM macros where applicable. Changes for
# config.mk are usually highlighted in release notes, but changes to
# the configs/linux.mk template should be checked before upgrading to
# a new release.
tee config.mk <<'EOF'
# install locations
PREFIX = %{_prefix}
BINDIR = %{_bindir}

# variables used during build
PLATFORM = %{_os}
ARCH = %{_arch}
HARECFLAGS =
QBEFLAGS =
ASFLAGS =
LDLINKFLAGS = --gc-sections -z noexecstack
CFLAGS = -std=c11 -D_XOPEN_SOURCE=700 -Iinclude %{build_cflags}
LDFLAGS = %{build_ldflags}
LIBS = -lm

CC = gcc
AS = as
LD = ld
QBE = qbe

# build locations
HARECACHE = .cache
BINOUT = .bin

# variables that will be embedded in the binary with -D definitions
DEFAULT_TARGET = $(ARCH)
VERSION = %{version}-%{release}
EOF

%build
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc README.md docs/*.txt
%{_bindir}/harec

%changelog
%autochangelog
