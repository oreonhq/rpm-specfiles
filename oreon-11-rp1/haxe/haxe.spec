%global source2_hash d100de5f606c18530371eed83abacc1c208266db25cfe2fac3877430353a6f2e
%global source1_hash d89c3f551d4808b7a57e5615b312aed23cad4e06fe572cdbae0ec89c9f0b9601
%global source0_hash a3fc0d66dbbe36c0617079a6e9f09881df0b4485d725e4763ebfc8cd7c932d46
ExcludeArch: %{ix86}
%global commit_haxelib 4000137b822989eacb1e1c370470ee1c9ecdf4b8
%global commit_hx3compat f1f18201e5c0479cb5adf5f6028788b37f37b730
Name:           haxe
Version:        4.3.7
Release:        1%{?dist}
Summary:        Multi-target universal programming language
License:        GPL-2.0-or-later AND MIT AND LGPL-2.0-or-later
URL:            https://haxe.org/
Source0:        https://github.com/HaxeFoundation/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/HaxeFoundation/haxelib/archive/%{commit_haxelib}.tar.gz#/haxelib-%{commit_haxelib}.tar.gz
Source2:        https://github.com/HaxeFoundation/hx3compat/archive/%{commit_hx3compat}.tar.gz#/hx3compat-%{commit_hx3compat}.tar.gz
Requires:       nekovm >= 2.3.0
Requires:       %{name}-stdlib = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  mbedtls-devel
BuildRequires:  nekovm-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-luv-devel
BuildRequires:  ocaml-ptmap-devel
BuildRequires:  ocaml-sedlex-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(libuv)
BuildRequires:  zlib-devel
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
make
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
mkdir -p %{buildroot}%{_mandir}/man1
help2man ./haxe --version-option=-version --no-discard-stderr --no-info --output=%{buildroot}%{_mandir}/man1/haxe.1
help2man ./haxelib --help-option=help --version-option=version --no-info --output=%{buildroot}%{_mandir}/man1/haxelib.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{buildroot}%{_bindir}/haxe -version
%{buildroot}%{_bindir}/haxelib version
pushd %{buildroot}
%{buildroot}%{_bindir}/haxe -v Std
popd
%files -f %{oreon_filedir}/main.list
%files -n haxe-stdlib -f %{oreon_filedir}/haxe-stdlib.list

%changelog

%autochangelog
