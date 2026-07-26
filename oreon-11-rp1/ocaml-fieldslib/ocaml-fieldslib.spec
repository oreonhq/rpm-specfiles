%global source0_hash 3d6001f7355d2dfb0f33fb7e64f39e34bda0917277609f5ec9a0703aa17b7dfa

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
# The only source file for this package consists of a single "include" line.
# It exports some private functions from the library in ocaml-base.  Although
# debuginfo is generated, it is tagged with the file names from ocaml-base,
# rather than the single 1-line source file in this project.  That leads to
# this error:
#
# error: Empty %%files file /builddir/build/BUILD/fieldslib-0.13.0/debugsourcefiles.list
#
# Do not try to gather debug sources to workaround the problem.
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-fieldslib
Version:        0.17.0
Release:        %autorelease
Summary:        OCaml record fields as first class values

License:        MIT
URL:            https://github.com/janestreet/fieldslib
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/fieldslib-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0

%description
This package contains an OCaml syntax extension to define first class values
representing record fields, to get and set record fields, iterate and fold
over all fields of a record and create new record values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fieldslib-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
