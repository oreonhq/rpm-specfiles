%global source0_hash d19d526e26e4620ae4fdc13f89d3e79b39df5fca643787c8b2e62151152ee4fd

Name:           fabtests
Version:        2.3.1
Release:        %autorelease
Summary:        Test suite for libfabric API
# COPYING says the license is your choice of BSD or GPLv2.
# include/jsmn.h and common/jsmn.c are licensed under MIT.
License:        (BSD-2-Clause OR GPL-2.0-only) AND MIT
Url:            https://github.com/ofiwg/libfabric
Source:        https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  libfabric-devel >= %{version}
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
BuildRequires:  gcc
BuildRequires:  make
Requires:       python3-pytest

%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure \
%ifarch %{valgrind_arches}
  --with-valgrind
%endif

%make_build V=1

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%doc AUTHORS README
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-1
- Prepare for Oreon 11 (RP1)
