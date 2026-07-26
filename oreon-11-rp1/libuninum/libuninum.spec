%global source0_hash e704983c3c00e9b76bd836b8b83ce31bfe4eb1752eee8be123cf97c1275076ea

Summary:       Library for converting unicode strings to numbers
Name:          libuninum
Version:       2.7
Release:       42%{?dist}
# numconv is GPLv2, lib is LGPLv2
# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License:       GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:           http://billposer.org/Software/libuninum.html
Source0:       http://billposer.org/Software/Downloads/libuninum-%{version}.tar.bz2
Patch0:        libuninum-2.7-64bit-clean.patch
Patch1:        libuninum-configure-c99.patch
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: make
%description
libuninum is a library for converting Unicode strings to
numbers. Internal computation is done using arbitrary precision
arithmetic, so there is no limit on the size of the integer that can
be converted. The value is returned as an ASCII decimal string, a GNU
MP object, or an unsigned long integer.  Auto-detection of the number
system is provided. The number systems supported include Arabic,
Armenian, Balinese, Bengali, Burmese, Chinese, Cyrillic, Devanagari,
Egyptian, Ethiopic, Glagolitic, Greek, Gujarati, Gurmukhi, Hebrew,
Kannada, Khmer, Klingon, Lao, Limbu, Malayalam, Mongolian, New Tai
Lue, Nko, Old Italic, Old Persian, Odia, Osmanya, Perso-Arabic,
Phoenician, Roman Numerals, Tamil, Telugu, Tengwar, Thai, and Tibetan.

%package       devel
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
%description   devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -D -m 0644 numconv.1 %{buildroot}/%{_mandir}/man1/numconv.1
rm -f %{buildroot}%{_bindir}/NumberConverter.tcl
rm -f %{buildroot}%{_libdir}/libuninum.la

%files
%license COPYING
%doc AUTHORS ChangeLog CREDITS NEWS README README_NUMBERCONVERTER TODO
%doc Examples
%{_bindir}/numconv
%{_libdir}/libuninum.so.*
%{_mandir}/man1/numconv.1*

%files devel
%license COPYING
%{_includedir}/uninum
%{_libdir}/libuninum.so

%changelog
%autochangelog
