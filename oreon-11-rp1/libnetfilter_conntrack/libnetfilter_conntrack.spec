Name:           libnetfilter_conntrack
Version:        1.1.1
Release:        %autorelease
Summary:        Netfilter conntrack userspace library
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz
Source1:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
# oreon url source checksums begin
%global source0_sha256 769d3eaf57fa4fbdb05dd12873b6cb9a5be7844d8937e222b647381d44284820
%global source0_file libnetfilter_conntrack-1.1.1.tar.xz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel >= 1.0.3
BuildRequires:  libnfnetlink-devel >= 1.0.1
BuildRequires:  make autoconf automake libtool
BuildRequires:  pkgconfig

%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name} = %{version}-%{release}, libnfnetlink-devel >= 1.0.1
Requires:       kernel-headers

%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnetfilter_conntrack-1.1.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "769d3eaf57fa4fbdb05dd12873b6cb9a5be7844d8937e222b647381d44284820" || { echo "oreon: Source0 SHA256 mismatch for libnetfilter_conntrack-1.1.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -vi
%configure --disable-static --disable-rpath

%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_conntrack
%{_includedir}/libnetfilter_conntrack/*.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-1
- Prepare for Oreon 11 (RP1)
