%global source0_hash e32eb4c6f319ff74241da9e1b00032f990241347271baf3adb468faaaa616147

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is needed to build lwt, which is used to build ounit, but this
# package needs ounit to run its tests.  Break the dependency cycle here.
%bcond test 0

Name:           ocaml-re
Version:        1.14.0
Release:        3%{?dist}
Summary:        A regular expression library for OCaml

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/ocaml-re
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune

%if %{with test}
BuildRequires:  ocaml-ounit-devel
%endif

%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
