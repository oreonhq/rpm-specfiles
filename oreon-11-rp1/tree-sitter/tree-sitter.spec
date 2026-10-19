%global source0_hash d35c96e68736bd9569d2757c3cc71052485f33082c3825f1aed9d0e86013a159
%global tree_sitter_so_version 0.27
%global tree_sitter_language_version 15
%global tree_sitter_min_compatible_language_version 13
Name:           tree-sitter
Version:        0.27.0
Release:        1%{?dist}
Summary:        An incremental parsing system for programming tools
License:        MIT
URL:            https://tree-sitter.github.io/
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
%{__make} %{?_smp_mflags} -j${RPM_BUILD_NCPUS} %{?_make_verbose}
%install
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}' INCLUDEDIR='%{_includedir}'
%{__make} install DESTDIR=%{buildroot} %{?_make_verbose}
find %{buildroot}%{_libdir} -type f \( -name "*.la" -o -name "*.a" \) -delete -print
install -d %{buildroot}%{_datadir}/tree-sitter/queries
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

grep -q '^#define TREE_SITTER_LANGUAGE_VERSION %tree_sitter_language_version' \
     lib/include/tree_sitter/api.h
grep -q '^#define TREE_SITTER_MIN_COMPATIBLE_LANGUAGE_VERSION %tree_sitter_min_compatible_language_version' \
     lib/include/tree_sitter/api.h
%files -f %{oreon_filedir}/main.list
%files -n libtree-sitter -f %{oreon_filedir}/libtree-sitter.list
%files -n libtree-sitter-devel -f %{oreon_filedir}/libtree-sitter-devel.list

%changelog

%autochangelog
