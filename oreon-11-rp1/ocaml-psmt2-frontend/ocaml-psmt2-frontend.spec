%global source0_hash 06eff884b629ce30704d08fb4559e54812e8c234e6086da770ea693613fe9780

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ACoquereau/psmt2-frontend

Name:           ocaml-psmt2-frontend
Version:        0.4.0
Release:        29%{?dist}
Summary:        Parser and typechecker for an extension of SMT-LIB 2

License:        Apache-2.0
URL:            https://acoquereau.github.io/psmt2-frontend/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/psmt2-frontend-%{version}.tar.gz
# Update conf.py for Sphinx 6.x
# https://github.com/ACoquereau/psmt2-frontend/pull/24
Patch:          %{name}-sphinx6.patch

BuildRequires:  make
BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-dune >= 2.6.0
BuildRequires:  ocaml-menhir >= 20180528
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%description
This package contains a library to parse and typecheck a conservative
extension of the SMT-LIB 2 standard with prenex polymorphism.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}

%description    docs
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n psmt2-frontend-%{version} -p1

%conf
# Do not use git to find the version; we don't have a git checkout
sed -i '/^git =/d;/^branch=/d;s/^\(version = \).*/\1"%{version}"/' sphinx/conf.py

%build
%dune_build
make sphinx

%install
%dune_install

# Put something interesting into the binary package META file
cat > %{buildroot}%{ocamldir}/psmt2-frontend_bin/META << EOF
version = "%{version}"
description = "PSMT2 command line tool"
requires = ""
EOF

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%files docs
%doc docs/sphinx

%changelog
%autochangelog
