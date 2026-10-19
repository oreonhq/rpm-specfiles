%global source2_hash e4978c5484d0d1ce5c218d11ba2acc304e4c5b3116078e1cd262e694baf3bedc
%global source0_hash 5f07a947b0e7d4d83e3663717028b201707ed264afb6fb19f5ebf9b16c21eadc
Name:           kefir
Version:        0.5.1
Release:        1%{?dist}
Summary:        An implementation of C17 language compiler from scratch
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://kefir.protopopov.lv
Source0:        https://%{name}.protopopov.lv/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/kefir-%{version}.tar.gz.asc
Source2:        https://www.protopopov.lv/static/files/jprotopopov.gpg 
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  libatomic
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mandoc
# /oreon:deps
%description
an implementation of C17 language compiler from scratch. No existing open
source compiler infrastructure is being reused. The main priority is
self-sufficiency of the project, compatibility with platform ABI and
compliance with C17 language standard. Any omissions or incompatibilities
between the language standard and Kefir behavior which are not explicitly
documented (see Implementation & Usage quirks section below) shall be
considered bugs.

Kefir supports modern x86-64 Linux, FreeBSD, OpenBSD and NetBSD environments
(see Supported environments section below). Compiler is also able to produce
JSON streams containing program representation on various stages of
compilation (tokens, AST, IR), as well as printing source code in preprocessed
form. The compiler targets GNU As (Intel syntax with/without prefixes and ATT
syntax are supported) and Yasm assemblers. Kefir is able to produce debug
information in DWARF5 format for GNU As. Position-independent code generation
is supported. Kefir features cc-compatible command line interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -c -n %{name}-%{version}

%build

LC_ALL=C.UTF-8 %make_build all \
    PROFILE=reldebug \
    CC=gcc \
    DESTDIR=%{buildroot} \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    sysconfdir=%{_sysconfdir}
%install
%make_install \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    sysconfdir=%{_sysconfdir}
rm -fr %{buildroot}%{_datadir}/licenses
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
