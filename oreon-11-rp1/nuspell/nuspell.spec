%global source0_hash none

Name:           nuspell
Version:        5.1.7
Release:        4%{?dist}
Summary:        Fast and safe spellchecking C++ library and command-line tool
License:        LGPL-3.0-or-later
URL:            https://nuspell.github.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Add DLL version suffix
Patch0:         nuspell-dllver.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  pandoc
BuildRequires:  catch-devel
BuildRequires:  doxygen

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-icu

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-icu

Requires:       hunspell-en-US

%description
Nuspell is a fast and safe spelling checker software program. It is designed \
for languages with rich morphology and complex word compounding. Nuspell is \
written in modern C++ and it supports Hunspell dictionaries.


%package devel
Summary:        Development tools for %{name}
Requires:       libicu-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and developer docs for \
%{name}.


%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}


%build
%cmake
%cmake_build

%mingw_cmake -DBUILD_TESTING=OFF
%mingw_make_build


%install
%cmake_install
%mingw_make_install

# Drop docs from mingw packages
rm -rf %{buildroot}%{mingw32_docdir}/%{name}
rm -rf %{buildroot}%{mingw64_docdir}/%{name}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%mingw_debug_install_post


%check
%ctest


%files
%doc AUTHORS CHANGELOG.md README.md
%license COPYING COPYING.LESSER
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.5*
%{_mandir}/man1/nuspell.1*

%files devel
%doc %{_docdir}/nuspell/
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files -n mingw32-%{name}
%license COPYING COPYING.LESSER
%{mingw32_bindir}/%{name}.exe
%{mingw32_bindir}/lib%{name}-5.dll
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/cmake/%{name}/
%{mingw32_libdir}/pkgconfig/%{name}.pc
%{mingw32_libdir}/lib%{name}.dll.a


%files -n mingw64-%{name}
%license COPYING COPYING.LESSER
%{mingw64_bindir}/%{name}.exe
%{mingw64_bindir}/lib%{name}-5.dll
%{mingw64_includedir}/%{name}/
%{mingw64_libdir}/cmake/%{name}/
%{mingw64_libdir}/pkgconfig/%{name}.pc
%{mingw64_libdir}/lib%{name}.dll.a


%changelog
%autochangelog

