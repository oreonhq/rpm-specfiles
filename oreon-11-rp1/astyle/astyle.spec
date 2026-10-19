%global source0_hash fa81c6c257c4015ad37d64fa6c084c8d46bf5dabbe0b6c7e286d6ade82ef1407
Name:           astyle
Version:        3.6.19
Release:        1%{?dist}
Summary:        Source code formatter for C-like programming languages
%global soversion       %{version}
License:        MIT
URL:            https://astyle.sourceforge.net/
Source0:        https://gitlab.com/saalen/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch1:         astyle-html-help.patch
# oreon:deps
BuildRequires:  gcc-c++
# /oreon:deps
%description
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

%package devel
Summary:        Source code formatter for C-like programming languages
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

This package contains the shared library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# drop executable bit from all files
find . -type f -exec chmod a-x {} \;

%build

pushd AStyle/src
    g++ %{build_cxxflags} -DASTYLE_LIB -fPIC -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp astyle_main.cpp
    g++ %{build_ldflags} -shared -o libastyle.so.%{soversion} *.o -Wl,-soname,libastyle.so.%{soversion}
    ln -s libastyle.so.%{soversion} libastyle.so
    g++ %{build_cxxflags} -c ASLocalizer.cpp astyle_main.cpp
    g++ %{build_ldflags} -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
popd
%install
pushd AStyle/src
    mkdir -p %{buildroot}{%{_bindir},%{_libdir},%{_includedir}}
    install -p -m 755 astyle %{buildroot}%{_bindir}
    install -p -m 755 libastyle.so.%{soversion} %{buildroot}%{_libdir}
    cp -P libastyle.so %{buildroot}%{_libdir}
    install -p -m 644 astyle.h %{buildroot}%{_includedir}
popd
%oreon_autofiles astyle-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n astyle-devel -f %{oreon_filedir}/astyle-devel.list

%changelog

%autochangelog

