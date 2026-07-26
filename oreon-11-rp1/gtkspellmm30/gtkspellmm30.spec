%global source0_hash 5b875a5753ce593274d0c6e803af6300973020c5443905999aba96ed3cef1545

%bcond mingw 1

Name:          gtkspellmm30
Version:       3.0.5
Release:       28%{?dist}
License:       GPL-2.0-or-later
Summary:       On-the-fly spell checking for GtkTextView widgets - C++ bindings
URL:           http://gtkspell.sourceforge.net/
Source0:       http://sourceforge.net/projects/gtkspell/files/gtkspellmm/gtkspellmm-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: gtkspell3-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtkmm30-doc
BuildRequires: make

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-glibmm24
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw32-gtkspell3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-glibmm24
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw64-gtkspell3
%endif

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package       devel
Summary:       Development files for gtkspellmm30
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The gtkspellmm30-devel package provides header and documentation files for
developing C++ applications which use GtkSpell.

%package       doc
Summary:       Documentation for %{name}
BuildArch:     noarch
Requires:      gtkmm30-doc

%description   doc
This package contains the full API documentation for %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows GtkSpellmm library
Obsoletes:     mingw32-%{name}-static
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GtkSpellmm library.

%package -n mingw64-%{name}
Summary:       MinGW Windows GtkSpellmm library
Obsoletes:     mingw64-%{name}-static
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GtkSpellmm library.
%endif

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gtkspellmm-%{version}

%build
# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure
%make_build
popd

%if %{with mingw}
# MinGW build
%mingw_configure --disable-documentation
%mingw_make_build
%endif

%install
%make_install -C build_native
%if %{with mingw}
%mingw_make_install
%endif

find %{buildroot} -name "*.la" -exec rm {} \;

%{?mingw_debug_install_post}

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/libgtkspellmm-3.0.so.0*

%files devel
%{_includedir}/gtkspellmm-3.0
%{_libdir}/libgtkspellmm-3.0.so
%{_libdir}/pkgconfig/gtkspellmm-3.0.pc
%{_libdir}/gtkspellmm-3.0

%files doc
%license COPYING
%{_datadir}/devhelp/books/gtkspellmm-3.0
%{_datadir}/doc/gtkspellmm-3.0

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libgtkspellmm-3.0-0.dll
%{mingw32_includedir}/gtkspellmm-3.0/
%{mingw32_libdir}/gtkspellmm-3.0/
%{mingw32_libdir}/libgtkspellmm-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtkspellmm-3.0.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libgtkspellmm-3.0-0.dll
%{mingw64_includedir}/gtkspellmm-3.0/
%{mingw64_libdir}/gtkspellmm-3.0/
%{mingw64_libdir}/libgtkspellmm-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtkspellmm-3.0.pc
%endif

%changelog
%autochangelog
