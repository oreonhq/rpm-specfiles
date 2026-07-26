%global source0_hash 03bf4bae6908a947582485c2a0b8f96428f39f97efd540573a613632be56ad2a

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocsigen/lwt

Name:           ocaml-lwt
Version:        5.9.1
Release:        4%{?dist}
Summary:        OCaml lightweight thread library

# The project as a whole is MIT.  The following files are BSD-2-Clause:
# - src/core/lwt_condition.ml
# - src/core/lwt_condition.mli
# - src/core/lwt_mvar.ml
# - src/core/lwt_mvar.mli
License:        MIT AND BSD-2-Clause
URL:            https://ocsigen.org/lwt
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/lwt-%{version}.tar.gz
# Expose a dependency on the math library so rpm can see it
Patch:          %{name}-mathlib.patch
# Compatibility with ppxlib 0.36
# https://github.com/ocsigen/lwt/pull/1033
Patch:          %{name}-ppxlib-0.36.patch

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-ocplib-endian-devel

# lwt_react dependencies.
BuildRequires:  ocaml-react-devel >= 1.0.0

# lwt_ppx dependencies.
BuildRequires:  ocaml-ppxlib-devel >= 0.16.0
BuildRequires:  ocaml-ppx-let-devel

# optional dependencies.
BuildRequires:  libev-devel

# This can be removed when F43 reaches EOL
Obsoletes:      ocaml-lwt-luv < 5.7.0

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocplib-endian-devel%{?_isa}
Requires:       libev-devel%{?_isa}

# This can be removed when F43 reaches EOL
Obsoletes:      ocaml-lwt-luv-devel < 5.7.0

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        react
Summary:        Helpers for using React with Lwt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    react
Helpers for using React with Lwt.

%package        react-devel
Summary:        Development files for ocaml-lwt-react

Requires:       %{name}-react%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-react-devel%{?_isa}

%description    react-devel
The %{name}-react-devel package contains libraries and signature files for
developing applications that use %{name}-react.

%package        ppx
Summary:        PPX syntax for Lwt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ppx
PPX syntax for Lwt, providing something similar to async/await from JavaScript.

%package        ppx-devel
Summary:        Development files for ocaml-lwt-ppx

Requires:       %{name}-ppx%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    ppx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-ppx.

%package        retry
Summary:        Utilities for retrying Lwt computations
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    retry
Utilities for retrying Lwt computations.

%package        retry-devel
Summary:        Development files for ocaml-lwt-retry

Requires:       %{name}-retry%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    retry-devel
The %{name}-retry-devel package contains libraries and signature files for
developing applications that use %{name}-retry.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lwt-%{version} -p1

# It looks like one test fails.
# Actually, it looks like all the "mcast" tests fail in koji.
# They should probably be disabled via a patch, but this works for now.
sed 's,test_mcast "mcast-join-loop" true true;,(*test_mcast "mcast-join-loop" true true;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-join-noloop" true false;,(*test_mcast "mcast-join-noloop" true false;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-nojoin-loop" false true;,(*test_mcast "mcast-nojoin-loop" false true;*),' -i test/unix/test_mcast.ml
sed 's,test_mcast "mcast-nojoin-noloop" false false;,(*test_mcast "mcast-nojoin-noloop" false false;*),' -i test/unix/test_mcast.ml

%build
# Enable libev and pthread.
dune exec src/unix/config/discover.exe -- --save \
     --use-libev true --use-pthread true
%dune_build

%install
%dune_install -s

# Remove test-only directory
rm -rf %{buildroot}%{ocamldir}/lwt_ppx_let

%check
# Disable this test on s390x.
# https://bugzilla.redhat.com/show_bug.cgi?id=1826511
%ifnarch s390x
%dune_check
%endif

%files -f .ofiles-lwt
%doc CHANGES README.md
%license LICENSE.md

%files devel -f .ofiles-lwt-devel
%doc CHANGES README.md
%license LICENSE.md

%files react -f .ofiles-lwt_react
%doc CHANGES README.md
%license LICENSE.md

%files react-devel -f .ofiles-lwt_react-devel
%doc CHANGES README.md

%files ppx -f .ofiles-lwt_ppx
%doc CHANGES README.md

%files ppx-devel -f .ofiles-lwt_ppx-devel
%doc CHANGES README.md

%files retry -f .ofiles-lwt_retry
%doc CHANGES README.md

%files retry-devel -f .ofiles-lwt_retry-devel
%doc CHANGES README.md

%changelog
%autochangelog
