%global source0_hash 3fc2bee78dfb7c41fd9605061fc69138db7df007eae2f669a1f56e8bacef74ab

%{?mingw_package_header}

Name:           mingw-orc
Version:        0.4.40
Release:        4%{?dist}
Summary:        Cross compiled Oil Run-time Compiler

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://code.entropywave.com/projects/orc/
Source0:        http://gstreamer.freedesktop.org/src/orc/orc-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

# Mingw32
%package -n mingw32-orc
Summary: %{summary}

%description -n mingw32-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw32-orc-compiler
Summary:        Orc compiler
Requires:       mingw32-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw32-orc-compiler
The Orc compiler, to produce optimized code.

# Mingw64
%package -n mingw64-orc
Summary: %{summary}

%description -n mingw64-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw64-orc-compiler
Summary:        Orc compiler
Requires:       mingw64-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw64-orc-compiler
The Orc compiler, to produce optimized code.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n orc-%{version}

%build
%mingw_meson -Dgtk_doc=disabled
%mingw_ninja

%install
%mingw_ninja_install

# Mingw32
%files -n mingw32-orc
%license COPYING
%doc README
%{mingw32_bindir}/liborc-0.4-0.dll
%{mingw32_bindir}/liborc-test-0.4-0.dll
%{mingw32_bindir}/orc-bugreport.exe
%{mingw32_includedir}/orc-0.4/
%{mingw32_libdir}/liborc-0.4.dll.a
%{mingw32_libdir}/liborc-test-0.4.dll.a
%{mingw32_libdir}/pkgconfig/orc-0.4.pc
%{mingw32_libdir}/pkgconfig/orc-test-0.4.pc

%files -n mingw32-orc-compiler
%{mingw32_bindir}/orcc.exe

# Mingw64
%files -n mingw64-orc
%license COPYING
%doc README
%{mingw64_bindir}/liborc-0.4-0.dll
%{mingw64_bindir}/liborc-test-0.4-0.dll
%{mingw64_bindir}/orc-bugreport.exe
%{mingw64_includedir}/orc-0.4/
%{mingw64_libdir}/liborc-0.4.dll.a
%{mingw64_libdir}/liborc-test-0.4.dll.a
%{mingw64_libdir}/pkgconfig/orc-0.4.pc
%{mingw64_libdir}/pkgconfig/orc-test-0.4.pc

%files -n mingw64-orc-compiler
%{mingw64_bindir}/orcc.exe

%changelog
%autochangelog
