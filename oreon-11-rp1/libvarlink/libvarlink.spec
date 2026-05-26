%global _hardened_build 1

Name:           libvarlink
Version:        24.0.1
Release:        %autorelease
Summary:        Varlink C Library
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/varlink/%{name}
Source:        https://github.com/varlink/libvarlink/archive/v24.0.1/libvarlink-24.0.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 ca3ecd13005309e0322bc64a26f2960e613f2a9a9cedee845865c2d042f73b3c
%global source0_file libvarlink-24.0.1.tar.gz
# oreon url source checksums end

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glibc-langpack-de

%description
Varlink C Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        util
Summary:        Varlink command line tools

%description    util
The %{name}-util package contains varlink command line tools.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libvarlink-24.0.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ca3ecd13005309e0322bc64a26f2960e613f2a9a9cedee845865c2d042f73b3c" || { echo "oreon: Source0 SHA256 mismatch for libvarlink-24.0.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
# https://github.com/varlink/libvarlink/issues/63
%ifarch ppc64le
test_list=$(%meson_test --list) 2> /dev/null
%if 0%{?fedora} || 0%{?rhel} > 10
test_list=${test_list//libvarlink:test-symbols}
%else
test_list=${test_list//test-symbols}
%endif
%meson_test $test_list
%else
%meson_test
%endif

%install
%meson_install

%files
%license LICENSE
%{_libdir}/libvarlink.so.*

%files util
%{_bindir}/varlink
%{_datadir}/bash-completion/completions/varlink
%{_datadir}/vim/vimfiles/after/*

%files devel
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24.0.1-1
- Prepare for Oreon 11 (RP1)
