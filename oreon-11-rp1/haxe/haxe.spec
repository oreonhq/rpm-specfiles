%global source0_hash d100de5f606c18530371eed83abacc1c208266db25cfe2fac3877430353a6f2e

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global commit_haxelib 4000137b822989eacb1e1c370470ee1c9ecdf4b8
%global commit_hx3compat f1f18201e5c0479cb5adf5f6028788b37f37b730

Name:           haxe
Version:        4.3.7
Release:        5%{?dist}
Summary:        Multi-target universal programming language

# As described in https://haxe.org/foundation/open-source.html:
#   * The Haxe Compiler - GPLv2+
#   * The Haxe Standard Library - MIT
#
# The source files:
#   * All files in the std folder is MIT licensed.
#   * Ocamllibs in the libs folder:
#     * extc, ilib, javalib, neko, swflib - GPLv2+
#     * pcre - LGPLv2+
#     * everything else - LGPLv2.1+
# Automatically converted from old format: GPLv2+ and MIT and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND MIT AND LGPL-2.0-or-later

URL:            https://haxe.org/

Source0:        https://github.com/HaxeFoundation/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/HaxeFoundation/haxelib/archive/%{commit_haxelib}.tar.gz#/haxelib-%{commit_haxelib}.tar.gz
Source2:        https://github.com/HaxeFoundation/hx3compat/archive/%{commit_hx3compat}.tar.gz#/hx3compat-%{commit_hx3compat}.tar.gz

BuildRequires:  make
BuildRequires:  nekovm-devel >= 2.3.0
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-camlp-streams
BuildRequires:  ocaml-sedlex-devel >= 2.0
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-extlib-devel >= 1.7.8
BuildRequires:  ocaml-ptmap-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  ocaml-luv-devel >= 0.5.13
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(libuv)
BuildRequires:  mbedtls-devel
BuildRequires:  cmake
BuildRequires:  help2man
Requires:       nekovm >= 2.3.0
Requires:       %{name}-stdlib = %{version}

%description
Haxe is an open source toolkit based on a modern,
high level, strictly typed programming language, a cross-compiler,
a complete cross-platform standard library and ways to access each
platform's native capabilities.

%package        stdlib
Summary:        The Haxe standard library
BuildArch:      noarch

%description    stdlib
The %{name}-stdlib package contains the standard library used
by the Haxe compiler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
pushd extra/haxelib_src && tar -xf %{SOURCE1} --strip-components=1 && popd
pushd extra/haxelib_src/hx3compat && tar -xf %{SOURCE2} --strip-components=1 && popd

%build
# TODO: Please submit an issue to upstream (rhbz#2380634)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# note that the Makefile does not support parallel building
make

# Recompile haxelib.
#
# In the default Makefile, haxelib is built using `nekotools boot ...`.
# It produces haxelib by concatenating the neko binary with haxelib neko bytecode.
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/FFE3B3TGLXMVPDIZGAOJYHFOJMBGUQUL/
#
# Instead, use the haxelib CMake, which use `nekotools boot -c ...`
# to produce a C source code and build it with standard C toolchain.
rm ./haxelib
%cmake -S extra/haxelib_src -DHAXE_COMPILER="$(realpath haxe)"
%cmake_build
mv %__cmake_builddir/haxelib .

chmod 755 haxe haxelib

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -p haxe %{buildroot}%{_bindir}
cp -p haxelib %{buildroot}%{_bindir}
cp -rfp std %{buildroot}%{_datadir}/%{name}

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man ./haxe --version-option=-version --no-discard-stderr --no-info --output=%{buildroot}%{_mandir}/man1/haxe.1
help2man ./haxelib --help-option=help --version-option=version --no-info --output=%{buildroot}%{_mandir}/man1/haxelib.1

%check
%{buildroot}%{_bindir}/haxe -version
%{buildroot}%{_bindir}/haxelib version

# should not call haxe from the source dir or it will get confused about the std lib
pushd %{buildroot}
%{buildroot}%{_bindir}/haxe -v Std
popd

%files
%doc README.md
%license extra/LICENSE.txt
%{_bindir}/haxe
%{_bindir}/haxelib
%{_mandir}/man1/haxe.1*
%{_mandir}/man1/haxelib.1*

%files stdlib
%doc README.md
%license extra/LICENSE.txt
%{_datadir}/%{name}/

%changelog
%autochangelog
