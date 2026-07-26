%global source0_hash 93e1dca78657c48f9c497a71b9e9d11e88ffadcc20fac27f9c48cdba7f132b51

Name:           waifu2x-converter-cpp
Version:        5.3.4
Release:        20%{?dist}
Summary:        Image Super-Resolution for Anime-style art using OpenCL and OpenCV

# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/DeadSix27/waifu2x-converter-cpp
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

# Add soname versioning
Patch0:         waifu2x-converter-cpp-5.3-set_soversion.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  opencv-devel
Recommends:     beignet
Recommends:     mesa-libOpenCL

Provides:       bundled(picojson)
Provides:       bundled(tclap)

%description
Image Super-Resolution for Anime-style art using OpenCL and OpenCV.

This is a reimplementation of waifu2x (original) converter function,
in C++, using OpenCV.

%package        devel
Summary:        Development files for waifu2x-converter-cpp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for waifu2x-converter-cpp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix ARM build
sed -i 's|-mfloat-abi=hard -mfloat-abi=softfp|-mfloat-abi=hard|' CMakeLists.txt

%build
%cmake3 -DINSTALL_MODELS=true ..
%cmake3_build

%install
%cmake3_install

%files
%license LICENSE include/picojson_LICENSE.txt include/tclap/tclap_LICEENSE.txt
%doc README.md
%{_bindir}/waifu2x-converter-cpp
%{_libdir}/libw2xc.so.1*
%{_datadir}/waifu2x-converter-cpp

%files devel
%{_includedir}/w2xconv.h
%{_libdir}/libw2xc.so

%changelog
%autochangelog
