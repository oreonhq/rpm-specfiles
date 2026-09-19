%global source0_hash 4b6a3085d682327269fe69ff0d7eb9a2f8532f41ee57a42f27f48b7fdc3b058c

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-zed
Version:        3.2.3
Release:        19%{?dist}
Summary:        Abstract engine for text editing in OCaml

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/zed
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/zed-%{version}.tar.gz
# We don't need the uchar forwards compatibility package
Patch0:         %{name}-uchar.patch

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-uucp-devel >= 2.0.0
BuildRequires:  ocaml-uuseg-devel
BuildRequires:  ocaml-uutf-devel

%description
Zed is an abstract engine for text editing.  It can be used to
write text editors, editing widgets, readlines, ...  You just
have to connect an engine to your inputs and rendering functions
to get an editor.

Zed provides: editing state management, multiple cursor support,
key-binding helpers, and general purpose unicode rope
manipulation functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-react-devel%{_isa}
Requires:       ocaml-result-devel%{_isa}
Requires:       ocaml-uucp-devel%{_isa}
Requires:       ocaml-uuseg-devel%{_isa}
Requires:       ocaml-uutf-devel%{_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n zed-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
