%global source0_hash 14073d5487233897355d3ff04ddc1c8d03cc5ba8d2356236aa88161a9f2dc912
Name:           libnetfilter_cthelper
Version:        1.0.1
Release:        1%{?dist}
Summary:        User-space infrastructure for connection tracking helpers
License:        GPL-2.0-only
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
This library provides the infrastructure for the user-space helper
infrastructure available since the Linux kernel 3.6.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.1
Requires:       kernel-headers
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnetfilter_cthelper-devel -f %{oreon_filedir}/libnetfilter_cthelper-devel.list

%changelog

%autochangelog
