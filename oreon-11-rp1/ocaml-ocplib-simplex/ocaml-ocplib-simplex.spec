%global source0_hash 1c6c67cb4e5ff49c53f2abffec99032e883199be37bf2bdac8e690787b3be9d7

# NOTE: The version of this package is tied to the alt-ergo version.
# Currently, alt-ergo-free is on version 2.3.x, which requires version 0.4.x
# of this package.  DO NOT UPDATE to a newer version until a newer alt-ergo-free
# is also available.

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ocplib-simplex
Epoch:          1
Version:        0.4.1
Release:        15%{?dist}
Summary:        Simplex algorithm for solving systems of linear inequalities

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/OCamlPro/ocplib-simplex
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ocplib-simplex-%{version}.tar.gz
# Upstream patch to fix the tests
Patch:          %{name}-tests.patch
# Upstream patch to fix DESTDIR
Patch:          %{name}-destdir.patch
# Update configure.in for autoconf 2.71
Patch:          %{name}-autoconf.patch
# Adapt to ocaml-num 1.6
Patch:          %{name}-num.patch

BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  ocaml >= 4.01.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-rpm-macros

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
# The tests assume the availability of ocamlopt
%check
make local-tests
%endif

%files -f .ofiles
%doc README.md
%license LICENSE

%files devel -f .ofiles-devel
%doc extra/simplex_invariants.txt

%changelog
%autochangelog
