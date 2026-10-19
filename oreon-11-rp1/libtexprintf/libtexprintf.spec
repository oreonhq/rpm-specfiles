%global source0_hash c50a44e33eba551526ff553c0af0bdd3f3a219d8ed60f11fcd9d7b30cd028af1
Name:           libtexprintf
Version:        1.25
Release:        7%{?dist}
Summary:        Formatted Output with tex-like syntax support
License:        GPL-3.0-only
URL:            https://github.com/bartp5/libtexprintf
Source0:        https://github.com/bartp5/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch:          clean-printf.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The utftex program and underlying libtexprintf library provide tools to
pretty print math in mono-space fonts, using a tex-like syntax. It
produces UTF-8 encoded text. The program was inspired by asciiTeX, and
the improved asciiTeX fork. However, utftex supports much more TeX
syntax and contains extensive Unicode tables to map latex commands
to Unicode symbols. Use libtexprintf/utftex to unlock the math
capabilities of Unicode in mono-space text applications.

Note that how the equations look depends strongly on the font you use.
Naturally, one needs a monospace font with good Unicode support for
the symbols you use. A good monospace font for math is, for example,
JuliaMono.

%package devel
Summary: Development headers for libtexprintf
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for libtexprintf including header file.

%package tools
Summary: The utftex and utfinfo binaries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
utftex is a command line utility to format math.
utfstringinfo is a command line utility to analyze UTF8-strings.

%package static
Summary: Static libtexprintf library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static

Provides static libtexprintf library for use in compiling
applications that need it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libtexprintf-devel -f %{oreon_filedir}/libtexprintf-devel.list
%files -n libtexprintf-tools -f %{oreon_filedir}/libtexprintf-tools.list
%files -n libtexprintf-static -f %{oreon_filedir}/libtexprintf-static.list

%changelog

%autochangelog
