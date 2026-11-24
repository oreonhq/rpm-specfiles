# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 278d03a0a662d00a46178afc64f32535ede2d78c603842b6fd1c55fa9cd44683
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libaribcaption
Version:        1.1.1
Release:        1%{?dist}
Summary:        Portable ARIB STD-B24 Caption Decoder/Renderer
License:        MIT
URL:            https://github.com/xqq/libaribcaption

Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-version.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(fontconfig)

%description
Decoder and renderer for handling ARIB STD-B24 based broadcast captions, making
it possible for general players to render ARIB captions with the same effect
(or even better) as Television.

Features
- Support captions in Japanese (ARIB STD-B24 JIS), Latin languages (ABNT NBR
  15606-1) and Philippine (ARIB STD-B24 UTF-8)
- Full support for rendering ARIB additional symbols (Gaiji) and DRCScharacters
- Lightweight and portable implementation that works on various platforms
- Performance optimized (SSE2 on x86/x64) graphics rendering
- Multiple text rendering backend driven by DirectWrite / CoreText / FreeType
- Zero third-party dependencies on Windows (using DirectWrite) and macOS / iOS
  (using CoreText)
- Built-in font fallback mechanism
- Built-in DRCS converting table for replacing / rendering known DRCS characters
  into / by alternative Unicode

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkg-config

%description    devel
Decoder and renderer for handling ARIB STD-B24 based broadcast captions, making
it possible for general players to render ARIB captions with the same effect
(or even better) as Television.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/aribcaption/*
%{_libdir}/cmake/aribcaption/aribcaption-*.cmake
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
