%global source0_hash 71316b55592f8d0c98924242c98dbfa6252153a8b6e7d89e57fe6923934d77d0

%?mingw_package_header

%global name1 libconfuse
Name:           mingw-%{name1}
Version:        3.2.2
Release:        20%{?dist}
Summary:        MinGW configuration file parser library

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/martinh/libconfuse
Source0:        https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  check-devel
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext

%description
libConfuse is a configuration file parser library, licensed under
the terms of the ISC license, and written in C. It supports
sections and (lists of) values (strings, integers, floats,
booleans or other sections), as well as some other features (such
as single/double-quoted strings, environment variable expansion,
functions and nested include statements). It makes it very
easy to add configuration file capability to a program using
a simple API.

The goal of libConfuse is not to be the configuration file parser
library with a gazillion of features. Instead, it aims to be
easy to use and quick to integrate with your code.

%package -n mingw32-%{name1}
Summary:        MinGW configuration file parser library

%description -n mingw32-%{name1}
libConfuse is a configuration file parser library, licensed under
the terms of the ISC license, and written in C. It supports
sections and (lists of) values (strings, integers, floats,
booleans or other sections), as well as some other features (such
as single/double-quoted strings, environment variable expansion,
functions and nested include statements). It makes it very
easy to add configuration file capability to a program using
a simple API.

The goal of libConfuse is not to be the configuration file parser
library with a gazillion of features. Instead, it aims to be
easy to use and quick to integrate with your code.

%package -n mingw64-%{name1}
Summary:        MinGW configuration file parser library

%description -n mingw64-%{name1}
libConfuse is a configuration file parser library, licensed under
the terms of the ISC license, and written in C. It supports
sections and (lists of) values (strings, integers, floats,
booleans or other sections), as well as some other features (such
as single/double-quoted strings, environment variable expansion,
functions and nested include statements). It makes it very
easy to add configuration file capability to a program using
a simple API.

The goal of libConfuse is not to be the configuration file parser
library with a gazillion of features. Instead, it aims to be
easy to use and quick to integrate with your code.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n confuse-%{version}

%build
%mingw_configure --disable-static --disable-examples
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT/%{mingw32_datadir}/doc/confuse/{AUTHORS,ChangeLog.md,LICENSE,README.md}
rm -f $RPM_BUILD_ROOT/%{mingw64_datadir}/doc/confuse/{AUTHORS,ChangeLog.md,LICENSE,README.md}
rm -rf $RPM_BUILD_ROOT/doc/html

%mingw_find_lang confuse --all-name

%files -n mingw32-%{name1} -f mingw32-confuse.lang
%license LICENSE
%doc AUTHORS README.md
%{mingw32_bindir}/libconfuse-2.dll
%{mingw32_includedir}/confuse.h
%{mingw32_libdir}/libconfuse.dll.a
%{mingw32_libdir}/pkgconfig/libconfuse.pc

%files -n mingw64-%{name1} -f mingw64-confuse.lang
%license LICENSE
%doc AUTHORS README.md
%{mingw64_bindir}/libconfuse-2.dll
%{mingw64_includedir}/confuse.h
%{mingw64_libdir}/libconfuse.dll.a
%{mingw64_libdir}/pkgconfig/libconfuse.pc

%changelog
%autochangelog
