%global source0_hash 6d9ad31c86408711f0a60f05b1933101c7497683c2e0d8917d1611a3feba3dd5

Name:             libnfc
Version:          1.8.0
Release:          13%{?dist}
Summary:          NFC SDK and Programmers API

License:          LGPL-3.0-or-later
URL:              http://www.libnfc.org/
Source0:          https://github.com/nfc-tools/libnfc/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:          README.fedora

BuildRequires:    gcc
BuildRequires:    pcsc-lite-devel
BuildRequires:    libusb-compat-0.1-devel
BuildRequires:    doxygen
BuildRequires:    make
Requires:         systemd
Requires(post):   systemd
Requires(postun): systemd

%description
libnfc is the first free NFC SDK and Programmers API released under the
GNU Lesser General Public License. It provides complete transparency and
royalty-free use for everyone.

%package devel
Summary: Development libraries for libnfc
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libnfc-devel package contains header files necessary for
developing programs using libnfc.

%package examples
Summary: Examples using libnfc
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
The libnfc-examples package contains examples demonstrating the functionality
of libnfc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp %{SOURCE1} .

%build
%configure --disable-static --with-drivers=all

# remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
doxygen

%install
make install DESTDIR=%{buildroot}
# remove *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# migrate udev rule to dynamic ACL management, classify the device as smartcard reader
sed -i 's/GROUP="plugdev"/ENV{ID_SMARTCARD_READER}="1"/' contrib/udev/93-pn53x.rules

# install udev rule
install -Dp -m 0644 contrib/udev/93-pn53x.rules %{buildroot}%{_prefix}/lib/udev/rules.d/93-pn53x.rules

# install module blacklist file as an example
install -Dp -m 0644 contrib/linux/blacklist-libnfc.conf %{buildroot}%{_datadir}/%{name}/blacklist-libnfc.conf

# install sample config file
mkdir -p %{buildroot}%{_sysconfdir}/nfc/devices.d
install -p -m 0644 libnfc.conf.sample %{buildroot}%{_sysconfdir}/nfc/libnfc.conf

%post
/sbin/ldconfig
[ "$1" = 1 ] && udevadm control --reload
exit 0

%postun
/sbin/ldconfig
[ "$1" = 0 ] && udevadm control --reload
exit 0

%files
%doc COPYING README.md README.fedora AUTHORS ChangeLog
%dir %{_sysconfdir}/nfc
%dir %{_sysconfdir}/nfc/devices.d
%{_prefix}/lib/udev/rules.d/93-pn53x.rules
%config(noreplace) %{_sysconfdir}/nfc/libnfc.conf
%{_datadir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/nfc/
%{_libdir}/pkgconfig/*.pc
%doc doc/html

%files examples
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
