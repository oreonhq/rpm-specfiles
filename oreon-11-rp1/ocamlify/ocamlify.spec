%global source0_hash f7d9fec478714d174cb00e3298daa8b64ac03b704f6b671943914a163116c2c5

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocamlify
Version:        0.1.0
Release:        5%{?dist}
Summary:        Include files in OCaml code

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/gildor478/ocamlify
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  help2man

%description
OCamlify allows to create OCaml source code by including whole files into
OCaml string or string list. The code generated can be compiled as a standard
OCaml file. It allows embedding external resources as OCaml code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%dune_build

%install
%dune_install

# generate manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
help2man $RPM_BUILD_ROOT%{_bindir}/ocamlify \
    --output $RPM_BUILD_ROOT%{_mandir}/man1/ocamlify.1 \
    --name "Include files in OCaml code" \
    --version-string %{version} \
    --no-info

%check
%dune_check

%files -f .ofiles -f .ofiles-devel
%doc README.md
%license COPYING.txt
%{_mandir}/man1/ocamlify.1*

%changelog
%autochangelog
