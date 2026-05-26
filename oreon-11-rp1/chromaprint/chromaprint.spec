# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9d33482e56a1389a37a0d6742c376139fa43e3b8a63d29003222b93db2cb40da
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# The presence of this macro ensures the disttag changes
# when set in side tags
%bcond_with bootstrap

%if 0%{?rhel} && 0%{?rhel} < 9
%bcond_with ffmpeg
%else
%bcond ffmpeg %{?_with_bootstrap:0}%{!?_with_bootstrap:1}
%endif
# Globing of libraries is against the packging guidelines
%global sover 1


Name:           chromaprint
Version:        1.6.0
Release:        2%{?dist}
Summary:        Library implementing the AcoustID fingerprinting

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.acoustid.org/chromaprint
Source:         https://github.com/acoustid/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fftw-devel >= 3
BuildRequires:  ninja-build

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+

%package -n libchromaprint
Summary:        Library implementing the AcoustID fingerprinting
Obsoletes:      python-chromaprint < 0.6-3

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+

%package -n libchromaprint-devel
Summary:        Headers for developing programs that will use %{name}
Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%if %{with ffmpeg}
%package tools
Summary:        Chromaprint audio fingerprinting tools
BuildRequires:  ffmpeg-free-devel
Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%description tools
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

This is a set of Chromaprint tools related to acoustic fingerprinting
featuring fpcalc an standalone AcoustID tool used by Picard.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+
%endif

%prep
%oreon_verify_sources
%autosetup -p1

%build
# examples and cli tools require ffmpeg, so turn off.
%cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTS=ON \
        -DBUILD_TOOLS=%{?with_ffmpeg:ON}%{!?with_ffmpeg:OFF}

%cmake_build

%install
%cmake_install

rm  -f %{buildroot}%{_libdir}/lib*.la

%check
%ctest

%files -n libchromaprint
%doc NEWS.txt README.md
%license LICENSE.md
%{_libdir}/lib*.so.%{sover}*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/Chromaprint/
%{_libdir}/cmake/Chromaprint/*.cmake

%if %{with ffmpeg}
%files tools
%{_bindir}/fpcalc
%endif

%changelog
* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-2
- Import from Fedora 43 dist-git for Oreon 11 RP1
