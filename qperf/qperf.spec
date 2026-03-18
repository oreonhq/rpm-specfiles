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
