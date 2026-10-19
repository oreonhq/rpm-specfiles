%global source0_hash 9088ee8457b0f511cbfa95eeeeaca4ce9d186ebebe991dfebb2a31b78c3c9805
Name:           monitor-edid
Summary:        Tool for probing and parsing monitor EDID
License:        GPL-3.0-or-later
Url:            http://gitweb.mageia.org/software/monitor-edid/
Version:        3.4
Release:        1%{?dist}
Source0:        https://gitweb.mageia.org/software/monitor-edid/snapshot/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch000:	000-monitor-edid-Makefile.patch
Patch001:	001-Avoid-double-include.patch
Patch002:	002-Use-usr-bin-for-sbin-files-per-F42.patch
Requires:	perl(File::Find)
%ifarch %{ix86} x86_64
%else
%global debug_package %{nil}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Parse::EDID)
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
Monitor-edid is a tool for probing and parsing Extended display
identification data (EDID) from monitors.

For more information about EDID, see http://en.wikipedia.org/wiki/EDID

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir refs/tags/v%{version}
%oreon_prep
%build

%set_build_flags
LDFLAGS=$(echo ${LDFLAGS} | sed -e 's/-Wl,--as-needed//')
export LDFLAGS
%make_build
%install
%make_install
%oreon_autofiles main

%check

cd test
make new_MonitorsDB
make all
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
