%global source0_hash ed9bcf88d781767ad6a7c0480aff09d5889f2fc500dda0d1620a1786d4e44490

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-pcre
Version:        8.0.5
Release:        3%{?dist}
Summary:        Perl compatibility regular expressions (PCRE) for OCaml

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/pcre-ocaml
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/pcre-%{version}.tbz

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pcre-devel

%description
Perl compatibility regular expressions (PCRE) for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pcre-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pcre-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGELOG.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
