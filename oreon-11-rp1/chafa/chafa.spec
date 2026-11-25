# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fb995ef21dce6c73dd0dd454ba3e0f7fac08e053ea16060a2e5ce69a3746ee27

Name:           chafa
Version:        1.18.3
Release:        2%{?dist}
Summary:        Terminal graphics library and image converter
License:        LGPL-3.0-or-later
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/chafa/releases/download/%{version}/chafa-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(librsvg-2.0)

Requires:       chafa-libs%{?_isa} = %{version}-%{release}

%description
Chafa converts images into ANSI and Unicode character art for terminals.

%package libs
Summary:        Shared library for Chafa
Provides:       bundled(libnsgif) = 0.2.1
Provides:       bundled(lodepng)

%description libs
Shared library used by Chafa and applications that render terminal graphics.

%package devel
Summary:        Development files for Chafa
Requires:       chafa-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and pkg-config files for applications that use libchafa.

%prep
%oreon_sha256
%autosetup

%build
%configure --disable-rpath --disable-static --disable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
install -D -m 644 tools/completions/bash-completion.sh \
    %{buildroot}%{_datadir}/bash-completion/completions/chafa
install -D -m 644 tools/completions/zsh-completion.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_chafa
install -D -m 644 tools/completions/fish-completion.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/chafa.fish

%check
%make_build check

%files
%license COPYING.LESSER
%doc AUTHORS NEWS README README.md
%{_bindir}/chafa
%{_mandir}/man1/chafa.1*
%{_datadir}/bash-completion/completions/chafa
%{_datadir}/zsh/site-functions/_chafa
%{_datadir}/fish/vendor_completions.d/chafa.fish

%files libs
%license COPYING.LESSER
%{_libdir}/libchafa.so.0*

%files devel
%{_includedir}/chafa/
%{_libdir}/libchafa.so
%{_libdir}/pkgconfig/chafa.pc
%{_libdir}/chafa/include/chafaconfig.h
