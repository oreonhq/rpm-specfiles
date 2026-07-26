%global source0_hash 90db08fd33e9494aea3f00f9b71cdcf3114c65457ee35558e8274df6ebac43f3

Name:              bstring
Version:           1.0.3
Release:           1%{?dist}
Summary:           A string abstraction data type for the C language
License:           BSD-3-Clause OR GPL-2.0-only
URL:               https://github.com/msteinert/bstring
Source0:           %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# https://github.com/msteinert/bstring/pull/120
Patch0:            bstring-gpl-2-only-alternative.patch

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     gcc
BuildRequires:     meson
BuildRequires:     doxygen
BuildRequires:     check-devel
BuildRequires:     sed

%description
The bstring library provides a string abstraction data type for the C language
as a memory safe alternative to null terminated buffers.

This is a fork of Paul Hsieh's Better String Library. The following features
(or mis-features, depending on your point of view) are included:

- Build system (Meson+Ninja)
- Updated test suite based on Check
- Add memory profiling with Valgrind to the workflow
- Add continuous integration via GitHub Actions
- Remove C++ wrapper code, returning this to a pure C library
- Documentation generation with Doxygen
- Other various code quality and reliability improvements

Currently this fork should be binary-compatible with the original code.
The only source incompatibility is the removal of the const_bstring type.
Just use const bstring instead.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        HTML Documentation for %{name}
BuildArch:      noarch

%description doc
The bstring library provides a string abstraction data type for the C language
as a memory safe alternative to null terminated buffers.
 
This package contains the HTML documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# change from html to docbook format
sed -i 's/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/' doc/Doxyfile.in
sed -i 's/GENERATE_HTML          = YES/GENERATE_HTML          = NO/' doc/Doxyfile.in
sed -i 's/DOCBOOK_OUTPUT         = docbook/DOCBOOK_OUTPUT         = html/' doc/Doxyfile.in
sed -i 's/strip_directory: false/strip_directory: true/' doc/meson.build
sed -i "s|/ 'doc' /|/ 'help' / 'en' /|" doc/meson.build

%build
%meson \
        -Denable-docs=true  \
        -Denable-tests=true

%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING COPYING-GPL-2
%doc README.md SECURITY.md
%{_libdir}/lib%{name}.so.1{,.*}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/bstraux.h
%{_includedir}/bstrlib.h
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING COPYING-GPL-2
%doc doc/*.md
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/%{name}

%changelog
%autochangelog
