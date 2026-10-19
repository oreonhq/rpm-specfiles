%global source0_hash ca5c87d41339f8bc4daabb53e8a9356b3c995f2d2419b85d7bff823b2ecc252d
Summary:        C library for reading MaxMind DB files
Name:           libmaxminddb
Version:        1.14.1
Release:        1%{?dist}
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://maxmind.github.io/libmaxminddb/
Source0:        https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        maxminddb_config.h
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a custom
binary format designed to facilitate fast lookups of IP addresses
while allowing for great flexibility in the type of data associated
with an address.

The MaxMind DB format is an open file format. The specification is
available at https://maxmind.github.io/MaxMind-DB/ and licensed under
the Creative Commons Attribution-ShareAlike 3.0 Unported License.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
autoreconf --force --install

%build

%configure --disable-static
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
mv -f $RPM_BUILD_ROOT%{_includedir}/maxminddb_config{,-%{__isa_bits}}.h
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/maxminddb_config.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_PRELOAD=$RPM_BUILD_ROOT%{_libdir}/%{name}.so make check
%files -f %{oreon_filedir}/main.list
%files -n libmaxminddb-devel -f %{oreon_filedir}/libmaxminddb-devel.list

%changelog

%autochangelog
