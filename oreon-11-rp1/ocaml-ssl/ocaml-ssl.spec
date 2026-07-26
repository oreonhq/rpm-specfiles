%global source0_hash 932726838c6bfd82727b24af660a37d3bc0b905ea3f80b07056fe0901d92ed6c

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global forgeurl https://github.com/savonet/ocaml-ssl
#global tag    x.y.z
%global commit ffc634d9adc8ebf5c6cc6cd5002233c4ab233798
Version:       0.7.0
%forgemeta

Name:           ocaml-ssl
Release:        17%{?dist}
Summary:        SSL bindings for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source0:        %{forgesource}

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  %{_bindir}/openssl
BuildRequires:  openssl-devel >= 1.0.2

%description
SSL bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license COPYING

%files devel -f .ofiles-devel
# We used to include the examples, but they are GPL-2.0-only.
# Put them in a separate subpackage?

%changelog
%autochangelog
