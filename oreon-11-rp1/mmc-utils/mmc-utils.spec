%global source0_hash 39e6a89e06b53f99816f110af6743d1adc82220b26c51b0c3fd0a11ccf4206c2

%global commit d8a8358a7207bd81d0c38dca2cf27a48bf411341
%global date 20250624
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Configure MMC storage devices from userspace
Name: mmc-utils
Version: 1.0
Release: 3%{?dist}
URL: https://docs.kernel.org/driver-api/mmc/mmc-tools.html
Source0: https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/snapshot/mmc-utils-%{version}.tar.gz
Patch0: https://sources.debian.org/data/main/m/mmc-utils/0%2Bgit20220624.d7b343fd-1/debian/patches/0001-Fix-typo.patch
Patch1: https://sources.debian.org/data/main/m/mmc-utils/0%2Bgit20220624.d7b343fd-1/debian/patches/0002-man-mmc.1-Fix-warning-macro-not-defined.patch
# remove -Werror from CFLAGS
Patch2: %{name}-no-Werror.patch
# fix warning: _FORTIFY_SOURCE requires compiling with optimization (-O)
Patch3: %{name}-cflags-fortify-source.patch
License: GPL-2.0-only AND BSD-3-Clause
BuildRequires: gcc
BuildRequires: make
# BSD-licensed HMAC-SHA-224/256/384/512 implementation from http://www.ouah.org/ogay/hmac/
# 3rdparty/hmac_sha
Provides: bundled(hmac)

%description
The mmc-utils tools can do the following:

* Print and parse extcsd data.
* Determine the eMMC writeprotect status.
* Set the eMMC writeprotect status.
* Set the eMMC data sector size to 4KB by disabling emulation.
* Create general purpose partition.
* Enable the enhanced user area.
* Enable write reliability per partition.
* Print the response to STATUS_SEND (CMD13).
* Enable the boot partition.
* Set Boot Bus Conditions.
* Enable the eMMC BKOPS feature.
* Permanently enable the eMMC H/W Reset feature.
* Permanently disable the eMMC H/W Reset feature.
* Send Sanitize command.
* Program authentication key for the device.
* Counter value for the rpmb device will be read to stdout.
* Read from rpmb device to output.
* Write to rpmb device from data file.
* Enable the eMMC cache feature.
* Disable the eMMC cache feature.
* Print and parse CID data.
* Print and parse CSD data.
* Print and parse SCR data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build C=0 GIT_VERSION=%{version}

%install
%make_install bindir=%{_bindir}
install -D -pm0644 -t %{buildroot}%{_mandir}/man1 man/mmc.1

%files
%doc README
%{_bindir}/mmc
%{_mandir}/man1/mmc.1*

%changelog
%autochangelog
