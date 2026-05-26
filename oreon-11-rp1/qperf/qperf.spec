Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.9
Release:        33%{?dist}
# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
Source:         http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2300e75edffe95d4dfbe576eb5c2f0d0da3142b5e4a96fcd01b535d50a48f07c
%global source0_file qperf-0.4.9.tar.gz
# oreon url source checksums end
Url:            http://www.openfabrics.org
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libibverbs-devel >= 1.2.0
BuildRequires:  librdmacm-devel >= 1.0.21
BuildRequires:  perl-interpreter
BuildRequires:  perl-diagnostics
BuildRequires:  perl-POSIX
# RDMA is not currently built on 32-bit ARM: #1484155
ExcludeArch:    %{arm}

%description
Measure socket and RDMA performance.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/qperf-0.4.9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2300e75edffe95d4dfbe576eb5c2f0d0da3142b5e4a96fcd01b535d50a48f07c" || { echo "oreon: Source0 SHA256 mismatch for qperf-0.4.9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%make_build

%install
%make_install

%files
%license COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.9-33
- Prepare for Oreon 11 (RP1)
