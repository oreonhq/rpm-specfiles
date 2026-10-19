%global source0_hash 724ca46761cbb776e05bb690d435e3399b55222c9157ba95cfc371eab453d8d5
%global commit 24f889aaabe33bc390b993d737d830b8dd367e61
%global date 20250205
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:       daala
Version:    0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Daala video compression
License:    BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND GPL-1.0-or-later
URL:        http://xiph.org/daala/
Source0:        https://gitlab.xiph.org/xiph/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    libs
Summary:    Daala video codec libraries
%description libs
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    devel
Summary:    Development files for the Daala video codec libraries
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package    tools
Summary:    Daala video codec tools
%description tools
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

The %{name}-tools package contains a test player and encoder plus programs for
testing %{name} support in your applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

autoreconf -vif
%configure \
    --disable-silent-rules \
    --disable-static \
    --enable-analyzer \
    --enable-float-pvq \
    --enable-tools
%make_build
%make_build tools
%install
%make_install
find %{buildroot} -name "*.la" -delete
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p \
    tools/bjontegaard \
    tools/block_size_analysis \
    tools/compute_basis \
    tools/compute_haar_basis \
    tools/cos_search \
    tools/divu_const \
    tools/downsample \
    tools/draw_zigzags \
    tools/dump_fastssim \
    tools/dump_msssim \
    tools/dump_psnr \
    tools/dump_psnrhvs \
    tools/dump_ssim \
    tools/gen_cdf \
    tools/gen_laplace_tables \
    tools/gen_sqrt_tbl \
    tools/jpegyuv \
    tools/.libs/daalainfo \
    tools/png2y4m \
    tools/to_monochrome \
    tools/trans2d \
    tools/trans_gain \
    tools/upsample \
    tools/vq_train \
    tools/y4m2png \
    tools/y4m2yuv \
    tools/yuv2yuv4mpeg \
    tools/yuvjpeg \
    %{buildroot}%{_bindir}/
rm -fr %{buildroot}/%{_docdir}
mkdir -p %{buildroot}/%{_mandir}
cp -fr doc/man/man3/ %{buildroot}/%{_mandir}
rm -f %{buildroot}/%{_mandir}/man3/_*_include_daala_.3
%oreon_autofiles daala-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles daala-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles daala-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make V=0 check
%files -f %{oreon_filedir}/main.list
%files -n daala-libs -f %{oreon_filedir}/daala-libs.list
%files -n daala-devel -f %{oreon_filedir}/daala-devel.list
%files -n daala-tools -f %{oreon_filedir}/daala-tools.list

%changelog

%autochangelog
