%global source0_hash e0c6d8e9801d905343eb92a79a5bd46687c2781c287641f6cf7c13dd35b6e4cd
ExcludeArch: %{ix86}
%bcond_with    camomile
%bcond_with    tests
Name:           ocaml-gettext
Version:        0.5.0
Release:        1%{?dist}
Summary:        OCaml library for i18n
License:        LGPL-2.1-or-later with OCaml-LGPL-linking-exception
URL:            https://github.com/gildor478/ocaml-gettext
VCS:            git:%{url}.git
Source0:        https://github.com/gildor478/ocaml-gettext/archive/refs/tags/v0.5.0.tar.gz#/ocaml-gettext-0.5.0.tar.gz
Patch:          https://github.com/gildor478/ocaml-gettext/pull/37.patch
Patch:        https://github.com/gildor478/ocaml-gettext/pull/37.patch
%if %{with tests}
%endif
%if %{with camomile}
%endif
%if %{with camomile}
Requires:       ocaml-camomile-data
%endif
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-fileutils-devel
BuildRequires:  ocaml-ounit-devel
# /oreon:deps
%description
Ocaml-gettext provides support for internationalization of Ocaml
programs.

Constraints :

* provides a pure Ocaml implementation,
* the API should be as close as possible to GNU gettext,
* provides a way to automatically extract translatable
  strings from Ocaml source code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-fileutils-devel%{?_isa} >= 0.6.6
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%if %{with camomile}
%package        camomile
Summary:        Parts of %{name} which depend on Camomile
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    camomile
The %{name}-camomile package contains the parts of %{name} which
depend on Camomile.

%package        camomile-devel
Summary:        Development files for %{name}-camomile
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-camomile%{?_isa} = %{version}-%{release}
Requires:       ocaml-camomile-devel%{?_isa}
%description    camomile-devel
The %{name}-camomile-devel package contains libraries and
signature files for developing applications that use
%{name}-camomile.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Remove ocaml-seq dependency.  See note above.
sed -i 's/ seq / /' test/dune

%if %{without camomile}
# Remove dependency on camomile.
rm -f gettext-camomile.opam
rm -r src/lib/gettext-camomile
rm -r test/test-camomile
sed -i -e 's/camomile//' `find -name dune`
awk -i inplace -v RS='^\\(package' -v ORS= \
     '{while(sub(/\(package\n *\(name gettext-camomile\).*\)\)\)\)/,""));} {print}' dune-project
%endif

%build

%dune_build
%install
%dune_install -s
sed -i '\@%{_bindir}@d;\@%{_mandir}@d' .ofiles-gettext
cat .ofiles-gettext-stub >> .ofiles-gettext
cat .ofiles-gettext-stub-devel >> .ofiles-gettext-devel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-gettext-devel -f %{oreon_filedir}/ocaml-gettext-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-9
- Prepare for Oreon 11 (RP1)
