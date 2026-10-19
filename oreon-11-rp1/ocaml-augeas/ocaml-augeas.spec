%global source1_hash bbc1f9b637164843610ef3254693b2f4373d005931a5430cbcb463ad38f12309
%global source0_hash ee3899c85d5b22cdcc659183e571add0980725a8a705a9fe7bf53ddc2ba2dd63
%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0
ExcludeArch: %{ix86}
Name:           ocaml-augeas
Version:        0.7
Release:        1%{?dist}
Summary:        OCaml bindings for Augeas configuration API
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://people.redhat.com/~rjones/augeas/
Source0:        https://download.libguestfs.org/ocaml-augeas/ocaml-augeas-%{version}.tar.gz
Source1:        https://download.libguestfs.org/ocaml-augeas/ocaml-augeas-%{version}.tar.gz.sig
Source2:        libguestfs.keyring
# oreon:deps
BuildRequires:  augeas-devel
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Pass -g to ocamlmklib
sed -i 's/ocamlmklib/& -g/' Makefile.in

%build

%configure
%ifarch %{ocaml_native_compiler}
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
%ifarch %{ocaml_native_compiler}
ocamlfind install augeas META *.mli *.cmx *.cma *.cmxa *.a augeas.cmi *.so
%else
ocamlfind install augeas META *.mli *.cma *.a augeas.cmi *.so
%endif
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-augeas-devel -f %{oreon_filedir}/ocaml-augeas-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7-6
- Prepare for Oreon 11 (RP1)
