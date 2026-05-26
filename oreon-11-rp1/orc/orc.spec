# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 cb1bfd4f655289cd39bc04642d597be9de5427623f0861c1fc19c08d98467fa2
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		orc
Version:	0.4.41
Release:	3%{?dist}
Summary:	The Oil Run-time Compiler

License:	BSD-2-Clause AND BSD-3-Clause
URL:		http://cgit.freedesktop.org/gstreamer/orc/
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz

BuildRequires:	meson >= 0.47.0
BuildRequires:  gcc
BuildRequires:	gtk-doc

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package doc
Summary:	Documentation for Orc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for Orc.

%package devel
Summary:	Development files and libraries for Orc
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-compiler
Requires:	pkgconfig

%description devel
This package contains the files needed to build packages that depend
on orc.

%package compiler
Summary:	Orc compiler
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description compiler
The Orc compiler, to produce optimized code.


%prep
%oreon_verify_sources
%autosetup -p1

%build
%meson -D default_library=shared
%meson_build

%install
%meson_install

# Remove unneeded files.
find %{buildroot}/%{_libdir} -name \*.a -delete
rm -rf %{buildroot}/%{_libdir}/orc

%check
%meson_test

%ldconfig_scriptlets


%files
%license COPYING
%doc README
%{_libdir}/liborc-0.4.so.0*
%{_libdir}/liborc-test-0.4.so*
%{_bindir}/orc-bugreport

%files doc
%doc %{_datadir}/gtk-doc/html/orc/

%files devel
%doc examples/*.c
%{_includedir}/%{name}-0.4/
%{_libdir}/liborc-0.4.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_libdir}/pkgconfig/orc-test-0.4.pc

%files compiler
%{_bindir}/orcc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.41-3
- Prepare for Oreon 11 (RP1)
