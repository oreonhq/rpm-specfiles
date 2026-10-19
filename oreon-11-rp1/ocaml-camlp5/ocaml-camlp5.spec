%global source0_hash eb8c5bc0f47ce4b9518d37bcbf8be05ee80243c38e7019f8c3808456be8f15a8
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/camlp5/camlp5
Name:           ocaml-camlp5
Version:        8.04.00
Release:        4%{?dist}
Summary:        Preprocessor and pretty printer for OCaml
License:        BSD-3-Clause
URL:            https://camlp5.github.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/camlp5-%{version}.tar.gz
Patch0:         camlp5-8.00-kill-warn-error.patch
%global __ocaml_provides_opts -i Dynlink -i Dynlink_common -i Dynlink_config -i Dynlink_platform_intf -i Dynlink_symtable -i Dynlink_types
%global __ocaml_requires_opts -i Dynlink_cmo_format -i MLast
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-camlp5-buildscripts
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-pcre2-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-rresult-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(String::ShellQuote)
# /oreon:deps
%description
Camlp5 is a preprocessor-pretty-printer of OCaml.

It is compatible with all versions of OCaml from 4.05.0 thru 4.14.0.
Previous versions of Camlp5 have supported OCaml versions down to 1.07
and jocaml 3.12.0 to 3.12.1, but this version cuts off support at
4.10.0.  Camlp5 is heavily tested with OCaml versions from 4.10.0
forward, with an extensive and ever-growing testsuite.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlp5-%{version} -p1
find . -name .gitignore -delete

# Avoid obsolescence warning
sed -i 's/egrep/grep -E/' configure

%build

./configure \
    --prefix %{_prefix} \
    --bindir %{_bindir} \
    --libdir %{_libdir}/ocaml \
    --mandir %{_mandir}
%ifarch %{ocaml_native_compiler}
%make_build DEBUG=-g
%else
%make_build world DEBUG=-g
%endif
%install
%make_install
%ocaml_files
sed -i '\@%{_bindir}@d;\@%{_mandir}@d' .ofiles
%ifarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C testsuite all-tests
make -C test all
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-camlp5-devel -f %{oreon_filedir}/ocaml-camlp5-devel.list

%changelog

%autochangelog
