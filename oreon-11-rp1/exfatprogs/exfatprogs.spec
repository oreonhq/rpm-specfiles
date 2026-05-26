%bcond defrag 0

Name:           exfatprogs
Version:        1.3.2
Release:        %autorelease
Summary:        Userspace utilities for exFAT filesystems
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}

Source0:        https://github.com/exfatprogs/exfatprogs/releases/download/1.3.2/exfatprogs-1.3.2.tar.xz
# oreon url source checksums begin
%global source0_sha256 67ddb50543636292df8fde58117eefd54210d6cd7bf1eea5e91d2c4dccbc425e
%global source0_file exfatprogs-1.3.2.tar.xz
# oreon url source checksums end

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
Utilities for formatting and repairing exFAT filesystems.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/exfatprogs-1.3.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "67ddb50543636292df8fde58117eefd54210d6cd7bf1eea5e91d2c4dccbc425e" || { echo "oreon: Source0 SHA256 mismatch for exfatprogs-1.3.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/dump.exfat
%{_sbindir}/exfat2img
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/dump.exfat.*
%{_mandir}/man8/exfat2img.*
%{_mandir}/man8/exfatlabel.*
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*

%if %{with defrag}
%{_sbindir}/defrag.exfat
%{_mandir}/man8/defrag.exfat.*
%else
%exclude %{_sbindir}/defrag.exfat
%exclude %{_mandir}/man8/defrag.exfat.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)
