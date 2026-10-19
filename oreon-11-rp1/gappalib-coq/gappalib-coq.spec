%global source0_hash decca33f02a7180d4222e9816027245b199851e73c37a859a5861b4676dffa06
%global gappadir %{ocamldir}/coq/user-contrib/Gappa
%global rocqver 9.1.1
%global commit  20d239160d980d452f39f06e0f428ffb0e8e4dd4
%global giturl  https://gitlab.inria.fr/gappa/coq
Name:           gappalib-coq
Version:        1.11.0
Release:        1%{?dist}
Summary:        Coq support library for gappa
License:        LGPL-3.0-or-later
URL:            https://gappa.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ocaml_native_compiler}
Requires:       rocq%{?_isa} = %{rocqver}
Requires:       flocq
Requires:       gappa
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coq-core-compat
BuildRequires:  flocq
BuildRequires:  gappa
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-zarith-devel
BuildRequires:  remake
BuildRequires:  rocq
# /oreon:deps
%description
This support library provides vernacular files so that the certificates
Gappa generates can be imported by the Coq proof assistant.  It also
provides a "gappa" tactic that calls Gappa on the current Coq goal.

Gappa (Génération Automatique de Preuves de Propriétés Arithmétiques --
automatic proof generation of arithmetic properties) is a tool intended
to help verifying and formally proving properties on numerical programs
dealing with floating-point or fixed-point arithmetic.

%package source
Summary:        Source Coq files
Requires:       %{name} = %{version}-%{release}
%description source
This package contains the source Coq files for gappalib-coq.  These
files are not needed to use gappalib-coq.  They are made available for
informational purposes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n coq-%{name}-%{version}-%{commit}

%conf
# Enable debuginfo
sed -i 's/-rectypes/-g &/' Remakefile.in

# Generate the configure script
autoconf -f

%build

./configure --prefix=%{_prefix} --datadir=%{_datadir}
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{gappadir}
DESTDIR=%{buildroot} remake install
cp -p src/*.v  %{buildroot}%{gappadir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

remake check
%files -f %{oreon_filedir}/main.list
%files -n gappalib-coq-source -f %{oreon_filedir}/gappalib-coq-source.list

%changelog

%autochangelog
