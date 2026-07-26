%global source0_hash 74e0fe75753dba3ac114531b5e73240452c789a3f3adccf5c51217da1d933b21

%define libnfnetlink 1.0.0

Name:           libnetfilter_log
Version:        1.0.1
Release:        31%{?dist}
Summary:        Netfilter logging userspace library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Patch0:		libnetfilter_log-sysheader.patch

BuildRequires:  gcc
BuildRequires:  libnfnetlink-devel >= %{libnfnetlink}, pkgconfig, kernel-headers
BuildRequires: make

%description
libnetfilter_log is a userspace library providing interface to packets that
have been logged by the kernel packet filter. It is is part of a system that
deprecates the old syslog/dmesg based packet logging.

libnetfilter_log has been previously known as libnfnetlink_log.

libnetfilter_log is used by ulogd2. 

%package        devel
Summary:        Netfilter logging userspace library
Requires:       %{name} = %{version}-%{release}, pkgconfig, kernel-headers

%description    devel
libnetfilter_log is a userspace library providing interface to packets that
have been logged by the kernel packet filter. It is is part of a system that
deprecates the old syslog/dmesg based packet logging.

libnetfilter_log has been previously known as libnfnetlink_log.

libnetfilter_log is used by ulogd2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
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
%autochangelog
