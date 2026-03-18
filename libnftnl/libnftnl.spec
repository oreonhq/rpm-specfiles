Name:           libnftnl
Version:        1.3.1
Release:        2%{?dist}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl

License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnftnl/
Source0:        %{url}/files/%{name}-%{version}.tar.xz
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt

BuildRequires:  libmnl-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2

%description
A library for low-level interaction with nftables Netlink's API over libmnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules
%make_build

%check
%make_build check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-2
- Prepare for Oreon 11 (RP1)
