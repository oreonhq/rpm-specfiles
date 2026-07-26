%global source0_hash 1072a8b0b35bd6df939c0670add33027f981e4f69a53233cb006b442fa12af30

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-result
Version:        1.5
Release:        32%{?dist}
Summary:        Compat result type

License:        BSD-3-Clause
URL:            https://github.com/janestreet/result
VCS:            git:%{url}.git
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 1.0

%description
Projects that want to use the new result type defined in
OCaml >= 4.03 while staying compatible with older versions
of OCaml should use the Result module defined in this library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n result-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%license LICENSE.md

%changelog
%autochangelog
