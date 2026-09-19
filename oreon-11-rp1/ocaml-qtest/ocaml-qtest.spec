%global source0_hash eb8f3949155f535c6e69b6a424a1df7a97794df8cab441b1bcd6330e63d09d3b

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-qtest
Version:        2.11.2
Release:        29%{?dist}
Summary:        Inline (Unit) Tests for OCaml

License:        GPL-3.0-or-later
URL:            https://github.com/vincent-hugot/qtest
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove references to the bytes library for OCaml 5.0 compatibility
Patch:          %{name}-ocaml5.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.1
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-qcheck-devel >= 0.14
BuildRequires:  asciidoc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  python3-pygments

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

# generate manpage
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/qtest \
    --output %{buildroot}/%{_mandir}/man1/qtest.1 \
    --name "Inline (Unit) Tests for OCaml" \
    --version-string %{version} \
    --no-info

# Build documentation
asciidoc README.adoc

%check
%dune_check

%files -f .ofiles
%doc README.html
%license LICENSE
%{_mandir}/man1/qtest.1*

%files devel -f .ofiles-devel
%doc README.html
%license LICENSE

%changelog
%autochangelog
