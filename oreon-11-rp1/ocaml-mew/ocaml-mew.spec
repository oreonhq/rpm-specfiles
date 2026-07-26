%global source0_hash 64d38ceb52ef574cb314bdd693f7e4a9c9e483e80a58595db22f2df76a8a59e6

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-mew
Version:        0.1.0
Release:        34%{?dist}
Summary:        Modal Editing Witch

License:        MIT
URL:            https://github.com/kandu/mew
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/mew-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch:          %{name}-mathlib.patch

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 1.1.0
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-trie-devel >= 1.0.0

%description
This is the core module of mew, a general modal editing engine generator.  You
can provide `Key`, `Mode`, and `Concurrent` modules to define the real world
environment to get the core component of a modal editing engine.  The core
component supports recursive key mappings associated with user provided modes.
After the core component is generated, you may extended it with a translator
to interpret user key sequences to get a complete modal editing engine.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-trie-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mew-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
