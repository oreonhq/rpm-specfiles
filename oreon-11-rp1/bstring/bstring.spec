%global source0_hash caaa9770c763dfc31a34e86d4afe50a9d3b3e6c43f9b410fa4f3130192ea47f1
Name:              bstring
Version:           1.1.1
Release:        1%{?dist}
Summary:        A string abstraction data type for the C language
License:           BSD-3-Clause OR GPL-2.0-only
URL:               https://github.com/msteinert/bstring
Source0:        https://github.com/msteinert/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:            bstring-gpl-2-only-alternative.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles bstring-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bstring-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n bstring-devel -f %{oreon_filedir}/bstring-devel.list
%files -n bstring-doc -f %{oreon_filedir}/bstring-doc.list

%changelog

%autochangelog
