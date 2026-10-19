%global source0_hash f9ff3c11305d6e03d81405957bdc11aea18e0d315c3e3f48da53a24ba251b9f5
%define libnfnetlink 1.0.1
Name:           libnetfilter_queue
Version:        1.0.5
Release:        1%{?dist}
Summary:        Netfilter queue userspace library
License:        GPL-2.0-only
URL:            http://netfilter.org
Source0:        https://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel
BuildRequires:  libnfnetlink-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnetfilter_queue-devel -f %{oreon_filedir}/libnetfilter_queue-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-13
- Import
