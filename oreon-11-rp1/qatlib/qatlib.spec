%global source0_hash 7c68bf05f196153b1b1669a7d17e5bfba6253e7cafb69f67d30a0d17e7facecb
%global libqat_soversion  4
%global libusdm_soversion 0
Name:             qatlib
Version:          26.02.0
Release:        1%{?dist}
Summary:        Intel QuickAssist user space library
License:          BSD-3-Clause
URL:              https://github.com/intel/%{name}
Source0:        https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz#/qatlib-26.02.0.tar.gz
Recommends:       qatlib-service
ExcludeArch:      %{arm} aarch64 %{power64} s390x i686 riscv64
Patch0:        force-32-bit-MMIO-CSR-reads.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  numactl-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Intel QuickAssist Technology (Intel QAT) provides hardware acceleration
for offloading security, authentication and compression services from the
CPU, thus significantly increasing the performance and efficiency of
standard platform solutions.

Its services include symmetric encryption and authentication,
asymmetric encryption, digital signatures, RSA, DH and ECC, and
lossless data compression.

This package provides user space libraries that allow access to
Intel QuickAssist devices and expose the Intel QuickAssist APIs.

%package       devel
Summary:       Headers and libraries to build applications that use qatlib
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   devel
This package contains headers and libraries required to build applications
that use the Intel QuickAssist APIs.

%package       tests
Summary:       Sample applications that use qatlib
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   tests
This package contains sample applications that use the Intel QuickAssists APIs.

%package       service
Summary:       A daemon for qatlib resources management
Requires:      pciutils
Requires:      %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}
%description   service
This package contains a daemon that manages QAT resources for the Intel
QuickAssist Technology user space library (qatlib).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --enable-legacy-algorithms
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
make DESTDIR=%{buildroot} samples-install
rm %{buildroot}/%{_libdir}/libqat.la
rm %{buildroot}/%{_libdir}/libusdm.la
rm %{buildroot}/%{_libdir}/libqat.a
rm %{buildroot}/%{_libdir}/libusdm.a
install -m0644 -D qatlib.sysusers.conf %{buildroot}%{_sysusersdir}/qatlib.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post          service

%systemd_post qat.service
if [ -S /run/udev/control ] ; then
    udevadm control --reload || :
    udevadm trigger || :
fi
%preun         service

%systemd_preun qat.service
%postun        service

%systemd_postun_with_restart qat.service
if [ -S /run/udev/control ] ; then
    udevadm control --reload || :
    udevadm trigger || :
fi
%files -f %{oreon_filedir}/main.list
%files -n qatlib-devel -f %{oreon_filedir}/qatlib-devel.list
%files -n qatlib-tests -f %{oreon_filedir}/qatlib-tests.list
%files -n qatlib-service -f %{oreon_filedir}/qatlib-service.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.02.0-2
- Import
