%global source0_hash fc85d6e46c4eb9370de9385f7bbfa6d57b4e48a9e96b20009007226b73f9530c

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-time-now
Version:        0.17.0
Release:        %autorelease
Summary:        Get the current time in OCaml

License:        MIT
URL:            https://github.com/janestreet/time_now
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/time_now-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-jane-street-headers-devel >= 0.17
BuildRequires:  ocaml-jst-config-devel >= 0.17
BuildRequires:  ocaml-ppx-base-devel >= 0.17
BuildRequires:  ocaml-ppx-optcomp-devel >= 0.17

%description
This package provides a single OCaml function to report the current time in
nanoseconds since the start of the Unix epoch.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-jane-street-headers-devel
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n time_now-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
