%define libnfnetlink 1.0.1

Name:           libnetfilter_queue
Version:        1.0.5
Release:        13%{?dist}
Summary:        Netfilter queue userspace library
# Most files say GPLv2+, one says v2 only.
License:        GPL-2.0-only
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 f9ff3c11305d6e03d81405957bdc11aea18e0d315c3e3f48da53a24ba251b9f5
%global source0_file libnetfilter_queue-1.0.5.tar.bz2
# oreon url source checksums end

BuildRequires:  libnfnetlink-devel >= %{libnfnetlink}, pkgconfig, kernel-headers
BuildRequires:  autoconf, automake, libtool, libmnl-devel >= 1.0.3
BuildRequires: make

%description
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue. 

%package        devel
Summary:        Netfilter queue userspace library
Requires:       %{name} = %{version}-%{release}, pkgconfig
Requires:	libnfnetlink-devel >= %{libnfnetlink}, kernel-headers

%description    devel
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnetfilter_queue-1.0.5.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f9ff3c11305d6e03d81405957bdc11aea18e0d315c3e3f48da53a24ba251b9f5" || { echo "oreon: Source0 SHA256 mismatch for libnetfilter_queue-1.0.5.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-13
- Import
