%global source1_hash d0e9145ea04c76626fb1a441382223ddfd278abac750d56680a55349b7d82cdf
%global source0_hash d282c81dc706efea466481a139f9b0b28d2c1ea6a0a1f57dd761a6bc11b99ce2
%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0
ExcludeArch: %{ix86}
%ifarch aarch64 %{arm} %{ix86} %{power} s390x x86_64
%bcond_without dietlibc
%else
%bcond_with dietlibc
%endif
%bcond_with dnf5
%global verify_tarball_signature 1
%global source_directory 5.3-development
Summary:        Tool for creating supermin appliances
Name:          supermin
Version:       5.3.5
Release:        1%{?dist}
License:       GPL-2.0-or-later
ExclusiveArch: %{kernel_arches}
URL:           http://people.redhat.com/~rjones/supermin/
Source0:        https://download.libguestfs.org/%{name}/%{source_directory}/%{name}-%{version}.tar.gz
Source1:        https://download.libguestfs.org/supermin/%{source_directory}/%{name}-%{version}.tar.gz.sig
Source2:        libguestfs.keyring
Patch1:        0001-prepare-Use-stable-owner-group-and-mtime-in-base.tar.patch
%if %{with dnf5}
%else
%endif
%if %{with dietlibc}
%else
%endif
%if 0%{verify_tarball_signature}
%endif
Requires:      rpm
Requires:      util-linux-ng
Requires:      cpio
Requires:      tar
Requires:      /usr/sbin/mke2fs
Requires:      e2fsprogs-libs >= 1.42
Source3:        supermin.attr
Source4:        supermin-find-requires
# oreon:deps
BuildRequires:  /usr/bin/pod2html
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/sbin/mke2fs
BuildRequires:  augeas
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dnf
BuildRequires:  dnf-plugins-core
BuildRequires:  e2fsprogs-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  gnupg2
BuildRequires:  grubby
BuildRequires:  hivex
BuildRequires:  kernel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  rpm
BuildRequires:  rpm-devel
BuildRequires:  systemd-udev
BuildRequires:  tar
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1

%build

autoreconf -fi
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check || {
    cat tests/test-suite.log
    exit 1
}
%files -f %{oreon_filedir}/main.list
%files -n supermin-devel -f %{oreon_filedir}/supermin-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3.5-9
- Prepare for Oreon 11 (RP1)
