%global source0_hash bfb97e7de161e8d7ce113b163bda1d1a8ec77d2c1afab56dcc8153d7a90187fc

Summary:        AES-based encryption tool for tar/cpio and loop-aes imagemore
Name:           aespipe
Version:        2.4g
Release:        8%{?dist}
License:        GPL-2.0-or-later
URL:            http://loop-aes.sourceforge.net/
Source:         %{url}/aespipe/aespipe-v%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  make
Requires:       gpg

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

%autosetup -p1 -n %{name}-v%{version}

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

%files
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_mandir}/man1/aespipe.1*
%{_bindir}/aespipe

%changelog
%autochangelog
