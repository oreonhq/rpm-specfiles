%global source0_hash 9088ee8457b0f511cbfa95eeeeaca4ce9d186ebebe991dfebb2a31b78c3c9805

Name:           monitor-edid
Summary:        Tool for probing and parsing monitor EDID

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            http://gitweb.mageia.org/software/monitor-edid/

Version:        3.4
Release:        13%{?dist}

Source0:        https://gitweb.mageia.org/software/monitor-edid/snapshot/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix Makefile to permit RPM CFLAGS
Patch000:	000-monitor-edid-Makefile.patch

# fix double include
Patch001:	001-Avoid-double-include.patch

Patch002:	002-Use-usr-bin-for-sbin-files-per-F42.patch

Requires:	perl(File::Find)

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  perl-generators

# for tests
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Parse::EDID)

%ifarch %{ix86} x86_64
BuildRequires: libx86-devel
BuildRequires: gcc
%else
# not binary on non x86 arches
%global debug_package %{nil}
%endif

%description
Monitor-edid is a tool for probing and parsing Extended display
identification data (EDID) from monitors.

For more information about EDID, see http://en.wikipedia.org/wiki/EDID

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n refs/tags/v%{version}

%build
# Use default build flags
%set_build_flags

# Remove -Wl,--as-needed  from LDFLAGS as that is not compatible with libx86
LDFLAGS=$(echo ${LDFLAGS} | sed -e 's/-Wl,--as-needed//')
export LDFLAGS

%make_build

%install
%make_install

%check
cd test
# see https://bugs.mageia.org/show_bug.cgi?id=25334
make new_MonitorsDB
make all

%files
%doc README NEWS ChangeLog
%license COPYING
%{_bindir}/monitor-parse-edid
%{_bindir}/monitor-edid
%{_bindir}/monitor-get*

# Mandriva specific scripts (requires lspcidrake)
%exclude %{_bindir}/monitor-probe*

%changelog
%autochangelog
