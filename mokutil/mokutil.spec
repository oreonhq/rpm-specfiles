Name:           mokutil
Version:        0.7.2
Release:        4%{?dist}
Epoch:          2
Summary:        Tool to manage UEFI Secure Boot MoK Keys
License:        GPL-3.0-or-later
URL:            https://github.com/lcp/mokutil
Source0:        https://github.com/lcp/mokutil/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        mokutil.patches
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

%include %{SOURCE1}

%description
mokutil provides a tool to manage keys for Secure Boot through the MoK
("Machine's Own Keys") mechanism.

%prep
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-4
- Prepare for Oreon 11 (RP1)
