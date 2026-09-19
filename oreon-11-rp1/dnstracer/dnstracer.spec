%global source0_hash 64cda0ed15ef598a38ec72a96a356e3d10b7f822fc75928115eae96a65ae2b21

Name:           dnstracer
Version:        1.10
Release:        11%{?dist}
Summary:        Trace DNS queries to the source

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.mavetju.org/unix/dnstracer.php
Source0:        http://www.mavetju.org/download/dnstracer-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators

Patch:          with_debug.patch

%description
dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%make_build

%install
# working with a very basic and minimal make file
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
%make_install PREFIX=%{buildroot}%{_prefix} MANPREFIX=%{buildroot}%{_mandir}/man8/

%files
%license LICENSE
%doc README CONTACT CHANGES
%{_bindir}/dnstracer
%{_mandir}/man8/dnstracer.8*

%changelog
%autochangelog
