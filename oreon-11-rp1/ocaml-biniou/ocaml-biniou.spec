%global source0_hash 8bf3ff17cd0ecb2d6b6d1d94cb08ef089d44caef96e9bae6be6839d428fa318f

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-biniou
Version:        1.2.2
Release:        17%{?dist}
Summary:        Safe and fast binary data format

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/biniou
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/biniou-%{version}.tbz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-dune

%description
Biniou (pronounced "be new") is a binary data format designed for
speed, safety, ease of use and backward compatibility as protocols
evolve. Biniou is vastly equivalent to JSON in terms of functionality
but allows implementations several times faster (4 times faster than
yojson), with 25-35%% space savings.

Biniou data can be decoded into human-readable form without knowledge
of type definitions except for field and variant names which are
represented by 31-bit hashes. A program named bdump is provided for
routine visualization of biniou data files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-easy-format-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n biniou-%{version}

%build
%dune_build

%install
%dune_install

%ifarch %{ocaml_native_compiler}
# avoid potential future name conflict
mv $RPM_BUILD_ROOT%{_bindir}/{,ocaml-}bdump
sed -i '/bdump/d' .ofiles
%endif

%check
# Upstream doesn't know how to build the tests without ocamlopt, so:
%ifarch %{ocaml_native_compiler}
%dune_check
%endif

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel
%license LICENSE
%doc biniou-format.txt CHANGES.md
%doc _build/install/default/doc/*
%ifarch %{ocaml_native_compiler}
%{_bindir}/ocaml-bdump
%endif

%changelog
%autochangelog
