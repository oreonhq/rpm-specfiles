# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1020f184046187baa2985dbde38e0691f49c44088bca7a1842b0236c6081dc0a
%global source1_hash 96ad7a0b3eb887e18d7046d855fdbf9c7c401e8c28ca4dab656e623806fb89de
%global source2_hash 784ac8eec65da1de51a59c0b7ee0e33a7d1887318c831f5ee970b71144951865
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global somajor 12
%global sominor 0
%global sotiny  0
%global soversion %{somajor}.%{sominor}.%{sotiny}

Name:			libvpx
Summary:		VP8/VP9 Video Codec SDK
Version:		1.17.0
Release:		1%{?dist}
License:		BSD-3-Clause
URL:			http://www.webmproject.org/code/
Source0:		https://github.com/webmproject/libvpx/archive/v%{version}.tar.gz
Source1:		vpx_config.h
Source2:		libvpx.ver
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:		make
%ifarch %{ix86} x86_64
BuildRequires:		nasm
%endif
BuildRequires:		doxygen
BuildRequires:		perl(Getopt::Long)

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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
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

%if %{generic_target}
mkdir tmp
cd tmp
ar x ../libvpx_g.a
cd ..
gcc -fPIC -shared -pthread -lm -Wl,--no-undefined -Wl,-soname,libvpx.so.%{somajor} -Wl,--version-script,%{SOURCE2} -Wl,-z,noexecstack -o libvpx.so.%{soversion} tmp/*.o
rm -rf tmp
%endif

%install
make DIST_DIR=%{buildroot}%{_prefix} dist

if [ -d %{buildroot}%{_prefix}/docs ]; then
   mv %{buildroot}%{_prefix}/docs doc/
fi

%if %{generic_target}
install -p libvpx.so.%{soversion} %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -sf libvpx.so.%{soversion} libvpx.so
ln -sf libvpx.so.%{soversion} libvpx.so.%{somajor}
ln -sf libvpx.so.%{soversion} libvpx.so.%{somajor}.%{sominor}
popd
%endif

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

%files
%license LICENSE
%doc AUTHORS CHANGELOG README
%{_libdir}/libvpx.so.%{somajor}*

%files devel
%doc docs/html/
%{_includedir}/vpx/
%{_includedir}/vpx_dsp/
%{_includedir}/vpx_mem/
%{_includedir}/vpx_ports/
%{_includedir}/vpx_scale/
%{_libdir}/pkgconfig/vpx.pc
%{_libdir}/libvpx.so

%files utils
%{_bindir}/*

%changelog
%autochangelog
