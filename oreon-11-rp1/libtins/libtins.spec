%global source0_hash 6ff5fe1ada10daef8538743dccb9c9b3e19d05d028ffdc24838e62ff3fc55841

Name:           libtins
Version:        4.5
Release:        9%{?dist}
Summary:        A high-level, multiplatform C++ network packet sniffing and crafting library

License:        BSD
URL:            https://github.com/mfontanini/libtins
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  boost-devel
BuildRequires:  doxygen

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
# TODO: Please submit an issue to upstream (rhbz#2380755)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DLIBTINS_BUILD_TESTS=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%cmake_build --target docs

%install
%cmake_install

%files
%license LICENSE
%doc CHANGES.md CONTRIBUTING.md README.md THANKS
%{_libdir}/%{name}.so.4.5

%files devel
%{_includedir}/tins
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%files doc
%doc %{__cmake_builddir}/docs

%changelog
%autochangelog
