%global source0_hash b064c7c3d426efb4786e60a8e6859b82ee2f2c5e49ffeea640cfe4fe33cbc376

Name:           libnfnetlink
Version:        1.0.2
Release:        1%{?dist}
Summary:        Netfilter netlink userspace library
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        https://netfilter.org/projects/libnfnetlink/files/%{name}-%{version}.tar.bz2
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
