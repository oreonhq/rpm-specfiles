%global source0_hash 8e36013b257e946542810bd66fad815b2c941903ceaafdea9a060b388bd38797

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Uncomment this for bugfix releases
#%%global bugfix bugfix2

%global giturl  https://github.com/thvnx/mlmpfr

Name:           ocaml-mlmpfr
Version:        4.2.1
Release:        12%{?dist}%{?bugfix:.%{bugfix}}
Summary:        OCaml bindings for MPFR

# FIXME: the individual files say LGPL-3.0-or-later, but opam says this:
License:        LGPL-3.0-only
URL:            https://thvnx.github.io/mlmpfr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/mlmpfr.%{version}.tar.gz
# Fix a build failure with OCaml 5.3.0
Patch:          %{name}-internals.patch
# Adapt the tests to dune 3.17.0
# https://github.com/thvnx/mlmpfr/commit/1e0c151ec39898dcb12d5b2cdc8184e7669f02a3
Patch:          %{name}-dune.patch

BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-dune >= 2.9
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(mpfr)

%description
This library provides OCaml bindings for MPFR.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mpfr-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mlmpfr-mlmpfr.%{version} -p1

%build
# Make sure this version is compatible with our mpfr version
cd utils
gcc %{build_cflags} %{build_ldflags} mlmpfr_compatibility_test.c \
    -o mlmpfr_compatibility_test -lmpfr
./mlmpfr_compatibility_test
cd -

# Build the binary artifacts and documentation
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
