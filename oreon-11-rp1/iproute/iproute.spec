%global source0_hash 4c2fa124c2cf0afd7ca34d1eeacba6ba048a56f6374e2aab93dafbdbd4eea9c0
Summary:        Advanced IP routing and network device configuration tools
Name:               iproute
Version:            7.2.0
Release:        1%{?dist}
URL:                https://kernel.org/pub/linux/utils/net/%{name}2/
Source0:        https://kernel.org/pub/linux/utils/net/%{name}2/%{name}2-%{version}.tar.xz
Source2:            README.etc
License:            GPL-2.0-or-later AND NIST-PD
%if ! 0%{?_module_build}
%endif
Requires:           libbpf
Requires:           psmisc
Provides:           /sbin/ip
%if "%{_sbindir}" == "%{_bindir}"
Requires:           filesystem(unmerged-sbin-symlinks)
Provides:           /usr/sbin/ip
Provides:           /usr/sbin/ss
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  iptables-devel
BuildRequires:  libbpf-devel
BuildRequires:  libcap-devel
BuildRequires:  libmnl-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
kernel.

%package tc
Summary:            Linux Traffic Control utility
License:            GPL-2.0-or-later
Requires:           %{name}%{?_isa} = %{version}-%{release}
Provides:           /sbin/tc
%description tc
The Traffic Control utility manages queueing disciplines, their classes and
attached filters and actions. It is the standard tool to configure QoS in
Linux.

%if ! 0%{?_module_build}
%package doc
Summary:            Documentation for iproute2 utilities with examples
License:            GPL-2.0-or-later
Requires:           %{name} = %{version}-%{release}
%description doc
The iproute documentation contains howtos and examples of settings.
%endif

%package devel
Summary:            iproute development files
License:            GPL-2.0-or-later
Requires:           %{name} = %{version}-%{release}
Provides:           iproute-static = %{version}-%{release}
%description devel
The libnetlink static library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}2-%{version}
%oreon_prep
%build

%configure --color auto
echo -e "\nPREFIX=%{_prefix}\nSBINDIR=%{_sbindir}" >> config.mk
%make_build
%install
%make_install
echo '.so man8/tc-cbq.8' > %{buildroot}%{_mandir}/man8/cbq.8
install -D -m644 include/libnetlink.h %{buildroot}%{_includedir}/libnetlink.h
install -D -m644 lib/libnetlink.a %{buildroot}%{_libdir}/libnetlink.a
rm -rf '%{buildroot}%{_docdir}'
mkdir -p %{buildroot}%{_sysconfdir}/iproute2
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/iproute2/README
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n iproute-tc -f %{oreon_filedir}/iproute-tc.list
%files -n iproute-doc -f %{oreon_filedir}/iproute-doc.list
%files -n iproute-devel -f %{oreon_filedir}/iproute-devel.list

%changelog

%autochangelog
