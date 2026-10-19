%global source0_hash 2929c28a042453ee67785201dda234308ef19e068fb474cc1db69dd5f67c4dab
%global source1_hash e04fbc7b4243b5cb69819ae10f26bd375f94d8986a939cd4e6f6ca555dab7dbd
%global source2_hash 23dfa86c2ecd2601a2efed4967eb2ec0505a52c14776054ce4d89707c2de0a9b
%global source3_hash 44e82ceaebb240f22882e7640633d747453887f74384dd5ffd258d802d7352e6
%global source4_hash 004213e13d89b692ea0912d7ffa6ee98c93146d1a7962a849ad7860697bc88bd
%global source5_hash 97b66c9ab60451e41a94aa80a684e792fbe69816835f735224222beea22afb78
%global source6_hash 994cd2db976f6818bfb7644674c5f7c5830e9c5a339243541ac24611ff672ce4
%global pkg_name skylighting
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global skylightingcore skylighting-core-0.14.7
%global skylightingformatansi skylighting-format-ansi-0.1
%global skylightingformatblazehtml skylighting-format-blaze-html-0.1.1.3
%global skylightingformatcontext skylighting-format-context-0.1.0.2
%global skylightingformatlatex skylighting-format-latex-0.1
%global skylightingformattypst skylighting-format-typst-0.1
%global subpkgs %{skylightingcore} %{skylightingformatansi} %{skylightingformatblazehtml} %{skylightingformatcontext} %{skylightingformatlatex} %{skylightingformattypst}
Name:           ghc-%{pkg_name}
Version:        0.15
Release:        1%{?dist}
Summary:        Syntax highlighting library
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/skylighting
Source0:        https://hackage.haskell.org/package/skylighting-%{version}/skylighting-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{skylightingcore}/%{skylightingcore}.tar.gz
Source2:        https://hackage.haskell.org/package/skylighting-format-ansi-0.1/skylighting-format-ansi-0.1.tar.gz
Source3:        https://hackage.haskell.org/package/skylighting-format-blaze-html-0.1.1.3/skylighting-format-blaze-html-0.1.1.3.tar.gz
Source4:        https://hackage.haskell.org/package/skylighting-format-context-0.1.0.2/skylighting-format-context-0.1.0.2.tar.gz
Source5:        https://hackage.haskell.org/package/skylighting-format-latex-0.1/skylighting-format-latex-0.1.tar.gz
Source6:        https://hackage.haskell.org/package/skylighting-format-typst-0.1/skylighting-format-typst-0.1.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
# /oreon:deps
%description
Skylighting is a syntax highlighting library with support for over one hundred
languages. It derives its tokenizers from XML syntax definitions used by KDE's
KSyntaxHighlighting framework, so any syntax supported by that framework can be
added. An optional command-line program is provided. Skylighting is intended to
be the successor to highlighting-kate. This package provides generated syntax
modules based on the KDE XML definitions provided by the 'skylighting-core'
package. As a result this package is licensed under the GPL.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingcore}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingformatansi}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingformatblazehtml}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingformatcontext}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingformatlatex}
%ghc_lib_subpackage -l BSD-3-Clause %{skylightingformattypst}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3 -a4 -a5 -a6
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-skylighting-devel -f %{oreon_filedir}/ghc-skylighting-devel.list
%files -n ghc-skylighting-doc -f %{oreon_filedir}/ghc-skylighting-doc.list
%files -n ghc-skylighting-prof -f %{oreon_filedir}/ghc-skylighting-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.7-16
- Prepare for Oreon 11 (RP1)
