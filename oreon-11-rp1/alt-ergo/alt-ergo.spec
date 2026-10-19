%global source0_hash 4c3dd68bb9e1edf18297d225138908b2ee5522358853007f97196d47c3c76c12
%global giturl  https://github.com/OCamlPro/alt-ergo
Name:		alt-ergo
Version:	2.6.4
Release:        1%{?dist}
Summary:        Automated theorem prover including linear arithmetic
License:	CECILL-C
URL:		https://alt-ergo.ocamlpro.com/
VCS:		git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}-free/%{name}-free-%{version}.tar.gz
Patch:		%{name}-forward-compat.patch
Patch:		%{name}-deprecation.patch
Patch:		%{name}-datadir.patch
Patch:		%{name}-inline-error.patch
Patch:		%{name}-cmdliner.patch
ExcludeArch:	%{ix86}
Obsoletes:	alt-ergo-gui < 2.4
Obsoletes:	ocaml-alt-ergo-lib < 2.4
Obsoletes:	ocaml-alt-ergo-lib-devel < 2.4
Obsoletes:	ocaml-alt-ergo-parsers < 2.4
Obsoletes:	ocaml-alt-ergo-parsers-devel < 2.4
Provides:	alt-ergo-gui = %{version}-%{release}
Provides:	ocaml-alt-ergo-lib = %{version}-%{release}
Provides:	ocaml-alt-ergo-lib-devel = %{version}-%{release}
Provides:	ocaml-alt-ergo-parsers = %{version}-%{release}
Provides:	ocaml-alt-ergo-parsers-devel = %{version}-%{release}
%global __requires_exclude ocaml\\\(AltErgoLib.*\\\)
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-build-info-devel
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocplib-simplex-devel
BuildRequires:  ocaml-psmt2-frontend-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-zip-devel
# /oreon:deps
%description
Alt-Ergo is an automated theorem prover implemented in OCaml.  It is based on
CC(X) - a congruence closure algorithm parameterized by an equational theory
X.  This algorithm is reminiscent of the Shostak algorithm.  Currently CC(X)
is instantiated by the theory of linear arithmetics.  Alt-Ergo also contains a
home made SAT-solver and an instantiation mechanism by which it fully supports
quantifiers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-free -p1

%conf
# Unzip an example
cd examples/AB-Why3-plugin
unzip p4_34.why.zip
rm p4_34.why.zip
cd -

%ifnarch %{ocaml_native_compiler}
# Do not require native plugins
sed -i '/cmxs/d' plugins/fm-simplex/dune
%endif

# This is not an autoconf-generated script.  Do NOT use %%configure.
./configure --prefix=%{_prefix} --libdir=%{ocamldir} --mandir=%{_mandir}

%build

%make_build
%install
%dune_install
chmod 0755 %{buildroot}%{_datadir}/%{name}-free/plugins/*.cmxs
mv %{buildroot}%{_datadir}/%{name}-free/{plugins,preludes} \
   %{buildroot}%{ocamldir}/%{name}-free
rmdir %{buildroot}%{_datadir}/%{name}-free
cat > %{buildroot}%{ocamldir}/%{name}-free/META << EOF
version = "%{version}"
description = "Automated theorem prover including linear arithmetic"
requires = ""
EOF
%oreon_autofiles main

%check

%dune_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
