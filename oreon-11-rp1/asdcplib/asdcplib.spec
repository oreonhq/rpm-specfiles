%global source0_hash ee40998f737d5751cf9157c4c416f2ef4f63fc5bdae579afefbb91a3265e6039
%global gittag rel_2_13_2
Name:           asdcplib
Version:        2.13.2
Release:        1%{?dist}
Summary:        AS-DCP file access libraries
License:        BSD-3-Clause
URL:            http://www.cinecert.com/asdcplib/
Source0:        https://github.com/cinecert/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        %{name}.pc
ExcludeArch:    %{ix86} %{arm}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  xerces-c-devel
# /oreon:deps
%description
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

%package        tools
Summary:        AS-DCP file access libraries tools
%description    tools
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

This package contains tools and testing programs for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{gittag}
sed -i -e 's/DESTINATION lib/DESTINATION %{_lib}/g' src/CMakeLists.txt

# rpmlint fixes
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.cpp" -exec chmod 644 {} \;
chmod 644 README.md

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_SKIP_RPATH=True
%cmake_build
%install
%cmake_install
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
sed -i \
    -e 's|PREFIX|%{_prefix}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDEDIR|%{_includedir}|g' \
    -e 's|VERSION|%{version}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
find %{buildroot} -name '*.la' -delete
rm -fr  %{buildroot}%{_prefix}/targets
%oreon_autofiles asdcplib-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles asdcplib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n asdcplib-tools -f %{oreon_filedir}/asdcplib-tools.list
%files -n asdcplib-devel -f %{oreon_filedir}/asdcplib-devel.list

%changelog

%autochangelog
