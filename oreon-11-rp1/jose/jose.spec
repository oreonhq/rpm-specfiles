%global source0_hash 1d055c445392aa48d709ecd6e56220384ae2b480496e270818bddf1f219c8659
Name:           jose
Version:        15
Release:        1%{?dist}
Summary:        Tools for JSON Object Signing and Encryption (JOSE)
License:        Apache-2.0
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires: lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  jansson-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
%description
José is a command line utility for performing various tasks on JSON
Object Signing and Encryption (JOSE) objects. José provides a full
crypto stack including key generation, signing and encryption.

%package -n lib%{name}
Summary:        Library implementing JSON Object Signing and Encryption
Conflicts:      jansson < 2.10
Provides:       lib%{name}-openssl = %{version}-%{release}
Obsoletes:      lib%{name}-openssl < %{version}-%{release}
Provides:       lib%{name}-zlib = %{version}-%{release}
Obsoletes:      lib%{name}-zlib < %{version}-%{release}
%description -n lib%{name}
This package contains a C library for performing JOSE operations.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       jansson-devel
Provides:       lib%{name}-openssl-devel = %{version}-%{release}
Obsoletes:      lib%{name}-openssl-devel < %{version}-%{release}
Provides:       lib%{name}-zlib-devel = %{version}-%{release}
Obsoletes:      lib%{name}-zlib-devel < %{version}-%{release}
%description -n lib%{name}-devel
This package contains development files for lib%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jose-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
rm -rf %{buildroot}
%meson_install
rm -rf %{buildroot}/%{_libdir}/lib%{name}.la
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%ldconfig_scriptlets -n lib%{name}
%files -f %{oreon_filedir}/main.list
%files -n libjose -f %{oreon_filedir}/libjose.list
%files -n libjose-devel -f %{oreon_filedir}/libjose-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14-1
- Import
