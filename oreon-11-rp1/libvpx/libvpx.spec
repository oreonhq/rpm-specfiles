%global source0_hash 1020f184046187baa2985dbde38e0691f49c44088bca7a1842b0236c6081dc0a
%global somajor 9
%global sominor 0
%global sotiny  0
%global soversion %{somajor}.%{sominor}.%{sotiny}
Name:			libvpx
Summary:        VP8/VP9 Video Codec SDK
Version:		1.17.0
Release:        1%{?dist}
License:		BSD-3-Clause
URL:			http://www.webmproject.org/code/
Source0:        https://github.com/webmproject/libvpx/archive/refs/tags/v%{version}.tar.gz#/libvpx-%{version}.tar.gz
Source1:		vpx_config.h
Source2:		libvpx.ver
%ifarch %{ix86} x86_64
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
# /oreon:deps
%description
libvpx provides the VP8/VP9 SDK, which allows you to integrate your applications
with the VP8 and VP9 video codecs, high quality, royalty free, open source codecs
deployed on millions of computers and devices worldwide.

%package devel
Summary:		Development files for libvpx
Requires:		%{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries and headers for developing software against
libvpx.

%package utils
Summary:		VP8 utilities and tools
Requires:		%{name}%{?_isa} = %{version}-%{release}
%description utils
A selection of utilities and tools for VP8, including a sample encoder
and decoder.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libvpx-%{version}

%build

%ifarch %{ix86}
%global vpxtarget x86-linux-gcc
%else
%ifarch	x86_64
%global	vpxtarget x86_64-linux-gcc
%else
%ifarch aarch64
%global vpxtarget arm64-linux-gcc
%else
%global vpxtarget generic-gnu
%endif
%endif
%endif
%if "%{vpxtarget}" == "generic-gnu"
%global generic_target 0
%else
%global	generic_target 0
%endif
%set_build_flags
./configure --target=%{vpxtarget} \
--enable-pic --disable-install-srcs \
--enable-vp9-decoder --enable-vp9-encoder \
--enable-experimental \
--enable-vp9-highbitdepth \
--enable-debug \
%if ! %{generic_target}
--enable-shared \
%endif
%ifarch %{ix86} x86_64
--as=nasm \
%endif
--enable-install-srcs \
--prefix=%{_prefix} --libdir=%{_libdir} --size-limit=16384x16384
%make_build verbose=true
%install
make DIST_DIR=%{buildroot}%{_prefix} dist
if [ -d %{buildroot}%{_prefix}/docs ]; then
   mv %{buildroot}%{_prefix}/docs doc/
fi
pushd %{buildroot}
rm -rf .%{_prefix}/build/ .%{_prefix}/md5sums.txt .%{_libdir}*/*.a .%{_prefix}/CHANGELOG .%{_prefix}/README
mv .%{_bindir}/examples/* .%{_bindir}
rm -rf .%{_bindir}/examples
mv .%{_bindir}/postproc .%{_bindir}/vp8_postproc
mv .%{_bindir}/simple_decoder .%{_bindir}/vp8_simple_decoder
mv .%{_bindir}/simple_encoder .%{_bindir}/vp8_simple_encoder
mv .%{_bindir}/twopass_encoder .%{_bindir}/vp8_twopass_encoder
chmod 755 .%{_bindir}/*
popd
%ifarch ppc64 ppc64le
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-ppc64.h
%else
%ifarch s390 s390x
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-s390.h
%else
%ifarch %{ix86}
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-x86.h
%else
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-%{_arch}.h
%endif
%endif
%endif
cp %{SOURCE1} %{buildroot}%{_includedir}/vpx/vpx_config.h
touch -r AUTHORS %{buildroot}%{_includedir}/vpx/vpx_config.h
mv %{buildroot}%{_prefix}/src/vpx_dsp %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_mem %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_ports %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_scale %{buildroot}%{_includedir}/
rm -rf %{buildroot}%{_prefix}/src
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libvpx-devel -f %{oreon_filedir}/libvpx-devel.list
%files -n libvpx-utils -f %{oreon_filedir}/libvpx-utils.list

%changelog

%autochangelog
