%global source0_hash 427a0a8e04288a62c11c2048c5d0f5cb19fb331dde65a39c9909d5c2d652e0ad

%global apiver 0

Name:           capypdf
Version:        0.11.0
Release:        8%{?dist}
Summary:        Fully color-managed PDF generation library

License:        Apache-2.0
URL:            https://github.com/jpakkane/capypdf
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

# Backports from upstream
## From: https://github.com/jpakkane/capypdf/commit/bf493d8340cba0020e0feadc96a0900580ccf23f
Patch0001:      0001-Building-devtools-is-now-optional.patch

BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(freetype2)

%description
This is a library for generating PDF files. It aims to be very low level.
It does not have its own document model, it merely exposes PDF primitives
directly.

%files
%license COPYING
%doc readme.md
%{_libdir}/lib%{name}.so.%{apiver}
%{_libdir}/lib%{name}.so.%{version}

%dnl --------------------------------------------------------------------

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the files for building applications that use
%{name}.

%files devel
%{_includedir}/%{name}-%{apiver}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%dnl --------------------------------------------------------------------

%package -n python3-%{name}
Summary:        Python 3 module for %{name}
BuildRequires:  python3-devel
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}
This package provides the files for building applications that use
%{name}.

%files -n python3-%{name}
%pycached %{python3_sitelib}/%{name}.py

%dnl --------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%meson

%build
%meson_build

%install
%meson_install

%changelog
%autochangelog
