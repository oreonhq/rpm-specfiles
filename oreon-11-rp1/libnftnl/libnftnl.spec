%global source0_hash 607da28dba66fbdeccf8ef1395dded9077e8d19f2995f9a4d45a9c2f0bcffba8

Name:           libnftnl
Version:        1.3.1
Release:        2%{?dist}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl

License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnftnl/
Source0:        https://netfilter.org/projects/libnftnl//files/libnftnl-1.3.1.tar.xz
Source1:        https://netfilter.org/projects/libnftnl//files/libnftnl-1.3.1.tar.xz.sig
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
