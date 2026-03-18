# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Optionally disable camomile dep on RHEL.
%if !0%{?rhel}
%bcond_without camomile
%bcond_without tests
%else
%bcond_with    camomile
%bcond_with    tests
%endif

Name:           ocaml-gettext
Version:        0.5.0
Release:        9%{?dist}
Summary:        OCaml library for i18n

License:        LGPL-2.1-or-later with OCaml-LGPL-linking-exception
URL:            https://github.com/gildor478/ocaml-gettext
VCS:            git:%{url}.git

Source0:        %{url}/archive/v%{version}.tar.gz

# Fix to stop using dune-site
# https://github.com/gildor478/ocaml-gettext/issues/36
# https://github.com/gildor478/ocaml-gettext/pull/37
Patch:          https://github.com/gildor478/ocaml-gettext/pull/37.patch

# Fix for OCaml >= 5.4
# https://github.com/gildor478/ocaml-gettext/issues/40
# https://github.com/gildor478/ocaml-gettext/pull/41
Patch:          0001-xgettext-Fix-type-for-OCaml-5.4.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-fileutils-devel >= 0.6.6-1
BuildRequires:  ocaml-dune >= 1.11.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-cppo
# This was orphaned and dropped from Fedora back in 2023, but may be
# needed to run the tests.
# https://github.com/gildor478/ocaml-gettext/issues/35
#BuildRequires: ocaml-seq-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  libxml2
%if %{with tests}
BuildRequires:  ocaml-ounit-devel
%endif
%if %{with camomile}
BuildRequires:  ocaml-camomile-devel >= 0.8.6-3
BuildRequires:  ocaml-camomile-data
%endif

%if %{with camomile}
# ocaml-gettext program needs camomile data files
Requires:       ocaml-camomile-data
%endif


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


%if %{with tests}
%check
%dune_check
%endif


%files -f .ofiles-gettext
%license LICENSE.txt


%files devel -f .ofiles-gettext-devel
%doc README.md CHANGES.md THANKS TODO.md
%{_bindir}/ocaml-gettext
%{_bindir}/ocaml-xgettext
%{_mandir}/man1/ocaml-gettext.1*
%{_mandir}/man1/ocaml-xgettext.1*
%{_mandir}/man5/ocaml-gettext.5*


%if %{with camomile}
%files camomile -f .ofiles-gettext-camomile
%license LICENSE.txt


%files camomile-devel -f .ofiles-gettext-camomile-devel
%doc README.md
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-9
- Prepare for Oreon 11 (RP1)
