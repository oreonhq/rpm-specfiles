# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-libvirt
Version:        0.6.1.7
Release:        19%{?dist}
Summary:        OCaml binding for libvirt
License:        LGPL-2.1-or-later

URL:            https://ocaml.libvirt.org/
Source0:        https://download.libvirt.org/ocaml/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-rpm-macros

BuildRequires:  libvirt-devel >= 0.2.1
BuildRequires:  perl-interpreter

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
OCaml binding for libvirt.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q
%autopatch -p1

# Fix detection of ocamlopt and ocamldoc
# https://gitlab.com/libvirt/libvirt-ocaml/-/merge_requests/27
sed -i '/AM_CONDITIONAL/s/"x"/"xno"/' configure.ac

# Regenerate the configure script
autoreconf -fi -I m4 .


%build
# Parallel builds do not work.
unset MAKEFLAGS
%configure
make


%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install
%ocaml_files


%files -f .ofiles
%doc README
%license COPYING.LIB


%files devel -f .ofiles-devel
%doc README TODO.libvirt
%license COPYING.LIB


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.1.7-19
- Prepare for Oreon 11 (RP1)
