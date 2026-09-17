%global source0_hash eb8c5bc0f47ce4b9518d37bcbf8be05ee80243c38e7019f8c3808456be8f15a8

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
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

# Kill -warn-error A
Patch0:         camlp5-8.00-kill-warn-error.patch

BuildRequires:  diffutils
BuildRequires:  make
BuildRequires:  ocaml >= 4.10
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-camlp-streams-devel >= 5.0
BuildRequires:  ocaml-camlp5-buildscripts >= 0.06
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-pcre2-devel >= 8.0.3
BuildRequires:  ocaml-re-devel >= 1.11.0
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-rresult-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(String::ShellQuote)

BuildRequires:  ocaml-ocamldoc

# Do not provide symbols already provided by the OCaml compiler
%global __ocaml_provides_opts -i Dynlink -i Dynlink_common -i Dynlink_config -i Dynlink_platform_intf -i Dynlink_symtable -i Dynlink_types
# Do not require symbols that we don't provide
%global __ocaml_requires_opts -i Dynlink_cmo_format -i MLast

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
# Upstream uses hand-written configure, grrrrrr.
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
# The testsuite relies on ocamlopt
%check
make -C testsuite all-tests
make -C test all
%endif

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel
%doc CHANGES ICHANGES DEVEL UPGRADING doc/html doc/htmlp
%{_bindir}/camlp5*
%{_bindir}/mkcamlp5*
%{_bindir}/ocpp5
%{_mandir}/man1/*.1*

%changelog
%autochangelog
