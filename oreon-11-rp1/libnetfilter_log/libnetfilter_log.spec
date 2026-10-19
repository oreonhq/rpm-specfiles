%global source0_hash e3f408575614d849e4726b45e90c7ebb0e6744b04859555a9ce6ec40744ffeea
%define libnfnetlink 1.0.0
Name:           libnetfilter_log
Version:        1.0.2
Release:        1%{?dist}
Summary:        Netfilter logging userspace library
License:        GPL-2.0-only
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Patch0:		libnetfilter_log-sysheader.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libnfnetlink-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnetfilter_log-devel -f %{oreon_filedir}/libnetfilter_log-devel.list

%changelog

%autochangelog
