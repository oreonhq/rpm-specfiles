%global source0_hash 091252258e3dd16320c3ce4ddb21bcd57efd9c8c2ebfb799ee6a543ed492d9fa

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global libname xmlm

Name:           ocaml-%{libname}
Version:        1.4.0
Release:        17%{?dist}
Summary:        A streaming XML codec

License:        ISC
URL:            https://erratique.ch/software/xmlm
VCS:            git:https://erratique.ch/repos/xmlm.git
Source0:        %{url}/releases/%{libname}-%{version}.tbz

# Example XML files for testing
Source1:        test-valid.xml
Source2:        test-invalid.xml

# Ensure source files are included in generated debuginfo subpackage
Patch0:         xmlm-1.4.0-debug.patch

BuildRequires:  ocaml >= 4.05.0
BUildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3

%description
Xmlm is an OCaml streaming codec to decode and encode the XML data
format. It can process XML documents without a complete in-memory
representation of the data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{libname}-%{version}

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

# Against valid XML
$RPM_BUILD_ROOT%{_bindir}/xmltrip -p %{SOURCE1} 2>valid-err.log
[ -z "$(cat valid-err.log)" ]

# Against invalid XML - stderr should contain the word expected
$RPM_BUILD_ROOT%{_bindir}/xmltrip -p %{SOURCE2} 2>invalid-err.log
grep expected invalid-err.log >/dev/null

%files -f .ofiles
%license LICENSE.md
%doc README.md

%files devel -f .ofiles-devel
%license LICENSE.md
%doc CHANGES.md _build/test/examples.ml _build/test/xhtml.ml doc

%changelog
%autochangelog
