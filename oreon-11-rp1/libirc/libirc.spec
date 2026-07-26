%global source0_hash 584925f0eafd57293fa7af62cc3820e47e3889a60d00543b0969716b808d0a8b

Name:     libirc
Version:  0.2.2
Release:  %{autorelease}
Summary:  IRC client library for C
License:  GPL-3.0-only
URL:      https://github.com/n0la/libirc
Source0:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconf
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: libcmocka-devel
BuildRequires: gnutls-devel

ExcludeArch:   i686

%description
%{summary}.

%package devel
Summary:   Development headers for the libirc library
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers for the libric library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%doc README.md
%{_libdir}/libirc.so.0
%{_libdir}/libirc.so.%{version}

%files devel
%{_includedir}/irc
%{_datadir}/pkgconfig/libirc.pc
%{_libdir}/libirc.so

%changelog
%autochangelog
