%global source0_hash 0f315b36e7d1ba74bfc97ab9f304f0a3072c47578bbe5e42594acae381f9acfe
Name:           efitools
Version:        1.9.2
Release:        1%{?dist}
Summary:        Tools to manipulate EFI secure boot keys and signatures
License:        GPL-2.0-only and LGPL-2.1-or-later and BSD-2-Clause
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/%{name}.git/snapshot/%{name}-%{version}.tar.gz
Patch1:         makefile-enable-harden-local-files.patch
Patch2:         fix-deps.patch
Patch3:         allow-riscv64-build.patch
Patch4:         sbat-compat.patch
Patch5:         fix-ftbfs-lp2083030.patch
Patch6:         drop-engine-options.patch
ExclusiveArch:  %{efi}
Requires:       coreutils
Requires:       mtools
Requires:       parted
Requires:       util-linux
Recommends:     sbsigntools
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnu-efi-devel
BuildRequires:  help2man
BuildRequires:  openssl
BuildRequires:  perl-File-Slurp
BuildRequires:  pkgconfig(openssl)
BuildRequires:  sbsigntools
# /oreon:deps
%description
This package installs a variety of tools for manipulating keys and binary
signatures on UEFI secure boot platforms. The tools provide access to the keys
and certificates stored in the secure variables of the UEFI firmware, usually
in the NVRAM area.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install DOCDIR=%{buildroot}%{_docdir}/%{name}/ CFLAGS="%{optflags}"
rm -v %{buildroot}%{_docdir}/%{name}/COPYING
%global efi_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
