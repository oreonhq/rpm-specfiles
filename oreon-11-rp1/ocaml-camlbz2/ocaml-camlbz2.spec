%global source0_hash cd17a33f58d903f7e4c26493cdaccf042b3ee029252ad6963bd83d4f5263bed3

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://gitlab.com/irill/camlbz2

Name:           ocaml-camlbz2
Version:        0.8.0
Release:        10%{?dist}
Summary:        OCaml bindings for bzip2

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://irill.gitlab.io/camlbz2
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{version}/camlbz2-%{version}.tar.gz
# Unbundle the OCaml io.h header file
Patch:          %{name}-io-h.patch
# We do not need the stdlib-shims forward compatibility package
Patch:          %{name}-shims.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  pkgconfig(bzip2)

%description
This package contains OCaml bindings for bzip2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlbz2-%{version} -p1

%conf
# Fix the version number
sed -i 's/0\.7\.1/%{version}/' dune-project

# Make sure we don't use the bundled copy of io.h
rm src/io.h

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc BUGS ChangeLog README
%license COPYING LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
