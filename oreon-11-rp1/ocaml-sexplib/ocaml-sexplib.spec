%global source0_hash da863b42b81235fdcf45eb32c04fb8bde22ff446a779cfb6f989730a35103160

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# The tests introduce circular dependencies, so do not test by default
%bcond test 0

Name:           ocaml-sexplib
Version:        0.17.0
Epoch:          1
Release:        %autorelease
Summary:        Automated S-expression conversion

# The project as a whole is MIT, but code in the src subdirectory is BSD.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/janestreet/sexplib
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/sexplib-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-parsexp-devel >= 0.17
BuildRequires:  ocaml-sexplib0-devel >= 0.17
BuildRequires:  vim-filesystem

%if %{with test}
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-base-quickcheck-devel
BuildRequires:  ocaml-core-kernel-devel
BuildRequires:  ocaml-expect-test-helpers-core-devel
BuildRequires:  ocaml-ppx-jane-devel
%endif

%description
This package contains a library for serializing OCaml values to and from
S-expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-num-devel%{?_isa}
Requires:       ocaml-parsexp-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        vim
Summary:        Support for sexplib syntax in vim
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       vim-filesystem

%description    vim
This package contains a vim syntax file for Sexplib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sexplib-%{version}

%build
%dune_build

%install
%dune_install

# Install the vim support
mkdir -p %{buildroot}%{vimfiles_root}/syntax
cp -p vim/syntax/sexplib.vim %{buildroot}%{vimfiles_root}/syntax

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.org
%license COPYRIGHT.txt LICENSE.md LICENSE-Tywith.txt THIRD-PARTY.txt

%files devel -f .ofiles-devel

%files vim
%{vimfiles_root}/syntax/sexplib.vim

%changelog
%autochangelog
