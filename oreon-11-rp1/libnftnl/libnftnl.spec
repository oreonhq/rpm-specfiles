%global source0_hash c97abc3409f8fa396b4462b2bb7f147a3a47a4ddc97cfa0b2f18890c9cfde8b0
Name:           libnftnl
Version:        1.3.2
Release:        1%{?dist}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl
License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnftnl/
Source0:        https://netfilter.org/projects/%{name}//files/%{name}-%{version}.tar.xz
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmnl-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnftnl-devel -f %{oreon_filedir}/libnftnl-devel.list

%changelog

%autochangelog
