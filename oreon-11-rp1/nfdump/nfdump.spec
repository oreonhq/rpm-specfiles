%global source0_hash d0b46d6e3da8d8316204fb74d20d12d782d8508f01559e34d9c31e33f016d794

Name:		nfdump
Version:	1.7.7
Release:	2%{?dist}
Summary:	NetFlow collecting and processing tools

License:	BSD-3-Clause AND GPL-2.0-or-later
URL:		https://github.com/phaag/nfdump
Source0:	https://github.com/phaag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	bzip2-devel
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	libfl-static
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	rrdtool-devel >= 1.9.0
BuildRequires:	sed
BuildRequires:	libzstd-devel

Requires:	nfdump-libs = %{version}-%{release}

%description
Nfdump is a set of tools to collect and process NetFlow data. It's fast and has
a powerful filter pcap like syntax. It supports NetFlow versions v1, v5, v7, v9
and IPFIX as well as a limited set of sflow. It includes support for CISCO ASA
(NSEL) and CISCO NAT (NEL) devices which export event logging records as v9
flows. Nfdump is fully IPv6 compatible.

%package libs
Summary:	Libraries used by NFDUMP packages

%description libs
Contains libraries used by NFDUMP utilities

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# prepare build script
./bootstrap

%configure \
    --enable-nsel \
    --enable-nfprofile \
    --enable-nftrack \
    --enable-sflow \
    --enable-readpcap \
    --enable-nfpcapd \
    --enable-shared \
    --disable-static

# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
chmod 0644 AUTHORS ChangeLog README.md
rm -rf %{buildroot}/%{_sysconfdir}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%doc src/libnffile/conf/nfdump.conf.dist
%{_bindir}/*
%{_mandir}/man1/*.1*

%files libs
%{_libdir}/libnfdump*.so
%{_libdir}/libnffile*.so

%changelog
%autochangelog
