%global source0_hash 5617bc42ae4572158988efd466954d08f25cbb78f1714164280064784c484f4d
%global __spec_install_post /usr/lib/rpm/brp-compress
%global debug_package %{nil}
%global common_description %{expand:
Memtest86+ is a thorough stand-alone memory test for x86 and x86-64
architecture computers. BIOS based memory tests are only a quick
check and often miss many of the failures that are detected by
Memtest86+.
}
%global mt_isa x64
Name:          memtest86+
Version:       8.10
Release:        1%{?dist}
Summary:        Stand-alone memory tester for x86-64 computers
License:       GPL-2.0-only
URL:           https://www.memtest.org/
Source0:        https://github.com/memtest86plus/memtest86plus/archive/refs/tags/v%{version}.tar.gz#/memtest86-plus-%{version}.tar.gz
Source1:       memtest86+.kernel-install-plugin
Requires(pre): systemd-udev >= 252
ExclusiveArch: x86_64
# oreon:deps
BuildRequires:  dosfstools
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mtools
BuildRequires:  xorriso
# /oreon:deps
%description
%wordwrap -v common_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir memtest86plus-%{version}
%oreon_prep
%build

pushd build/x86_64
make
make iso
popd
%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datarootdir}/%{name}
pushd build/x86_64
install -m 0644 mt86plus %{buildroot}%{_libdir}/%{name}/memtest86+%{mt_isa}.efi
install -m 0644 mt86plus %{buildroot}%{_libdir}/%{name}/memtest86+%{mt_isa}.bin
install -m 0644 memtest.iso %{buildroot}%{_datarootdir}/%{name}/memtest86+%{mt_isa}.iso
install -m 0755 %{SOURCE1} %{buildroot}%{_libdir}/%{name}/memtest86+.kernel-install-plugin
popd
%oreon_autofiles main

%posttrans

MEMTEST_IMAGE="memtest86+%{mt_isa}.bin"
if [ -d /sys/firmware/efi/ ]; then
MEMTEST_IMAGE="memtest86+%{mt_isa}.efi"
fi
KERNEL_INSTALL_PLUGINS=%{_libdir}/%{name}/memtest86+.kernel-install-plugin \
kernel-install add %{version} %{_libdir}/%{name}/${MEMTEST_IMAGE}
exit 0
%preun

if [ $1 -eq 0 ]; then
KERNEL_INSTALL_PLUGINS=%{_libdir}/%{name}/memtest86+.kernel-install-plugin \
kernel-install remove %{version}
fi
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
