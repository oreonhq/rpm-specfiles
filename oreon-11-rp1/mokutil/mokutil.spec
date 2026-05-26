# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 839d677c4fc9805f1565703ca32863e4652692c53da66a88ae9b9e30676f9e17
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           mokutil
Version:        0.7.2
Release:        4%{?dist}
Epoch:          2
Summary:        Tool to manage UEFI Secure Boot MoK Keys
License:        GPL-3.0-or-later
URL:            https://github.com/lcp/mokutil
Source0:        https://github.com/lcp/mokutil/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64 aarch64 %{arm} riscv64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  efivar-devel >= 31-1
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gnu-efi
BuildRequires:  keyutils-libs-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  libxcrypt-devel
Conflicts:      shim < 0.8-1%{?dist}
Obsoletes:      mokutil < 0.2.0

Patch0001: 0001-mokutil-remove-unused-int_to_b64.patch
Patch0002: 0002-mokutil.c-show-help-if-no-args-or-help-even-on-unsup.patch

%description
mokutil provides a tool to manage keys for Secure Boot through the MoK
("Machine's Own Keys") mechanism.

%prep
%oreon_verify_sources
%autosetup -S git_am -b 0 -T

%build
./autogen.sh
%configure
%{make_build}

%install
%{make_install}

%files
%license COPYING
%doc README
%{_bindir}/mokutil
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/mokutil

%changelog
* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-4
- Inline Patch lines (drop %%include mokutil.patches for spectool)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-4
- Prepare for Oreon 11 (RP1)
