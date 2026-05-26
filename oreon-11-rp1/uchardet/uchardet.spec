%undefine __cmake_in_source_build

Name:          uchardet
Version:       0.0.8
Release:       10%{?dist}
Summary:       An encoding detector library ported from Mozilla

License:       MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:           https://www.freedesktop.org/wiki/Software/%{name}
Source0:       https://www.freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 e97a60cfc00a1c147a674b097bb1422abd9fa78a2d9ce3f3fdcc2e78a34ac5f0
%global source0_file uchardet-0.0.8.tar.xz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. Uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains headers and shared libraries
for developing tools for uchardet.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/uchardet-0.0.8.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e97a60cfc00a1c147a674b097bb1422abd9fa78a2d9ce3f3fdcc2e78a34ac5f0" || { echo "oreon: Source0 SHA256 mismatch for uchardet-0.0.8.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
# TODO: Please submit an issue to upstream (rhbz#2381619)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DBUILD_STATIC=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%check
pushd %{_vpath_builddir}
  ctest -VV \
  %ifarch %{ix86}
    || :
  %else
    ;
  %endif
popd

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.8-10
- Prepare for Oreon 11 (RP1)
