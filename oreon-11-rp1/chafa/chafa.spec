%global source0_hash fb995ef21dce6c73dd0dd454ba3e0f7fac08e053ea16060a2e5ce69a3746ee27
Name:           chafa
Version:        1.18.3
Release:        1%{?dist}
%global sum     Image-to-text converter for terminal
Summary:        Image-to-text converter for terminal
License:        LGPL-3.0-or-later
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  libavif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  make
# /oreon:deps
%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

It is highly configurable, with support for alpha transparency and multiple
color modes and color spaces, combining a range of Unicode characters for
optimal output.

%package libs
Summary:        %{sum} (library)
Provides:       bundled(libnsgif) = 0.2.1^chafa
Provides:       bundled(lodepng) = 20220109
%description libs
Shared library for %{name}.

%package static
Summary:        %{sum} (static library)
%description static
Static library for %{name}.

%package devel
Summary:        %{sum} (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}, such as headers.

%package doc
Summary:        %{sum} (documentation)
Recommends:     %{name}-devel
%description doc
Documentation for %{name}, such as headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure --disable-rpath
%make_build
%install
%make_install
%oreon_autofiles chafa-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles chafa-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles chafa-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles chafa-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n chafa-libs -f %{oreon_filedir}/chafa-libs.list
%files -n chafa-static -f %{oreon_filedir}/chafa-static.list
%files -n chafa-devel -f %{oreon_filedir}/chafa-devel.list
%files -n chafa-doc -f %{oreon_filedir}/chafa-doc.list

%changelog

%autochangelog
