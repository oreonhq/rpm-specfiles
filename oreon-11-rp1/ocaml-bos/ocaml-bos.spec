%global source0_hash d8d62e786b10d697e0457205a8eedeaa27ebcc90f1855f18df190cac2e3d8f37

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-bos
Version:        0.2.1
Release:        33%{?dist}
Summary:        Basic OS interaction for OCaml

License:        ISC
URL:            https://erratique.ch/software/bos
VCS:            git:https://erratique.ch/repos/bos.git
Source:         %{url}/releases/bos-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel >= 0.8.10
BuildRequires:  ocaml-fpath-devel >= 0.7.3
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-rresult-devel >= 0.7.0
BuildRequires:  ocaml-topkg-devel >= 1.0.3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
Bos provides support for basic and robust interaction with the operating
system in OCaml.  It has functions to access the process environment, parse
command line arguments, interact with the file system and run command line
programs.  Bos works equally well on POSIX and Windows operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-rresult-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bos-%{version}

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%if %{with docs}
%doc _build/default/_doc/*
%endif

%changelog
%autochangelog
