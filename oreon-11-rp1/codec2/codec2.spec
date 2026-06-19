%global source0_hash cbccae52b2c2ecc5d2757e407da567eb681241ff8dadce39d779a7219dbcf449

%undefine __cmake_in_source_build
%bcond_without bootstrap

Name:           codec2
Version:        1.2.0
Release:        %autorelease
Summary:        Next-Generation Digital Voice for Two-Way Radio

License:        LGPL-2.1-only
URL:            http://rowetel.com/codec2.html
Source0:        https://github.com/drowe67/codec2/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsamplerate-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel

%description
Codec 2 is an open source speech codec for 2400 bit/s and below.

%package devel
Summary:        Development files for Codec 2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Codec 2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{without bootstrap}
       -DLPCNET=ON
%endif
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/codec2.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${prefix}/include/%{name}
libdir=\${exec_prefix}/%{_lib}

Name: codec2
Description: Next-Generation Digital Voice for Two-Way Radio
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -l%{name}
EOF

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
