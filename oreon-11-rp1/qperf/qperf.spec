# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2300e75edffe95d4dfbe576eb5c2f0d0da3142b5e4a96fcd01b535d50a48f07c
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.9
Release:        33%{?dist}
# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
Source:         http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
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
%oreon_verify_sources
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
