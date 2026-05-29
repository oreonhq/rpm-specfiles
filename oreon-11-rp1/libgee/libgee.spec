%global source0_hash 189815ac143d89867193b0c52b7dc31f3aa108a15f04d6b5dca2b6adfad0b0ee

Name:           libgee
Version:        0.20.8
Release:        3%{?dist}
Summary:        GObject collection library

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libgee
Source0:        https://download.gnome.org/sources/libgee/0.20/libgee-0.20.8.tar.xz

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala
BuildRequires:  make

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

* Traversable
  o Iterable
    + Collection
      - List
        * BidirList
      - Set
        * SortedSet
          o BidirSortedSet
      - MultiSet
      - Queue
        * Deque
    + Map
      - SortedMap
        * BidirSortedMap
  o Iterator
    + BidirIterator
      - BidirListIterator
    + ListIterator
      - BidirListIterator
* MultiMap

The ArrayList, ArrauQueue, ConcurrentLinkedList, ConcurrentSet, HashSet,
HashMap, HashMultiSet, HashMultiMap, LinkedList, PriorityQueue, TreeSet,
TreeMap, TreeMultiSet, and TreeMultiMap classes provide a reasonable sample
implementation of those interfaces. In addition, a set of abstract
classes are provided to ease the implementation of new collections.

Around that, the API provide means to retrieve read-only views,
efficient sort algorithms, simple, bi-directional or index-based mutable
iterators depending on the collection type.

Libgee is written in Vala and can be used like any GObject-based C
library. It's planned to provide bindings for further languages.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
find -name '*.vala' -exec touch {} \;

%build
%configure --disable-static --enable-vala
%make_build


%check
make check


%install
%make_install \
    typelibdir=%{_libdir}/girepository-1.0 \
    girdir=%{_datadir}/gir-1.0
find $RPM_BUILD_ROOT -name '*.la' -delete


%ldconfig_scriptlets


%files
%doc AUTHORS MAINTAINERS NEWS README
%license COPYING
%{_libdir}/*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gee-0.8.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gee-0.8.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gee-0.8.vapi


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20.8-3
- Prepare for Oreon 11 (RP1)
