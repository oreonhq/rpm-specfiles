%global source0_hash a692fa7cdcc9e80fd9387c4f61677776b9fc15f9f7175b4220fcd1a73d1bafda
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-mew-vi
Version:        0.5.0
Release:        34%{?dist}
Summary:        Modal Editing Witch, VI interpreter
License:        MIT
URL:            https://github.com/kandu/mew_vi
VCS:            git:%{url}.git
Source0:        https://github.com/kandu/mew_vi/archive/%{version}/mew_vi-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-mew-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-react-devel
# /oreon:deps
%description
This is a vi-like modal editing engine generator.  Provide `Key`, `Mode`, and
`Concurrent` modules to define the real world environment to get a handy
vi-like modal editing engine.  Feed the the `i` channel user input and get the
vi actions from the `action_output` channel.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-mew-devel%{?_isa}
Requires:       ocaml-react-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mew_vi-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mew-vi-devel -f %{oreon_filedir}/ocaml-mew-vi-devel.list

%changelog

%autochangelog
