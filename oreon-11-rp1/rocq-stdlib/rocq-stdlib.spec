%global source0_hash 2d66421c52ed32719a15cb039c368e063c4d85f670e3d142f5eb7415fb427985

# This package is installed into an archful location, but contains no ELF
# objects.
%global debug_package %{nil}

# TESTING NOTE: The testsuite must be run as part of the rocq build.  See
# the rocq spec for details.

%global stdlibdir %{ocamldir}/coq/user-contrib/Stdlib
%global rocqver   9.1.1
%global giturl    https://github.com/rocq-prover/stdlib

Name:           rocq-stdlib
Version:        9.1.0
Release:        %autorelease
Summary:        The Rocq proof assistant standard library

License:        LGPL-2.1-only
URL:            https://rocq-prover.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/V%{version}/%{name}-%{version}.tar.gz

# Rocq's plugin architecture requires cmxs files.
ExclusiveArch:  %{ocaml_native_compiler}

BuildRequires:  coq-core-compat = %{rocqver}
BuildRequires:  rocq = %{rocqver}
BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-dune >= 3.6.1
BuildRequires:  ocaml-findlib

Requires:       rocq-core%{?_isa} = %{rocqver}

%global _desc %{expand:Rocq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems together
with an environment for semi-interactive development of machine-checked proofs.}

%description
%_desc

This package includes the Rocq Standard Library, that is to say, the set of
modules usually bound to the Stdlib.* namespace.

%package        source
Summary:        Source files of the Rocq proof assistant standard library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    source
%_desc

This package contains the source Rocq files for the standard library.  These
files are not needed to use the standard library.  They are made available for
informational purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n stdlib-%{version} -p1

%build
%dune_build -p rocq-stdlib

%install
%dune_install -n rocq-stdlib

%files -f .ofiles
%doc README.md CONTRIBUTING.md
%license LICENSE
%exclude %{stdlibdir}/*.v
%exclude %{stdlibdir}/*/*.v
%exclude %{stdlibdir}/*/*/*.v
%exclude %{stdlibdir}/*/*/*/*.v

%files source
%{stdlibdir}/*.v
%{stdlibdir}/*/*.v
%{stdlibdir}/*/*/*.v
%{stdlibdir}/*/*/*/*.v

%changelog
%autochangelog
