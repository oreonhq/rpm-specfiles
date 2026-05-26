%global tree_sitter_so_version 0

# Keep these up-to-date with the values in lib/include/tree_sitter/api.h:
%global tree_sitter_language_version 15
%global tree_sitter_min_compatible_language_version 13


Name:           tree-sitter
Version:        0.25.10
Release:        %autorelease
Summary:        An incremental parsing system for programming tools

License:        MIT
URL:            https://tree-sitter.github.io/
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ad5040537537012b16ef6e1210a572b927c7cdc2b99d1ee88d44a7dcdc3ff44c
%global source0_file tree-sitter-0.25.10.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: make


%description
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. Tree-sitter aims to be:

 * General enough to parse any programming language
 * Fast enough to parse on every keystroke in a text editor
 * Robust enough to provide useful results even in the presence
   of syntax errors
 * Dependency-free so that the runtime library (which is written
   in pure C) can be embedded in any application

%package -n lib%{name}
Summary:        Incremental parsing library for programming tools
%{lua:
  for i = rpm.expand('%tree_sitter_min_compatible_language_version'),
          rpm.expand('%tree_sitter_language_version') do
    print(string.format("Provides: tree-sitter(:LANGUAGE_VERSION) = %d\n", i))
  end
}

%description -n lib%{name}
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. This is the package with the dynamically linked C library.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/tree-sitter-0.25.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ad5040537537012b16ef6e1210a572b927c7cdc2b99d1ee88d44a7dcdc3ff44c" || { echo "oreon: Source0 SHA256 mismatch for tree-sitter-0.25.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%set_build_flags
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
%make_build


%install
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}' INCLUDEDIR='%{_includedir}'
%make_install

find %{buildroot}%{_libdir} -type f \( -name "*.la" -o -name "*.a" \) -delete -print

install -d %{buildroot}%{_datadir}/tree-sitter/queries


%check
grep -q '^#define TREE_SITTER_LANGUAGE_VERSION %tree_sitter_language_version' \
     lib/include/tree_sitter/api.h
grep -q '^#define TREE_SITTER_MIN_COMPATIBLE_LANGUAGE_VERSION %tree_sitter_min_compatible_language_version' \
     lib/include/tree_sitter/api.h


%files -n lib%{name}
%license LICENSE
%doc README.md
%dir %{_datadir}/tree-sitter
%dir %{_datadir}/tree-sitter/queries
%{_libdir}/libtree-sitter.so.%{tree_sitter_so_version}*

%files -n lib%{name}-devel
%{_includedir}/tree_sitter
%{_libdir}/libtree-sitter.so
%{_libdir}/pkgconfig/tree-sitter.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25.10-1
- Prepare for Oreon 11 (RP1)
