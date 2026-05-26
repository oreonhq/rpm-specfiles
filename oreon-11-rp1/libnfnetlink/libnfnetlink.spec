Name:           libnfnetlink
Version:        1.0.1
Release:        32%{?dist}
Summary:        Netfilter netlink userspace library
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/libnfnetlink/files/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 f270e19de9127642d2a11589ef2ec97ef90a649a74f56cf9a96306b04817b51a
%global source0_file libnfnetlink-1.0.1.tar.bz2
# oreon url source checksums end
BuildRequires:	kernel-headers
BuildRequires:  automake autoconf libtool pkgconfig
BuildRequires: make

%description
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions.  It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package        devel
Summary:        Netfilter netlink userspace library
Requires:       %{name} = %{version}-%{release}
Requires:	kernel-headers

%description    devel
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions.  It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnfnetlink-1.0.1.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f270e19de9127642d2a11589ef2ec97ef90a649a74f56cf9a96306b04817b51a" || { echo "oreon: Source0 SHA256 mismatch for libnfnetlink-1.0.1.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_libdir}/*.so.*


%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnfnetlink
%{_includedir}/libnfnetlink/*.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-32
- Prepare for Oreon 11 (RP1)
