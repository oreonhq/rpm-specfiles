%global source0_hash fa15735edc4b3d27675d954b5703e36a158f19cfa4f265aa5388cd33aede1c70

# from https://www.unicode.org/Public files (unicode-ucd pkg)
%global unicodedir  /usr/share/unicode
%global ucddir      %{unicodedir}/ucd

Name:           mujs
Version:        1.3.7
Release:        2%{?dist}
Summary:        An embeddable Javascript interpreter
License:        ISC
URL:            https://mujs.com/
Source0:        https://mujs.com/downloads/%{name}-%{version}.tar.gz

# https://github.com/ccxvii/mujs/pull/187
Patch:          set-library-soname-version.patch

# use custom soname version until it lands upstream to avoid future potential conflict
Patch:          downstream-soname-version.patch

# Remove curl commands to get Unicode files (linked in prep section from unicode-ucd pkg)
Patch:          remove-curl-from-Makefile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  unicode-ucd

%description
MuJS is a lightweight Javascript interpreter designed for embedding in
other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the MuJS shared library.

%package static
Summary:        MuJS development files using static lib
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides the MuJS static library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod a-x -v docs/*
ln -s %{ucddir}/UnicodeData.txt
ln -s %{ucddir}/SpecialCasing.txt

%build
%make_build release prefix="%{_prefix}" libdir="%{_libdir}" CFLAGS="%{build_cflags} %{build_ldflags}"

%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}"
%{__make} install-shared DESTDIR=%{?buildroot} INSTALL="%{__install} -p" prefix="%{_prefix}" libdir="%{_libdir}"

%check

%files
%license COPYING
%doc AUTHORS README docs
%{_bindir}/%{name}
%{_bindir}/%{name}-pp
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files static
%{_libdir}/lib%{name}.a

%changelog
%autochangelog
