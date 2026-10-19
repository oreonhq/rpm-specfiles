%global source0_hash 2300e75edffe95d4dfbe576eb5c2f0d0da3142b5e4a96fcd01b535d50a48f07c
Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.9
Release:        33%{?dist}
License:        GPL-2.0-only OR LicenseRef-Callaway-BSD
Source0:        http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Url:            http://www.openfabrics.org
ExcludeArch:    %{arm}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  make
BuildRequires:  perl-POSIX
BuildRequires:  perl-diagnostics
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Measure socket and RDMA performance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.9-33
- Prepare for Oreon 11 (RP1)
