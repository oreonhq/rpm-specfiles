%global source0_hash f9210a07c4a3eb1756a45fa8a32974d9b5ddad3583c3400442fdfe2c9d63d636
ExcludeArch: %{ix86}
Name:           ocaml-mtime
Version:        2.2.0
Release:        1%{?dist}
Summary:        Monotonic wall-clock time for OCaml
License:        ISC
URL:            https://erratique.ch/software/mtime
VCS:            git:https://erratique.ch/repos/mtime.git
Source0:        https://erratique.ch/software/mtime/releases/mtime-%{version}.tbz
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
# /oreon:deps
%description
Mtime has platform independent support for monotonic wall-clock time in pure
OCaml.  This time increases monotonically and is not subject to operating
system calendar time adjustments.  The library has types to represent
nanosecond precision timestamps and time spans.

The additional Mtime_clock library provide access to a system monotonic clock.

Mtime has no dependencies.  Mtime_clock depends on your system library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mtime-%{version}

# link with the math library
echo $'\ntrue: cclib(-lm)' >> _tags

%build

ocaml pkg/pkg.ml build --dev-pkg false --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mtime-devel -f %{oreon_filedir}/ocaml-mtime-devel.list

%changelog

%autochangelog
