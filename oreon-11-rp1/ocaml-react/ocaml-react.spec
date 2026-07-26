%global source0_hash c4add315d6f1f153d115ee7ca8dd60c1265ff4d408c266125fcb5124fd228f99

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-react
Version:        1.2.2
Release:        18%{?dist}
Summary:        OCaml framework for Functional Reactive Programming (FRP)

License:        ISC
URL:            https://erratique.ch/software/react
VCS:            git:https://erratique.ch/repos/react.git

Source0:        https://erratique.ch/software/react/releases/react-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
React is an OCaml module for functional reactive programming (FRP). It
provides support to program with time varying values : declarative
events and signals. React doesn't define any primitive event or
signal; it lets the client choose the concrete timeline.

React is made of a single, independent module and distributed under
the ISC license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n react-%{version}

# require debug info
echo $'\ntrue: debug' >> _tags

# expose a math library dependency to RPM
echo $'\ntrue: cclib(-lm)' >> _tags

%build
ocaml pkg/pkg.ml build --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel
%doc CHANGES.md README.md

%changelog
%autochangelog
