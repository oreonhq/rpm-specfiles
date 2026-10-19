%global source0_hash 9218e62793116d42a9f6d14cd9348518b27f382096eea3d0f2d1a24616bb5884
%bcond_without mingw
Name:          tesseract
Version:       5.5.3
Release:        1%{?dist}
Summary:        Raw OCR Engine
License:       Apache-2.0
URL:           https://github.com/tesseract-ocr/%{name}
Source0:        https://github.com/%{name}-ocr/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:        tesseract_cmake.patch
%if %{with mingw}
%endif
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/asciidoc
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  leptonica-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-giflib
BuildRequires:  mingw32-icu
BuildRequires:  mingw32-leptonica
BuildRequires:  mingw32-libgomp
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-giflib
BuildRequires:  mingw64-icu
BuildRequires:  mingw64-leptonica
BuildRequires:  mingw64-libgomp
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-pango
BuildRequires:  pango-devel
# /oreon:deps
%description

%package devel
Summary:       Development files for %{name}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description devel

The %{name}-devel package contains header file for
developing applications that use %{name}.

%package libs
Summary:       Shared libraries for %{name}
Conflicts:     %{name} < 5.4.1-4
Requires:      %{name}-common = %{version}-%{release}
%description libs

The %{name}-libs package contains shared libraries
for %{name}.

%package common
Summary:       Configuration files for ${name}
Conflicts:     %{name} < 5.5.0-5
Requires:      tesseract-langpack-eng
BuildArch:     noarch
%description common

The %{name}-common package contains configuration files for %{name}.

%package tools
Summary:       Training tools for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description tools

The %{name}-tools package contains tools for training %{name}.

%package -n mingw32-%{name}
Summary:       MinGW Windows tesseract-ocr library
BuildArch:     noarch
%description -n mingw32-%{name}
MinGW Windows tesseract-ocr library.

%package -n mingw32-%{name}-tools
Summary:       MinGW Windows tesseract-ocr library tools
Requires:      mingw32-%{name} = %{version}-%{release}
BuildArch:     noarch
%description -n mingw32-%{name}-tools
MinGW Windows tesseract-ocr library tools.

%package -n mingw64-%{name}
Summary:       MinGW Windows tesseract-ocr library
BuildArch:     noarch
%description -n mingw64-%{name}
MinGW Windows tesseract-ocr library.

%package -n mingw64-%{name}-tools
Summary:       MinGW Windows tesseract-ocr library tools
Requires:      mingw64-%{name} = %{version}-%{release}
BuildArch:     noarch
%description -n mingw64-%{name}-tools
MinGW Windows tesseract-ocr library tools.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DTESSDATA_PREFIX=%{_datadir}/%{name}
%cmake_build
man_xslt=http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
for file in doc/*.asc; do
    asciidoc -b docbook -d manpage -o - $file | XML_CATALOG_FILES=%{_sysconfdir}/xml/catalog xsltproc --nonet -o ${file/.asc/} $man_xslt -
done
%if %{with mingw}
MINGW32_CMAKE_ARGS=-DTESSDATA_PREFIX=%{mingw32_datadir}/%{name} \
MINGW64_CMAKE_ARGS=-DTESSDATA_PREFIX=%{mingw64_datadir}/%{name}
%mingw_cmake -DSW_BUILD=OFF -DLEPT_TIFF_RESULT=1
%mingw_make_build
%endif
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/{man1,man5}/
cp -a doc/*.1 %{buildroot}%{_mandir}/man1/
cp -a doc/*.5 %{buildroot}%{_mandir}/man5/
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n tesseract-devel -f %{oreon_filedir}/tesseract-devel.list
%files -n tesseract-libs -f %{oreon_filedir}/tesseract-libs.list
%files -n tesseract-common -f %{oreon_filedir}/tesseract-common.list
%files -n tesseract-tools -f %{oreon_filedir}/tesseract-tools.list
%files -n mingw32-tesseract -f %{oreon_filedir}/mingw32-tesseract.list
%files -n mingw32-tesseract-tools -f %{oreon_filedir}/mingw32-tesseract-tools.list
%files -n mingw64-tesseract -f %{oreon_filedir}/mingw64-tesseract.list
%files -n mingw64-tesseract-tools -f %{oreon_filedir}/mingw64-tesseract-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.5.2-2
- Prepare for Oreon 11 (RP1)
