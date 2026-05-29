%global source0_hash d282c81dc706efea466481a139f9b0b28d2c1ea6a0a1f57dd761a6bc11b99ce2

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# On platforms and architectures that support it, the default is
# ‘--with dietlibc’.
#
# To use glibc-static instead, do ‘--without dietlibc’.  This results
# in a much larger (about 40 times larger) init binary.
#
# On other platforms, there is no dietlibc, so the default for those
# is ‘--without dietlibc’.
#
# See also:
# https://github.com/libguestfs/supermin/commit/9bb57e1a8d0f3b57eb09f65dd574f702b67e1c2f

%if 0%{?rhel}
%bcond_with dietlibc
%else
%ifarch aarch64 %{arm} %{ix86} %{power} s390x x86_64
%bcond_without dietlibc
%else
%bcond_with dietlibc
%endif
%endif

%if 0%{?fedora} > 40 || 0%{?rhel} > 10
%bcond_without dnf5
%else
%bcond_with dnf5
%endif

# Whether we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 5.3-development

Summary:       Tool for creating supermin appliances
Name:          supermin
Version:       5.3.5
Release:       9%{?dist}
License:       GPL-2.0-or-later

ExclusiveArch: %{kernel_arches}
%if 0%{?rhel}
# No qemu-kvm on POWER (RHBZ#1946532).
ExcludeArch:   %{power64}
%endif

URL:           http://people.redhat.com/~rjones/supermin/
Source0:        http://download.libguestfs.org/supermin/5.3-development/supermin-5.3.5.tar.gz
Source1:        http://download.libguestfs.org/supermin/5.3-development/supermin-5.3.5.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring

# Use stable owner, group and mtime in base.tar.gz
# Upstream in > 5.3.5
# https://bugzilla.redhat.com/show_bug.cgi?id=2320025
Patch1:        0001-prepare-Use-stable-owner-group-and-mtime-in-base.tar.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf, automake
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html
BuildRequires: rpm
BuildRequires: rpm-devel
%if %{with dnf5}
BuildRequires: dnf5
%else
BuildRequires: dnf
BuildRequires: dnf-plugins-core
%endif
BuildRequires: /usr/sbin/mke2fs
BuildRequires: e2fsprogs-devel
BuildRequires: findutils
%if %{with dietlibc}
BuildRequires: dietlibc-devel
%else
BuildRequires: glibc-static
%endif
BuildRequires: ocaml, ocaml-findlib-devel
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# These are required only to run the tests.  We could patch out the
# tests to not require these packages.
BuildRequires: augeas hivex kernel tar

%if 0%{?rhel}
%ifarch s390x
# On RHEL 9 s390x, kernel incorrectly pulls in kernel-zfcpdump-core
# https://bugzilla.redhat.com/show_bug.cgi?id=2027654
BuildRequires: kernel-core
%endif
%endif

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires: grubby
# https://bugzilla.redhat.com/show_bug.cgi?id=1331012
BuildRequires: systemd-udev

# This only includes the dependencies needed at runtime, ie.  supermin
# --build.  For supermin --prepare, dependencies like dnf are placed
# in the -devel subpackage.
Requires:      rpm
Requires:      util-linux-ng
Requires:      cpio
Requires:      tar
Requires:      /usr/sbin/mke2fs
# RHBZ#771310
Requires:      e2fsprogs-libs >= 1.42

# For automatic RPM dependency generation.
# See: https://rpm-software-management.github.io/rpm/manual/dependency_generators.html
Source3:       supermin.attr
Source4:       supermin-find-requires


%description
Supermin is a tool for building supermin appliances.  These are tiny
appliances (similar to virtual machines), usually around 100KB in
size, which get fully instantiated on-the-fly in a fraction of a
second when you need to boot one of them.

Note that if you want to run 'supermin --prepare' you will need the
extra dependencies provided by %{name}-devel.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      rpm-build

# Dependencies needed for supermin --prepare
%if %{with dnf5}
Requires:      dnf5
%else
Requires:      dnf
Requires:      dnf-plugins-core
%endif
Requires:      findutils


%description devel
%{name}-devel contains development tools for %{name}.

It contains extra dependencies needed for 'supermin --prepare' to
work, as well as tools for automatic RPM dependency generation from
supermin appliances.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1


%build
autoreconf -fi
# Setting DNF is temporarily required for Rawhide.  We should be able
# to remove this later.  See:
# https://bugzilla.redhat.com/show_bug.cgi?id=2209412
# https://fedoraproject.org/wiki/Changes/ReplaceDnfWithDnf5
%configure %{?with_dnf5:DNF=%{_bindir}/dnf5} --disable-network-tests

%if %{with dietlibc}
make -C init CC="diet gcc"
%endif
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/


%check

# Skip execstack test where it is known to fail.
%if 0%{?fedora} <= 20
%ifarch aarch64 %{arm}
export SKIP_TEST_EXECSTACK=1
%endif
%endif

make check || {
    cat tests/test-suite.log
    exit 1
}


%files
%doc COPYING README examples/build-basic-vm.sh
%{_bindir}/supermin
%{_mandir}/man1/supermin.1*


%files devel
%{_rpmconfigdir}/fileattrs/supermin.attr
%{_rpmconfigdir}/supermin-find-requires


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3.5-9
- Prepare for Oreon 11 (RP1)
