%global source0_hash none

#global pre beta.4

%if 0%{?rhel}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          tesseract
Version:       5.5.2
Release:       2%{?dist}
Summary:       Raw OCR Engine

License:       Apache-2.0
URL:           https://github.com/tesseract-ocr/%{name}
Source0:       https://github.com/tesseract-ocr/tesseract/archive/%{version}%{?pre:-%pre}/%{name}-%{version}%{?pre:-%pre}.tar.gz

# Fix library name case
# Build training libs statically
Patch1:        tesseract_cmake.patch


BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: gcc-c++
BuildRequires: giflib-devel
BuildRequires: leptonica-devel
BuildRequires: libicu-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtool
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: pango-devel
BuildRequires: /usr/bin/asciidoc
BuildRequires: /usr/bin/xsltproc

%if %{with mingw}
BuildRequires: mingw32-curl
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-giflib
BuildRequires: mingw32-binutils
BuildRequires: mingw32-icu
BuildRequires: mingw32-leptonica
BuildRequires: mingw32-libgomp
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-pango

BuildRequires: mingw64-curl
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-giflib
BuildRequires: mingw64-binutils
BuildRequires: mingw64-icu
BuildRequires: mingw64-leptonica
BuildRequires: mingw64-libgomp
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-pango
%endif

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%global _description %{expand:
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.}

%description %_description


%package devel
Summary:       Development files for %{name}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %_description

The %{name}-devel package contains header file for
developing applications that use %{name}.


%package libs
Summary:       Shared libraries for %{name}
Conflicts:     %{name} < 5.4.1-4
Requires:      %{name}-common = %{version}-%{release}

%description libs %_description

The %{name}-libs package contains shared libraries
for %{name}.


%package common
Summary:       Configuration files for ${name}
Conflicts:     %{name} < 5.5.0-5
Requires:      tesseract-langpack-eng
BuildArch:     noarch

%description common %_description

The %{name}-common package contains configuration files for %{name}.


%package tools
Summary:       Training tools for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools %_description

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}


%build
# Native build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DTESSDATA_PREFIX=%{_datadir}/%{name}
%cmake_build

# Manually build manfiles, cmake does not build them
man_xslt=http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
for file in doc/*.asc; do
    asciidoc -b docbook -d manpage -o - $file | XML_CATALOG_FILES=%{_sysconfdir}/xml/catalog xsltproc --nonet -o ${file/.asc/} $man_xslt -
done

%if %{with mingw}
# MinGW build
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
%endif


%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/tesseract.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/libcommon_training.a
%{_libdir}/libunicharset_training.a
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.5.5
%{_libdir}/lib%{name}.so.%{version}

%files common
%license LICENSE
%{_datadir}/%{name}/

%files tools
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/cntraining
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/lstmeval
%{_bindir}/lstmtraining
%{_bindir}/merge_unicharsets
%{_bindir}/mftraining
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%{_mandir}/man1/ambiguous_words.1*
%{_mandir}/man1/classifier_tester.1*
%{_mandir}/man1/cntraining.1*
%{_mandir}/man1/combine_lang_model.1*
%{_mandir}/man1/combine_tessdata.1*
%{_mandir}/man1/dawg2wordlist.1*
%{_mandir}/man1/lstmeval.1*
%{_mandir}/man1/lstmtraining.1*
%{_mandir}/man1/merge_unicharsets.1*
%{_mandir}/man1/mftraining.1*
%{_mandir}/man1/set_unicharset_properties.1*
%{_mandir}/man1/shapeclustering.1*
%{_mandir}/man1/text2image.1*
%{_mandir}/man1/unicharset_extractor.1*
%{_mandir}/man1/wordlist2dawg.1*
%{_mandir}/man5/unicharambigs.5.gz*
%{_mandir}/man5/unicharset.5.gz*

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/libtesseract-55.dll
%{mingw32_includedir}/tesseract/
%{mingw32_libdir}/libtesseract.dll.a
%{mingw32_libdir}/libcommon_training.a
%{mingw32_libdir}/libunicharset_training.a
%{mingw32_libdir}/pkgconfig/tesseract.pc
%{mingw32_libdir}/cmake/%{name}/
%{mingw32_datadir}/%{name}/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/libtesseract-55.dll
%{mingw64_includedir}/tesseract/
%{mingw64_libdir}/libtesseract.dll.a
%{mingw64_libdir}/libcommon_training.a
%{mingw64_libdir}/libunicharset_training.a
%{mingw64_libdir}/pkgconfig/tesseract.pc
%{mingw64_libdir}/cmake/%{name}/
%{mingw64_datadir}/%{name}/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.5.2-2
- Prepare for Oreon 11 (RP1)
