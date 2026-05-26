# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7e2507fdef7b57c87b461d0f2515771b70699a02c8675b51785a73400b3c53a1
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global somajor 4

# Tests are flaky in Koji
%bcond_with tests

Name:           librist
Version:        0.2.7
Release:        11%{?dist}
Summary:        Library for Reliable Internet Stream Transport (RIST) protocol

# Everything used is BSD-2-Clause except getopt-shim, which is ISC as well
License:        BSD-2-Clause and ISC
URL:            https://code.videolan.org/rist/librist
Source0:        https://code.videolan.org/rist/librist/-/archive/v0.2.7/librist-v0.2.7.tar.gz

# Backport from upstream
## From: https://code.videolan.org/rist/librist/-/commit/809390b3b75a259a704079d0fb4d8f1b5f7fa956
Patch0001:      0001-meson.build-fix-reference-to-libcjson-pc-file.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  libcmocka-devel
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(libcjson)

%description
A library that can be used to speak the RIST protocol (as defined by Video
Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Technical documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains technical documentation for
developing applications that use %{name}.


%package -n     rist-tools
Summary:        User tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n rist-tools
This package contains the user tools for the RIST protocol library.


%prep
%oreon_verify_sources
%autosetup -n %{name}-v%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
# Strip unwanted executable bits
chmod -x %{buildroot}%{_includedir}/%{name}/*.h
chmod -x docs/*

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -av docs/* %{buildroot}%{_docdir}/%{name}


%if %{with tests}
%check
%meson_test
%endif


%files
%doc README.md CONTRIBUTING.md
%license COPYING
%{_libdir}/*.so.%{somajor}{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING
# Co-own with librist package
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/VSF_TR-06-1.pdf
%doc %{_docdir}/%{name}/VSF_TR-06-2.pdf
%doc %{_docdir}/%{name}/librist_logo.png

%files -n rist-tools
%{_bindir}/rist*


%changelog
* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.7-11
- Import from Fedora 43 dist-git for Oreon 11 RP1
