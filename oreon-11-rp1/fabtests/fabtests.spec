%global source0_hash d19d526e26e4620ae4fdc13f89d3e79b39df5fca643787c8b2e62151152ee4fd
Name:           fabtests
Version:        2.3.1
Release:        1%{?dist}
Summary:        Test suite for libfabric API
License:        (BSD-2-Clause OR GPL-2.0-only) AND MIT
Url:            https://github.com/ofiwg/libfabric
Source0:        https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
%ifarch %{valgrind_arches}
%endif
Requires:       python3-pytest
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libfabric-devel
BuildRequires:  make
# /oreon:deps
%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
%ifarch %{valgrind_arches}
  --with-valgrind
%endif
%make_build V=1
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-1
- Prepare for Oreon 11 (RP1)
