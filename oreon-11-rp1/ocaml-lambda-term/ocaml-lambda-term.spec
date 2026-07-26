%global source0_hash 2d44f56d23db7ac56192f0e4f8b7b5c3d46d6c7e32e82cd112921c2fffeb5549

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-lambda-term
Version:        3.3.2
Release:        22%{?dist}
Summary:        Terminal manipulation library for OCaml

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/lambda-term
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/lambda-term-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel >= 4.2.0
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-mew-vi-devel >= 0.5.0
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-zed-devel >= 3.2.0

%description
Lambda-term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

The main objective of lambda-term is to provide a higher level functional
interface to terminal manipulation than, for example, ncurses, by providing
a native OCaml interface instead of bindings to a C library.

Lambda-term integrates with zed to provide text editing facilities in
console applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-lwt-react-devel%{?_isa}
Requires:       ocaml-mew-vi-devel%{?_isa}
Requires:       ocaml-uucp-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lambda-term-%{version}

%build
%dune_build

%install
%dune_install

mkdir -p %{buildroot}%{_datadir}/lambda-term
mv %{buildroot}%{_datadir}/lambda-term{rc,-inputrc} %{buildroot}%{_datadir}/lambda-term
sed -e 's,%{_datadir}/lambda-termrc,%{_datadir}/lambda-term,' \
    -e '\,%{_datadir}/lambda-term-inputrc,d' \
    -i .ofiles

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc CHANGES.md README.md

%files devel -f .ofiles-devel
%license LICENSE

%changelog
%autochangelog
