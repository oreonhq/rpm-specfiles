%global source0_hash 102e22431e4ec6f1f0baacb6b1b036476f5e5a83400f2174807a090a14f4dc67

Name:           libopkele
Version:        2.0.4
Release:        43%{?dist}
Summary:        C++ implementation of the OpenID decentralized identity system
License:        MIT
URL:            http://kin.klever.net/libopkele/
Source0:        http://kin.klever.net/dist/%{name}-%{version}.tar.bz2
# Patch from debian bug http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667253
Patch0:         fix-ftbfs-gcc4.7.diff
# Patch from upstream already applied to git.
Patch1:         libopkele-2.0.4-remove-iterator.patch
Patch2:		0001-Fix-DH-parameter-access-for-OpenSSL-1.1.0.patch

BuildRequires:  boost-devel, openssl-devel, libxslt, libcurl-devel, expat-devel
BuildRequires:  tidy-devel, sqlite-devel, libuuid-devel, gcc-c++
BuildRequires: make

%description
libopkele is a C++ implementation of the OpenID decentralized identity
system. It provides OpenID protocol handling, leaving authentication
and user interaction to the implementor.

%package devel
Summary:        Header files and libraries for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} OpenID library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.{a,la}

%check
./test/test

%files
%doc AUTHORS COPYING NEWS
%{_libdir}/libopkele.so.*

%files devel
%{_includedir}/opkele
%{_libdir}/libopkele.so
%{_libdir}/pkgconfig/libopkele.pc

%changelog
%autochangelog
