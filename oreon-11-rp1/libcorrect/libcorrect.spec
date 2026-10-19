%global source0_hash ef78170fd0e87ce4e645a895dd02833b13cc2aeb62114b20fc7f1d1ea3ef3445
%global gitcommit_full f5a28c74fba7a99736fe49d3a5243eca29517ae9
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20181010
Name:           libcorrect
Version:        0
Release:        1%{?dist}
Summary:        C library for Convolutional codes and Reed-Solomon
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/quiet/libcorrect
Source0:        https://github.com/quiet/%{name}/tarball/%{gitcommit_full}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

%package devel
Summary:        Development files for libcorrect
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

This subpackage contains libraries and header files for developing
applications that want to make use of libcorrect.

%prep

%autosetup -p1 -n quiet-%{name}-%{gitcommit}
echo "set_property(TARGET correct PROPERTY SOVERSION 0.0.0)" >> CMakeLists.txt
sed -e "s|DESTINATION lib|DESTINATION %{_lib}|" \
    -e '/CMAKE_C_FLAGS/d' \
    -e 's|}" HAVE_SSE)|}" HAVE_SSE_dd)|' \
    -e "/(fec_shim_static/d" \
    -e "s| fec_shim_static||" \
    -e "/(correct_static/d" \
    -e "s| correct_static||" -i CMakeLists.txt

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcorrect-devel -f %{oreon_filedir}/libcorrect-devel.list

%changelog

%autochangelog
