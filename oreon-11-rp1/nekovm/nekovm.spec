%global source0_hash 702282028190dffa2078b00cca515b8e2ba889186a221df2226d2b6deb3ffaca

Name:           nekovm
Version:        2.4.1
Release:        2%{?dist}
Summary:        Neko embedded scripting language and virtual machine

# https://haxe.org/foundation/open-source.html#neko-license
License:        MIT AND LGPL-2.1-or-later

URL:            https://nekovm.org/
Source0:        https://github.com/HaxeFoundation/neko/archive/v2-4-1/neko-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  git
BuildRequires:  gc-devel
BuildRequires:  pcre2-devel
BuildRequires:  gtk3-devel
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  sqlite-devel >= 3
BuildRequires:  httpd-devel
BuildRequires:  mbedtls-devel

%description
Neko is a high-level dynamically typed programming language which can
also be used as an embedded scripting language. It has been designed
to provide a common run-time for several different languages. Neko is
not only very easy to learn and use, but also has the flexibility of
being able to extend the language with C libraries. You can even write
generators from your own language to Neko and then use the Neko
run-time to compile, run, and access existing libraries.

If you need to add a scripting language to your application, Neko
provides one of the best trade-offs available between simplicity,
extensibility and speed.

Neko allows the language designer to focus on design whilst reusing a
fast and well constructed run-time, as well as existing libraries for
accessing file system, network, databases, XML...

Neko has a compiler and virtual machine. The Virtual Machine is both
very lightweight and extremely well optimized so that it can run very
quickly. The VM can be easily embedded into any application and your
libraries are directly accessible using the C foreign function
interface.

The compiler converts a source .neko file into a byte-code .n file that
can be executed with the Virtual Machine. Although the compiler is
written in Neko itself, it is still very fast. You can use the
compiler as standalone command-line executable separated from the VM,
or as a Neko library to perform compile-and-run for interactive
languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n neko-2-4-1
%autopatch -p1

%build
# Avoid a compiler stack-overflow when building on 64 bit.
ulimit -s unlimited

%cmake . \
    -G Ninja \
    -DRELOCATABLE=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DRUN_LDCONFIG=OFF \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%cmake_build

%check
%ninja_test -C "%{_vpath_builddir}"

%install
%ninja_install -C "%{_vpath_builddir}"

%files
%doc README.md
%license LICENSE
%{_bindir}/neko
%{_bindir}/nekoc
%{_bindir}/nekoml
%{_bindir}/nekotools
%{_libdir}/libneko.so.*
%{_libdir}/neko/

%files devel
%doc CHANGES
%{_includedir}/*.h
%{_libdir}/libneko.so
%{_libdir}/cmake/*

%changelog
%autochangelog
