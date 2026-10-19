%global source0_hash 3f7d792b4464ddc55ab7c3acfe250bc56751923790301798c3b3ce9516dd342d
%undefine __cmake_in_source_build
%bcond_without doh
%bcond_with online
%bcond_with http_parser
Name:		flamethrower
Version:	0.12.0
Release:        1%{?dist}
Summary:        A DNS performance and functional testing utility
License:	Apache-2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:        https://github.com/DNS-OARC/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		flamethrower-0.12.0-unbundle-meson.patch
%if %{with doh}
%endif
%if %{with http_parser}
%endif
ExcludeArch: %{ix86}
Provides: bundled(cpp-base64)
%if %{without http_parser}
Provides: bundled(http-parser) = 2.9.1
Provides: bundled(url-parser) = 2.9.1
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(httplib)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  docopt-cpp-devel
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(ldns)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  uvw-devel
# /oreon:deps
%description
Flamethrower is a small, fast, configurable tool for
functional testing, benchmarking, and stress testing
DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many
of the command line options are compatible.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled source we are able to use from the system
rm -rf 3rd/{json,docopt.cpp,uvw,cpp-httplib}

%build

%meson -Dbundles=false \
%if %{with doh}
  -Ddoh=true \
%endif
%meson_build
%install
%meson_install
install -m 0644 -pD man/flame.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flame.1
%oreon_autofiles main

%check

%ctest
export LD_LIBRARY_PATH="${RPM_BUILD_ROOT}%{_libdir}"
${RPM_BUILD_ROOT}%{_bindir}/flame --help
%if %{with online}
	COMMON="-Q 30 -g randomlabel -l 3 -r test dns.google"
	PROTOS="udp tcp dot"
	%if %{with doh}
		PROTOS+=" doh"
	%endif
	for PROTO in $PROTOS
	do
		${RPM_BUILD_ROOT}%{_bindir}/flame -P $PROTO $COMMON
	done
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
