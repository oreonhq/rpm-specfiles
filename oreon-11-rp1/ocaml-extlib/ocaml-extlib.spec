# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-extlib
Version:        1.8.0
Release:        7%{?dist}
Summary:        OCaml ExtLib additions to the standard library
License:        LGPL-2.1-or-later with OCaml-LGPL-linking-exception

URL:            https://github.com/ygrek/ocaml-extlib
VCS:            git:%{url}.git
Source0:        https://github.com/ygrek/ocaml-extlib/releases/download/1.8.0/extlib-1.8.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 964277f001280a8eddfc08e0701d59ca0c6bdc5d052313b3e40e5088f6d45d70
%global source0_file extlib-1.8.0.tar.gz
# oreon url source checksums end

BuildRequires:  make
BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-findlib
# In order to apply patches:
BuildRequires:  git-core


%description
ExtLib is a project aiming at providing a complete - yet small -
standard library for the OCaml programming language. The purpose of
this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances
or more safety (tail-recursive) but also to provide new modules which
should be useful for the average OCaml programmer.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/extlib-1.8.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "964277f001280a8eddfc08e0701d59ca0c6bdc5d052313b3e40e5088f6d45d70" || { echo "oreon: Source0 SHA256 mismatch for extlib-1.8.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git -n extlib-%{version}

# Remove references to the bytes library for OCaml 5.0
sed -i '/bytes/d' src/META


%build
# https://bugzilla.redhat.com/show_bug.cgi?id=1837823
export minimal=1
%ifarch %{ocaml_native_compiler}
%make_build
%else
%make_build -C src all
%endif


%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

export minimal=1
%make_install
%ocaml_files


%check
export minimal=1
%ifarch %{ocaml_native_compiler}
make test
%else
make -C test all run
%endif


%files -f .ofiles
%doc README.md
%license LICENSE


%files devel -f .ofiles-devel


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.0-7
- Prepare for Oreon 11 (RP1)
