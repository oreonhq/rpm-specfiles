%global source0_hash 7b9d7390fca822afd8b35197814616088edfb3fa3cb44903dfa49399e9fefb50

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# cudf includes C bindings, but it produces a static library.
# therefore for now, we'll not build them.

%global giturl  https://gitlab.com/irill/cudf

Name:           ocaml-cudf
Version:        0.10
Release:        17%{?dist}
Summary:        Format for describing upgrade scenarios

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://www.mancoosi.org/cudf/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/v%{version}/cudf-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ounit-devel

# Depend on pod2man.
BuildRequires:  /usr/bin/pod2man

%description
CUDF (for Common Upgradeability Description Format) is a format for
describing upgrade scenarios in package-based Free and Open Source
Software distribution.

In every such scenario there exists a package universe (i.e. a set
of packages) known to a package manager application, a package status
(i.e. the currently installed packages), and a user request (i.e. a
wish to change the set of installed packages) that need to be
fulfilled.

CUDF permits to describe an upgrade scenario in a way that is
both distribution-independent and package-manager-independent.

CUDF offers a rigorous semantics of dependency solving that
enables to independently check the correctness of upgrade
solutions proposed by package managers.

CUDF adoption would enable to share dependency solver components
across different package managers, both intra- and
inter-distributions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-extlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cudf-v%{version}

%build
%dune_build
%make_build -C doc

%install
%dune_install

# Install the man page for cudf-check.
mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/cudf-check.1* %{buildroot}%{_mandir}/man1

%check
%dune_check

%files -f .ofiles
%license COPYING
%doc README
%{_mandir}/man1/cudf-check.1*

%files devel -f .ofiles-devel
%license COPYING

%changelog
%autochangelog
