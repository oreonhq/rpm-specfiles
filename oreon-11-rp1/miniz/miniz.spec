%global source0_hash 98468f8924934b723276680f85238b6c78bf1f8b49b4459cc9b7214a20e2e9fb

Name:       miniz
Version:    3.1.2
Release:    1%{?dist}
Summary:    Compression library implementing the zlib and Deflate
# examples/example1.c:  Unlicense (refers to "unlicense" statement at the end
#                       of tinfl.c from miniz-1.15)
# examples/example2.c:  Unlicense
# examples/example3.c:  Unlicense
# examples/example4.c:  Unlicense
# examples/example5.c:  Unlicense ("Public domain. See unlicense statement")
# examples/example6.c:  Unlicense
# LICENSE:  MIT text
# miniz.c:  MIT
# miniz.h:  Unlicense (See "unlicense" statement at the end of this file.)
# readme.md:    MIT
License:    MIT AND Unlicense
URL:        https://github.com/richgel999/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Adjust examples for building against a system miniz library,
# not suitable for upstream that prefers a copy-lib approach.
Patch0:     miniz-2.2.0-Examples-to-include-system-miniz.h.patch
BuildRequires:  cmake
BuildRequires:  coreutils
# diffutils for cmp
BuildRequires:  diffutils
%if "%{toolchain}" == "gcc"
BuildRequires:  gcc
BuildRequires:  gcc-g++
%else
%if "%{toolchain}" == "clang"
BuildRequires:  clang
%else
%{error:Unknown toolchain.}
%endif
%endif
BuildRequires:  dos2unix

%description
Miniz is a lossless, high performance data compression library in a single
source file that implements the zlib (RFC 1950) and Deflate (RFC 1951)
compressed data format specification standards. It supports the most commonly
used functions exported by the zlib library, but is a completely independent
implementation so zlib's licensing requirements do not apply. It also
contains simple to use functions for writing PNG format image files and
reading/writing/appending ZIP format archives. Miniz's compression speed has
been tuned to be comparable to zlib's, and it also has a specialized real-time
compressor function designed to compare well against fastlz/minilzo.

%package devel
Provides:       miniz-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:    Development files for the %{name} library
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   cmake-filesystem
Requires:   pkg-config%{?_isa}

%description devel
Header files for developing applications that use the %{name} library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
%patch -P0 -p1

# Normalize end-of-lines
dos2unix -k ChangeLog.md LICENSE

%build
%cmake
%cmake_build

%install
%cmake_install

%check
pushd bin
for EXAMPLE in *; do
    case "$EXAMPLE" in
        example3)
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}" c ../readme.md readme.md.z
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}" d readme.md.z readme.md
            cmp ../readme.md readme.md
            ;;
        example4)
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}" readme.md.z readme.md
            cmp ../readme.md readme.md
            ;;
        example5)
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}" c ../readme.md readme.md.z
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}" d readme.md.z readme.md
            cmp ../readme.md readme.md
            ;;
        *)
            LD_LIBRARY_PATH=../%{__cmake_builddir} "./${EXAMPLE}"
            ;;
    esac
done

%files
%license LICENSE
%doc ChangeLog.md readme.md
%{_libdir}/lib%{name}.so.{3,%{version}}

%files devel
%doc examples/*.c
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
