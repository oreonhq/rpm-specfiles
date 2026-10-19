%global source0_hash 7b9d7390fca822afd8b35197814616088edfb3fa3cb44903dfa49399e9fefb50
ExcludeArch: %{ix86}
%global giturl  https://gitlab.com/irill/cudf
Name:           ocaml-cudf
Version:        0.10
Release:        1%{?dist}
Summary:        Format for describing upgrade scenarios
License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://www.mancoosi.org/cudf/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/v%{version}/cudf-v%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ounit-devel
# /oreon:deps
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
%global oreon_srcdir cudf-v%{version}
%oreon_prep
%build

%dune_build
%make_build -C doc
%install
%dune_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/cudf-check.1* %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-cudf-devel -f %{oreon_filedir}/ocaml-cudf-devel.list

%changelog

%autochangelog
