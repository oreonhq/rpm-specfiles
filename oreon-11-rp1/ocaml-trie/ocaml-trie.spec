%global source0_hash c2f8054ea44216e6a3a961b28f7630e0e3dbfbd1b504ae741be230cbe32498ea

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-trie
Version:        1.0.0
Release:        33%{?dist}
Summary:        Strict impure trie tree

License:        MIT
URL:            https://github.com/kandu/trie
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/trie-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune >= 1.0

%description
This package contains an implementation of a strict impure trie tree.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n trie-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
