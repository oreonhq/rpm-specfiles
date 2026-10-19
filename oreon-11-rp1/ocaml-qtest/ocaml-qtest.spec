%global source0_hash eb8f3949155f535c6e69b6a424a1df7a97794df8cab441b1bcd6330e63d09d3b
ExcludeArch: %{ix86}
Name:           ocaml-qtest
Version:        2.11.2
Release:        29%{?dist}
Summary:        Inline (Unit) Tests for OCaml
License:        GPL-3.0-or-later
URL:            https://github.com/vincent-hugot/qtest
VCS:            git:%{url}.git
Source0:        https://github.com/vincent-hugot/qtest/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-ocaml5.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  python3-pygments
# /oreon:deps
%description
qtest extracts inline unit tests written using a special syntax in comments.
Those tests are then run using the oUnit framework and the qcheck library.
The possibilities range from trivial tests — extremely simple to use — to
sophisticated random generation of test cases.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qtest-%{version} -p1

# Fix a markup bug in the README
sed -i 's/\[source\]/[source,OCaml]/' README.adoc

%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/qtest \
    --output %{buildroot}/%{_mandir}/man1/qtest.1 \
    --name "Inline (Unit) Tests for OCaml" \
    --version-string %{version} \
    --no-info
asciidoc README.adoc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-qtest-devel -f %{oreon_filedir}/ocaml-qtest-devel.list

%changelog

%autochangelog
