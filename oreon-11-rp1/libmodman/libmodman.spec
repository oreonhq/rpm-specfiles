%global source0_hash 4c2749154795d5cc49871ba162e1c2213f3b24598b1d8b6c10843de18ed8774d

Name:           libmodman
Version:        2.0.1
Release:        36%{?dist}
Summary:        A simple library for managing C++ modules (plug-ins)

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://code.google.com/p/libmodman/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/libmodman/libmodman-2.0.1.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel

%description
libmodman is a simple library for managing C++ modules (plug-ins).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libmodman-2.0.1

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%check
%ctest

%install
%cmake_install

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libmodman.so.*

%files devel
%{_includedir}/libmodman/
%{_libdir}/libmodman.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/Findlibmodman.cmake

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-36
- Import
