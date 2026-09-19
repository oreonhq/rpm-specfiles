%global source0_hash 2a8a0c5360d68bb4fcd11f2e4c47c69976e8d2c85b109dd7d60b1181a4f85d36

Name:           enet
Version:        1.3.18
Release:        5%{?dist}
Summary:        Thin, simple and robust network layer on top of UDP

License:        MIT
URL:            http://sauerbraten.org/enet/
Source0:        %{url}/download/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make

%description
ENet is a relatively thin, simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking library
that handles authentication, lobbying, server discovery, compression,
encryption and other high level, often application level or dependent tasks.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog README
%{_libdir}/lib%{name}.so.*

%files devel
%doc docs/*.dox
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog
