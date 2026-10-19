%global source0_hash 0e024711f33fb4cefc3670da014d21395ab83985423bb5850082412e583341cd
ExcludeArch: %{ix86}
Name:           ocaml-libvirt
Version:        0.6.1.7
Release:        19%{?dist}
Summary:        OCaml binding for libvirt
License:        LGPL-2.1-or-later
URL:            https://ocaml.libvirt.org/
Source0:        https://download.libvirt.org/ocaml/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libvirt-devel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  perl-interpreter
# /oreon:deps
%description
OCaml binding for libvirt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%autopatch -p1

# Fix detection of ocamlopt and ocamldoc
# https://gitlab.com/libvirt/libvirt-ocaml/-/merge_requests/27
sed -i '/AM_CONDITIONAL/s/"x"/"xno"/' configure.ac

# Regenerate the configure script
autoreconf -fi -I m4 .

%build

unset MAKEFLAGS
%configure
make
%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-libvirt-devel -f %{oreon_filedir}/ocaml-libvirt-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.1.7-19
- Prepare for Oreon 11 (RP1)
