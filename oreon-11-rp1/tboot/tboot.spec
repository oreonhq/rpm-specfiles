# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0fc184ef4c90878d183e719c6a11e77320471e1d4c0fe1a61020132553ad2a72
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:       Performs a verified launch using Intel TXT
Name:          tboot
Version:       1.11.7
Release:       15%{?dist}
Epoch:         1

License:       BSD-3-Clause
URL:           http://sourceforge.net/projects/tboot/
Source0:       https://sourceforge.net/projects/tboot/files/%{name}/%{name}-%{version}.tar.gz
Patch0:        tboot-gcc14.patch
Patch1:        openssl-no-engine.patch
Patch2:        tboot-sbin.patch
Patch3:        tboot-1.11.7-len.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: perl
BuildRequires: openssl-devel
BuildRequires: zlib-devel
Requires:      grub2-efi-x64-modules
ExclusiveArch: %{ix86} x86_64

%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
%oreon_verify_sources
%autosetup -p1 -n %{name}-%{version}

%build
%make_build debug=y

%install
%make_install debug=y

%post
# create the tboot grub entry
grub2-mkconfig -o /boot/grub2/grub.cfg

# For EFI based machines ...
if [ -d /sys/firmware/efi ]; then
	echo "EFI detected .."
	[ -d /boot/grub2/x86_64-efi ] || mkdir -pv /boot/grub2/x86_64-efi
	cp -vf /usr/lib/grub/x86_64-efi/relocator.mod /boot/grub2/x86_64-efi/
	cp -vf /usr/lib/grub/x86_64-efi/multiboot2.mod /boot/grub2/x86_64-efi/
fi

%postun
# Remove residual grub efi modules.
[ -d /boot/grub2/x86_64-efi ] && rm -rf /boot/grub2/x86_64-efi
grub2-mkconfig -o /etc/grub2.cfg


%files
%license COPYING
%doc docs/*
%config %{_sysconfdir}/grub.d/20_linux_tboot
%config %{_sysconfdir}/grub.d/20_linux_xen_tboot
%{_bindir}/lcp2_crtpol
%{_bindir}/lcp2_crtpolelt
%{_bindir}/lcp2_crtpollist
%{_bindir}/lcp2_mlehash
%{_bindir}/tb_polgen
%{_bindir}/txt-acminfo
%{_bindir}/txt-parse_err
%{_bindir}/txt-stat
%{_mandir}/man8/lcp2_crtpol.8.gz
%{_mandir}/man8/lcp2_crtpolelt.8.gz
%{_mandir}/man8/lcp2_crtpollist.8.gz
%{_mandir}/man8/lcp2_mlehash.8.gz
%{_mandir}/man8/tb_polgen.8.gz
%{_mandir}/man8/txt-acminfo.8.gz
%{_mandir}/man8/txt-parse_err.8.gz
%{_mandir}/man8/txt-stat.8.gz
/boot/tboot.gz
/boot/tboot-syms

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.11.7-15
- Import
