%global source0_hash none

Name:           astyle
Version:        3.6.16
Release:        1%{?dist}
Summary:        Source code formatter for C-like programming languages

%global soversion       %{version}

License:        MIT
URL:            https://astyle.sourceforge.net/
Source0:        https://gitlab.com/saalen/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++

# Fix (hardcoded) path to html-help
Patch1:         astyle-html-help.patch

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
    # it's much easier to compile it here than trying to fix the Makefile
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


%files
%license AStyle/LICENSE.md
%doc AStyle/doc/*.html
%{_bindir}/astyle
%{_libdir}/libastyle.so.%{soversion}

%files devel
%{_libdir}/libastyle.so
%{_includedir}/astyle.h


%changelog
%autochangelog

