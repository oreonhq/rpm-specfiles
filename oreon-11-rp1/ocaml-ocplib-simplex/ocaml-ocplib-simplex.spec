%global source0_hash 4518a8c9eaaaee4626f73899a2b87a482f55c3a6995303f08eea8c952c7befa5
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ocplib-simplex
Epoch:          1
Version:        0.5.1
Release:        1%{?dist}
Summary:        Simplex algorithm for solving systems of linear inequalities
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/OCamlPro/ocplib-simplex
VCS:            git:%{url}.git
Source0:        https://github.com/OCamlPro/ocplib-simplex/archive/v%{version}/ocplib-simplex-%{version}.tar.gz
Patch:          %{name}-tests.patch
Patch:          %{name}-destdir.patch
Patch:          %{name}-autoconf.patch
Patch:          %{name}-num.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
This package contains a library implementing a simplex algorithm, in a
functional style, for solving systems of linear inequalities and optimizing
linear objective functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n ocplib-simplex-%{version}

%conf
autoconf

# Upstream's attempt to set OCAMLFIND_DESTDIR interferes with ours
sed -i '/OCAMLFIND_DESTDIR/d' Makefile.in

%build

%configure
%ifarch %{ocaml_native_compiler}
%make_build opt
%else
%make_build byte
%endif
%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR
%make_install
rm -fr %{buildroot}%{_prefix}%{_prefix}
%ocaml_files
%ifarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make local-tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocplib-simplex-devel -f %{oreon_filedir}/ocaml-ocplib-simplex-devel.list

%changelog

%autochangelog
