%global source0_hash 6e5c10b079836fd38f313811575b9cb077f590de116c2aa3b02a80d56ddce292

%global prerelease beta

Name:           dvblinkremote
Version:        0.2.0
Release:        0.39.%{prerelease}%{?dist}
Summary:        Tool for interacting with a DVBLink Connect! Server

License:        MIT
URL:            https://github.com/marefr/dvblinkremote
Source0:        https://github.com/marefr/%{name}/archive/v%{version}-%{prerelease}/%{name}-%{version}-%{prerelease}.tar.gz
# Fix curl detection
Patch0:         %{name}-0.2.0-curl.patch
# Fix build with tinyxml2 >= 6.0.0
Patch1:         %{name}-0.2.0-tinyxml2.patch
# Fix compilation issues on Linux with recent gcc versions (see
# https://github.com/marefr/dvblinkremote/commit/b32af4a)
Patch2:         %{name}-0.2.0-build.patch
# Build a shared library instead of a static one
Patch3:         %{name}-0.2.0-shared_library.patch
# Fix installation
Patch4:         %{name}-0.2.0-install.patch
# Fix ordered pointer comparison against zero
Patch5:		%{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libcurl-devel
BuildRequires:  tinyxml2-devel

%description
A command line tool for interacting with a DVBLink Connect! Server using the
DVBLink Remote API.

%package        libs
Summary:        Pure C++ DVBLink Remote API library
%description    libs
libdvblinkremote is a pure C++ DVBLink Remote API static library. It currently
supports DVBLink Remote API version 0.2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use libdvblinkremote.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-%{prerelease} -p1

%build
%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DDVBLINKREMOTE_BIN_DIR=%{_bindir} \
  -DDVBLINKREMOTE_INCLUDE_DIR=%{_includedir}/lib%{name} \
  -DDVBLINKREMOTE_LIB_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}

%files libs
%doc COPYING README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/lib%{name}/
%{_libdir}/*.so

%changelog
%autochangelog
