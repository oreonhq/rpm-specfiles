# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-augeas
Version:        0.7
Release:        6%{?dist}
Summary:        OCaml bindings for Augeas configuration API
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://people.redhat.com/~rjones/augeas/
Source0:        https://download.libguestfs.org/ocaml-augeas/ocaml-augeas-%{version}.tar.gz
Source1:        https://download.libguestfs.org/ocaml-augeas/ocaml-augeas-%{version}.tar.gz.sig
Source2:        libguestfs.keyring
# oreon url source checksums begin
%global source0_sha256 ee3899c85d5b22cdcc659183e571add0980725a8a705a9fe7bf53ddc2ba2dd63
%global source0_file ocaml-augeas-0.7.tar.gz
# oreon url source checksums end

BuildRequires:  make
BuildRequires:  ocaml >= 3.09.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  augeas-devel >= 0.1.0
BuildRequires: gnupg2


%description
Augeas is a unified system for editing arbitrary configuration
files. This provides complete OCaml bindings for Augeas.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ocaml-augeas-0.7.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ee3899c85d5b22cdcc659183e571add0980725a8a705a9fe7bf53ddc2ba2dd63" || { echo "oreon: Source0 SHA256 mismatch for ocaml-augeas-0.7.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Pass -g to ocamlmklib
sed -i 's/ocamlmklib/& -g/' Makefile.in


%build
%configure
%ifarch %{ocaml_native_compiler}
# _smp_mflags breaks the build.
make
%else
make mlaugeas.cma test_augeas
%endif
make doc


%check
make check


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

# The upstream 'make install' rule is missing '*.so' and distributes
# '*.cmi' instead of just the augeas.cmi file.  Temporary fix:
#make install
%ifarch %{ocaml_native_compiler}
ocamlfind install augeas META *.mli *.cmx *.cma *.cmxa *.a augeas.cmi *.so
%else
ocamlfind install augeas META *.mli *.cma *.a augeas.cmi *.so
%endif

%ocaml_files


%files -f .ofiles
%license COPYING.LIB


%files devel -f .ofiles-devel
%doc html


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7-6
- Prepare for Oreon 11 (RP1)
