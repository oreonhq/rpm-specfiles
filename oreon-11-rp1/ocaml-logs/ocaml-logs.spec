%global source0_hash 760ec291c128d75b74826091337764f925b5ca414b02e2d336a0b37bf30df4ea
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-logs
Version:        0.10.0
Release:        1%{?dist}
Summary:        Logging infrastructure for OCaml
License:        ISC
URL:            https://erratique.ch/software/logs
VCS:            git:https://erratique.ch/repos/logs.git
Source0:        https://erratique.ch/software/logs/releases/logs-%{version}.tbz
ExcludeArch:    %{ix86}
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
# /oreon:deps
%description
Logs provides a logging infrastructure for OCaml.  Logging is performed on
sources whose reporting level can be set independently.  The log message
report is decoupled from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and the API
lets you easily implement your own.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir logs-%{version}
%oreon_prep
%build

ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --tests true \
  --with-js_of_ocaml-compiler false \
  --with-fmt true \
  --with-cmdliner true \
  --with-lwt true \
  --with-base-threads true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-logs-devel -f %{oreon_filedir}/ocaml-logs-devel.list

%changelog

%autochangelog
