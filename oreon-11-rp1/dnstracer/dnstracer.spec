%global source0_hash 64cda0ed15ef598a38ec72a96a356e3d10b7f822fc75928115eae96a65ae2b21
Name:           dnstracer
Version:        1.10
Release:        1%{?dist}
Summary:        Trace DNS queries to the source
License:        LicenseRef-Callaway-BSD
URL:            http://www.mavetju.org/unix/dnstracer.php
Source0:        http://www.mavetju.org/download/dnstracer-%{version}.tar.bz2
Patch:          with_debug.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators
# /oreon:deps
%description
dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%make_build
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
%make_install PREFIX=%{buildroot}%{_prefix} MANPREFIX=%{buildroot}%{_mandir}/man8/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
