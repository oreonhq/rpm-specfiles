%global source0_hash 8c41de5a3d7d24c94dd58e8bf780cf9139541c3b978269a4340ca6b34070647d
%global debug_package %{nil}
%global flocqdir %{ocamldir}/coq/user-contrib/Flocq
%global rocqver 9.1.1
%global commit  7aab8f55bceec0cfafc3b3bc0e77e0dbb5a70c5f
%global giturl  https://gitlab.inria.fr/flocq/flocq
Name:           flocq
Version:        4.2.2
Release:        1%{?dist}
Summary:        Formalization of floating point numbers for Coq
License:        LGPL-3.0-or-later
URL:            https://flocq.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ocaml_native_compiler}
Requires:       rocq%{?_isa} = %{rocqver}
Requires:       rocq-stdlib%{?_isa}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coq-core-compat
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  remake
BuildRequires:  rocq
BuildRequires:  rocq-stdlib
# /oreon:deps
%description
Flocq (Floats for Rocq) is a floating-point formalization for the Rocq system.
It provides a comprehensive library of theorems on a multi-radix
multi-precision arithmetic.  It also supports efficient numerical computations
inside Rocq.

%package source
Summary:        Source Rocq files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description source
This package contains the source Rocq files for flocq.  These files are not
needed to use flocq.  They are made available for informational purposes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}-%{commit}

%conf
# Point to the local coqdoc files
sed -i 's,\(--coqlib \)[^[:blank:]]*,\1%{ocamldir}/coq,' Remakefile.in

# Generate the configure script
autoconf -f

%build

./configure
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags} all doc
%install
sed -i 's,%{_libdir},%{buildroot}%{_libdir},' Remakefile
remake install
cp -p src/*.v %{buildroot}%{flocqdir}
cp -p src/Calc/*.v %{buildroot}%{flocqdir}/Calc
cp -p src/Core/*.v %{buildroot}%{flocqdir}/Core
cp -p src/IEEE754/*.v %{buildroot}%{flocqdir}/IEEE754
cp -p src/Pff/*.v %{buildroot}%{flocqdir}/Pff
cp -p src/Prop/*.v %{buildroot}%{flocqdir}/Prop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n flocq-source -f %{oreon_filedir}/flocq-source.list

%changelog

%autochangelog
