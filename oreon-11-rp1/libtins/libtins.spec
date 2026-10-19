%global source0_hash 37a9cc407929c56c2081e717347cac455287ba354016bad5bad6243d1f0a4a7a
Name:           libtins
Version:        4.6
Release:        1%{?dist}
Summary:        A high-level, multiplatform C++ network packet sniffing and crafting library
License:        BSD
URL:            https://github.com/mfontanini/libtins
Source0:        https://github.com/mfontanini/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libssl)
# /oreon:deps
%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Document files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
The %{name}-docs package contains document files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix GCC 13 build
# https://github.com/mfontanini/libtins/pull/496
sed -i 's|stdint.h|cstdint|' include/tins/ip_address.h

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DLIBTINS_BUILD_TESTS=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%cmake_build --target docs
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libtins-devel -f %{oreon_filedir}/libtins-devel.list
%files -n libtins-doc -f %{oreon_filedir}/libtins-doc.list

%changelog

%autochangelog
