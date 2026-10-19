%global source0_hash 448fe1e58612c184951645ddd926fc5bdb64fc4f2f828c766c82aa1127e9a3e2
Summary:        AES-based encryption tool for tar/cpio and loop-aes imagemore
Name:           aespipe
Version:        2.4j
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            http://loop-aes.sourceforge.net/
Source0:        http://loop-aes.sourceforge.net//%{name}/%{name}-v%{version}.tar.bz2
Requires:       gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  make
# /oreon:deps
%description
aespipe is an encryption tool that reads from standard input and
writes to standard output. It uses the AES (Rijndael) cipher.

It can be used as an encryption filter, to create and restore
encrypted tar/cpio backup archives and to read/write and convert
loop-AES compatible encrypted images.

aespipe can be used for non-destructive in-place encryption of
existing disk partitions for use with the loop-AES encrypted loop-back
kernel module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%set_build_flags
%configure LDFLAGS="${CFLAGS}"
%global make_target %{nil}
%ifarch x86_64
%global make_target amd64
%endif
%ifarch %{ix86}
%global make_target x86
%endif
make %{?_smp_mflags} %{make_target}
%check

make tests
%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples
cp -p ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}
install -Dp -m0644 bz2aespipe %{buildroot}%{_defaultdocdir}/%{name}/examples
install -Dp -m0644 aespipe.1 %{buildroot}%{_mandir}/man1/aespipe.1
install -Dp -m0755 aespipe %{buildroot}%{_bindir}/aespipe
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
