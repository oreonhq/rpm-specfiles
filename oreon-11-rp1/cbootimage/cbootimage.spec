%global source0_hash 46cce01f07df977668de9e1d49884d8ed539169994215606a9719d17b9db8804
Name:           cbootimage
Version:        1.8
Release:        20%{?dist}
Summary:        Tools to dump and generate boot config table on Tegra devices
License:        GPL-2.0-only
URL:            https://github.com/NVIDIA/cbootimage
Source0:        https://github.com/NVIDIA/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains two programs to parse the boot config table (bct)
of Tegra SoC based devices and to generate a new bct with appended
bootloader (e.g. u-boot) read to be flashed to a storage device.
The boot config table is used in the early boot process to setup the sdhci,
DRAM memory controller and also points to the position of the bootloader.

For more information, see:
http://http.download.nvidia.com/tegra-public-appnotes/bct-overview.html

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -vif
%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
