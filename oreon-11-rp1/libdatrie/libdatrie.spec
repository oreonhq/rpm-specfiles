%global source0_hash f04095010518635b51c2313efa4f290b7db828d6273e39b2b8858f859dfe81d5
Name:           libdatrie
Version:        0.2.14
Release:        2%{?dist}
Summary:        Implementation of Double-Array structure for representing trie
License:        LGPL-2.1-or-later
URL:            http://linux.thai.net/projects/datrie
Source0:        http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
datrie is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with O(1) 
time complexity for searching. Comparably as efficient as hashing, trie also 
provides flexibility on incremental matching and key spelling manipulation. 
This makes it ideal for lexical analyzers, as well as spelling dictionaries.

Details of the implementation: http://linux.thai.net/~thep/datrie/datrie.html

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -f -i -v
%configure --disable-static \
           --with-html-docdir=%{_pkgdocdir}-devel
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -frv %{buildroot}%{_pkgdocdir}
find %{buildroot} -name '*.*a' -delete -print
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=../datrie/.libs %make_build check
%files -f %{oreon_filedir}/main.list
%files -n libdatrie-devel -f %{oreon_filedir}/libdatrie-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.14-2
- Prepare for Oreon 11 (RP1)
