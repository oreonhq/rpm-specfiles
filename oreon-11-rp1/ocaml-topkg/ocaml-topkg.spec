%global source0_hash 20da062dc9cea21b5c728f22c986ed3e3d57310e643260160a802d559712f6fc
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond care 0
Name:           ocaml-topkg
Version:        1.1.1
Release:        1%{?dist}
Summary:        The transitory OCaml software packager
License:        ISC
URL:            https://erratique.ch/software/topkg/
VCS:            git:https://erratique.ch/repos/topkg.git
Source0:        https://erratique.ch/software/topkg/releases/topkg-%{version}.tbz
ExcludeArch:    %{ix86}
%if %{with care}
%endif
%global _desc %{expand:Topkg is a packager for distributing OCaml software.  It provides an API to
describe the files a package installs in a given build configuration and to
specify information about the package's distribution, creation and publication
procedures.}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
%_desc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%if %{with care}
%package        care
Summary:        Command line tool for the transitory OCaml software packager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocamlbuild%{?_isa}
%description    care
%_desc

This package provides a command line tool which helps with various aspects of
a package's life cycle: creating and linting a distribution, releasing it on
the web, publishing its documentation, adding it to the OCaml opam repository,
etc.

%package        care-devel
Summary:        Development files for %{name}-care
Requires:       %{name}-care%{?_isa} = %{version}-%{release}
Requires:       ocaml-bos-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-opam-format-devel%{?_isa}
Requires:       ocaml-webbrowser-devel%{?_isa}
%description    care-devel
The %{name}-care-devel package contains libraries and signature files for
developing applications that use %{name}-care.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n topkg-%{version} -p1

%conf
# This package can replace "watermarks" in software that it builds.  However,
# we are building from scratch, rather than using topkg to build itself, so we
# have to do the job manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%PKG_DOC%%%%,%{url}doc/,' \
      -e 's,%%%%PKG_HOMEPAGE%%%%,%{url},' \
      -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build

ocaml pkg/pkg.ml build --pkg-name topkg --dev-pkg false --tests true
%if %{with care}
ocaml pkg/pkg.ml build --pkg-name topkg-care --dev-pkg false --tests true
%endif
%install
%ocaml_install -s
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with care}
%check

ocaml pkg/pkg.ml test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-topkg-devel -f %{oreon_filedir}/ocaml-topkg-devel.list

%changelog

%autochangelog
