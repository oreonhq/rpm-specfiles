%global source0_hash 1788da91e28248388223e0770fc1b66d190faf178c4f3f43fc5a7bd739e62297
%global pkg_name bytestring-trie
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.7.7
Release:        1%{?dist}
Summary:        An efficient finite map from bytestrings to values
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/bytestring-trie
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
An efficient finite map from bytestrings to values.

The implementation is based on big-endian patricia trees, like "Data.IntMap".
We first trie on the elements of "Data.ByteString" and then trie on the
big-endian bit representation of those elements. Patricia trees have efficient
algorithms for union and other merging operations, but they're also quick for
lookups and insertions.

If you are only interested in being able to associate strings to values, then
you may prefer the 'hashmap' package which is faster for those only needing a
map-like structure. This package is intended for those who need the extra
capabilities that a trie-like structure can offer (e.g., structure sharing to
reduce memory costs for highly redundant keys, taking the submap of all keys
with a given prefix, contextual mapping, extracting the minimum and maximum
keys, etc.).

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-bytestring-trie-devel -f %{oreon_filedir}/ghc-bytestring-trie-devel.list
%files -n ghc-bytestring-trie-doc -f %{oreon_filedir}/ghc-bytestring-trie-doc.list
%files -n ghc-bytestring-trie-prof -f %{oreon_filedir}/ghc-bytestring-trie-prof.list

%changelog

%autochangelog
