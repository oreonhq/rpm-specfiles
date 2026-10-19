%global source0_hash 8bf3ff17cd0ecb2d6b6d1d94cb08ef089d44caef96e9bae6be6839d428fa318f
ExcludeArch: %{ix86}
Name:           ocaml-biniou
Version:        1.2.2
Release:        1%{?dist}
Summary:        Safe and fast binary data format
License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/biniou
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/biniou/releases/download/%{version}/biniou-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-ocamldoc
# /oreon:deps
%description
Biniou (pronounced "be new") is a binary data format designed for
speed, safety, ease of use and backward compatibility as protocols
evolve. Biniou is vastly equivalent to JSON in terms of functionality
but allows implementations several times faster (4 times faster than
yojson), with 25-35%% space savings.

Biniou data can be decoded into human-readable form without knowledge
of type definitions except for field and variant names which are
represented by 31-bit hashes. A program named bdump is provided for
routine visualization of biniou data files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-easy-format-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir biniou-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%ifarch %{ocaml_native_compiler}
mv $RPM_BUILD_ROOT%{_bindir}/{,ocaml-}bdump
sed -i '/bdump/d' .ofiles
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%ifarch %{ocaml_native_compiler}
%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-biniou-devel -f %{oreon_filedir}/ocaml-biniou-devel.list

%changelog

%autochangelog
