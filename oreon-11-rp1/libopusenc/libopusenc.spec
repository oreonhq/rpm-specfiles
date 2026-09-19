%global source0_hash f616d3aff9b2034547894ccb8ab56c36cf1a4acb0d922c5d7119f97bbe58642c

Name:     libopusenc
Version:  0.3
Release:  %autorelease
Summary:  A library that provides an easy way to encode Ogg Opus files
# Automatically converted from old format: BSD - review is highly recommended.
License:  LicenseRef-Callaway-BSD
URL:      https://opus-codec.org/

Source0:  https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: opus-devel
BuildRequires: make

%description
A library that provides an easy way to encode Ogg Opus files.

%package  devel
Summary:  Development package for libopusenc
Requires: opus-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with libopusenc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static

%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/

%check
make check %{?_smp_mflags} V=1

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libopusenc.so.*

%files devel
%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/libopusenc.so
%{_libdir}/pkgconfig/libopusenc.pc

%changelog
%autochangelog
