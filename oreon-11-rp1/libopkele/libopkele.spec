%global source0_hash 102e22431e4ec6f1f0baacb6b1b036476f5e5a83400f2174807a090a14f4dc67
Name:           libopkele
Version:        2.0.4
Release:        1%{?dist}
Summary:        C++ implementation of the OpenID decentralized identity system
License:        MIT
URL:            http://kin.klever.net/libopkele/
Source0:        http://kin.klever.net/dist/%{name}-%{version}.tar.bz2
Patch0:         fix-ftbfs-gcc4.7.diff
Patch1:         libopkele-2.0.4-remove-iterator.patch
Patch2:		0001-Fix-DH-parameter-access-for-OpenSSL-1.1.0.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  tidy-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

./test/test
%files -f %{oreon_filedir}/main.list
%files -n libopkele-devel -f %{oreon_filedir}/libopkele-devel.list

%changelog

%autochangelog
