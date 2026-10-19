%global source0_hash a96975b79ddd8fef6d9295c083fe3f1afa1a8898a57235d4069255ade44e5cf2
%global girname LangTag
%global girapiversion 0.6
%global soversion 1
%global soversion_gobject 0
Name: liblangtag
Version: 0.6.8
Release:        1%{?dist}
Summary:        An interface library to access tags for identifying languages
License: LGPL-3.0-or-later OR MPL-2.0
URL: https://bitbucket.org/tagoh/liblangtag/
Source0:        https://src.fedoraproject.org/repo/pkgs/liblangtag/liblangtag-0.6.8.tar.bz2/sha512/3072527ff6b2030d632d406ff6af854bf136112619d463c189f08a7f56bd68ffceb47fdce54ccee54a0199a017c800e68a78f8d90cc110aa6a81f9ad0a2fa69d/liblangtag-0.6.8.tar.bz2
Patch0: liblangtag-noparallel-gir.patch
Requires: %{name}-data = %{version}-%{release}
%if ! 0%{?flatpak}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package data
Summary: %{name} data files
License: Unicode-DFS-2015
BuildArch: noarch
%description data
The %{name}-data package contains data files for %{name}.

%package gobject
Summary: GObject introspection for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gobject
The %{name}-gobject package contains files for GObject introspection for
%{name}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gobject%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch
%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
%if 0%{?flatpak}
    --disable-gtk-doc \
%endif
    --disable-silent-rules --disable-static --enable-shared --enable-introspection
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
export LD_LIBRARY_PATH=`pwd`/liblangtag/.libs:`pwd`/liblangtag-gobject/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/%{name}/*.la
%ldconfig_scriptlets
%ldconfig_scriptlets gobject
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=`pwd`/liblangtag/.libs:`pwd`/liblangtag-gobject/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n liblangtag-data -f %{oreon_filedir}/liblangtag-data.list
%files -n liblangtag-gobject -f %{oreon_filedir}/liblangtag-gobject.list
%files -n liblangtag-devel -f %{oreon_filedir}/liblangtag-devel.list
%files -n liblangtag-doc -f %{oreon_filedir}/liblangtag-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.7-7
- Prepare for Oreon 11 (RP1)
