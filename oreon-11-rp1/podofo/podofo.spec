%global source0_hash 02815b21a51632c2849d41b067597e9356bbc54bad0efcd84c902b555c203ce7

%if 0%{?fedora} && ! 0%{?flatpak}
%bcond_without mingw
%else
%bcond_with mingw
%endif

#global pre rc1
%global podofo_resources_commit 394fcb3ea4c8e89bbabafbc1aa6caf20f801620c

Name:           podofo
Version:        1.0.3
Release:        3%{?dist}
Summary:        Tools and libraries to work with the PDF file format

License:        LGPL-2.0-or-later
URL:            https://github.com/podofo/podofo
Source0:        https://github.com/podofo/podofo/archive/%{version}%{?pre:-%pre}/%{name}-%{version}%{?pre:-%pre}.tar.gz
Source1:        https://github.com/podofo/podofo-resources/archive/%{podofo_resources_commit}/podofo-resources-%{podofo_resources_commit}.tar.gz

# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch1:         podofo_CVE-2019-20093.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  ghostscript
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  zlib-devel
# For tests
BuildRequires:  google-noto-sans-fonts

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-fontconfig
BuildRequires: mingw32-freetype
BuildRequires: mingw32-libidn
BuildRequires: mingw32-libjpeg
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-openssl
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-fontconfig
BuildRequires: mingw64-freetype
BuildRequires: mingw64-libidn
BuildRequires: mingw64-libjpeg
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-openssl
BuildRequires: mingw64-zlib
%endif

Obsoletes:      %{name}-libs < 0.10.0-1
Provides:       %{name} < 0.10.0-1
Provides:       %{name}-libs = %{version}-%{release}

%description
PoDoFo is a library to work with the PDF file format. The name comes from
the first letter of PDF (Portable Document Format). A few tools to work
with PDF files are already included in the PoDoFo package.

The PoDoFo library is a free, portable C++ library which includes classes
to parse PDF files and modify their contents into memory. The changes can be
written back to disk easily. The parser can also be used to extract
information from a PDF file (for example the parser could be used in a PDF
viewer). Besides parsing PoDoFo includes also very simple classes to create
your own PDF files. All classes are documented so it is easy to start writing
your own application using PoDoFo.

%package devel
Summary:        Development files for %{name} library
Requires:       openssl-devel%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and documentation for the %{name} library.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-tools < 0.10.0-1
Provides:      mingw32-%{name}-tools = %{version}-%{release}

%description -n mingw32-%{name}-tools
Tools for the MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-tools < 0.10.0-1
Provides:      mingw64-%{name}-tools = %{version}-%{release}

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}-tools
Tools for the MinGW Windows %{name} library.

%{?mingw_debug_package}

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}
tar xf %{SOURCE1} -C extern/resources --strip-components=1

# disable timestamps in docs
echo "HTML_TIMESTAMP = NO" >> Doxyfile

%build
# Natve build
%cmake
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DPODOFO_BUILD_TEST=OFF
%mingw_make_build
%endif

# Doc build
doxygen
# set timestamps on generated files to some constant
find html -exec touch -r %{SOURCE0} {} \;

%install
%cmake_install

%if %{with mingw}
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

%mingw_debug_install_post
%endif

%check
%ifarch i686
%ctest -E TestMaxObjectCount
%else
%ctest
%endif

%files
%doc AUTHORS.md CHANGELOG.md README.md TODO.md
%license COPYING
%{_libdir}/*.so.1.0.3
%{_libdir}/*.so.3

%files devel
%doc html examples
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libpodofo.dll
%{mingw32_libdir}/libpodofo.dll.a
%{mingw32_libdir}/cmake/%{name}/
%{mingw32_libdir}/pkgconfig/libpodofo.pc
%{mingw32_includedir}/podofo/

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libpodofo.dll
%{mingw64_libdir}/libpodofo.dll.a
%{mingw64_libdir}/cmake/%{name}/
%{mingw64_libdir}/pkgconfig/libpodofo.pc
%{mingw64_includedir}/podofo/
%endif

%changelog
%autochangelog
