%global source0_hash 52665aae3c7352a1fa68d017a87c825559c514072409e30753f36aa6eb0c7b4d

%global commit0 c278588e34e535f0bb8f00df3880d26928038cad
%global date0 20210526
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        ONNXIFI with Facebook Extension
Name:           foxi
License:        MIT
# 1.4.1 comes from VERSION_NUMBER file
Version:        1.4.1^git%{date0}.%{shortcommit0}
Release:        8%{?dist}

# Only for pytorch's arch
ExclusiveArch:  x86_64 aarch64
# and pytorch's toolchain
%global toolchain clang

URL:            https://github.com/houseroad/foxi
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/houseroad/foxi/pull/25
Patch0:         0001-Fix-signatures-of-functions.patch

BuildRequires: cmake
BuildRequires: clang

%description
%{summary}

%package devel

Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

# Change static library to shared
sed -i -e 's/foxi_loader STATIC/foxi_loader SHARED/' CMakeLists.txt
# Disable hidden so shared foxi_loader will find onnxifi_load
sed -i -e 's/__ELF_/__NO_ELF_DISABLING_HIDDEN__/' foxi/onnxifi_loader.h
# Fix the destination lib
sed -i -e 's/DESTINATION lib/DESTINATION lib64/' CMakeLists.txt
# Just install libfoxi_loader
sed -i -e 's/foxi foxi_dummy foxi_loader/foxi_loader/' CMakeLists.txt
# version *.so
echo "set_target_properties(foxi_loader PROPERTIES SOVERSION \"1.4.1\")" >> CMakeLists.txt

# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 3.1@cmake_minimum_required(VERSION 3.5@' CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DONNX_USE_LITE_PROTO=OFF

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%exclude %{_libdir}/libfoxi.so
%{_libdir}/libfoxi_loader.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libfoxi_loader.so

%changelog
%autochangelog
