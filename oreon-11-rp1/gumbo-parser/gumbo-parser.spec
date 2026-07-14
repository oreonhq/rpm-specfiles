%global source0_hash 90bea83283760339da194fb90112a532854c13cd1eabdabc7ef7a4dede1dbc9d

Name:           gumbo-parser
Epoch:          1
Version:        0.13.2
Release:        1%{?dist}
Summary:        A HTML5 parser

License:        Apache-2.0
URL:            https://codeberg.org/grisha/gumbo-parser/
Source0:        https://codeberg.org/grisha/gumbo-parser/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         0001-Doxygen-tweaks.patch

BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  make

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as
a pure C99 library with no outside dependencies. It's designed to serve
as a building block for other tools and libraries such as linters,
validators, templating languages, and refactoring and analysis tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python
Summary:        Python bindings to %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description    python
Python bindings to %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}

./autogen.sh

doxygen -u Doxyfile

touch footer.html
doxygen -w html /dev/null footer.html /dev/null Doxyfile
sed -i -e 's,\$generatedby,Generated on $date for $projectname by,' footer.html

%generate_buildrequires
%pyproject_buildrequires

%build
%configure --disable-static --disable-silent-rules --docdir=%{_pkgdocdir}
%{make_build}

doxygen Doxyfile

%pyproject_wheel

%check
make check

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -m 755 -d ${RPM_BUILD_ROOT}%{_mandir}/man3
install -m 644 docs/man/man3/*.3 ${RPM_BUILD_ROOT}%{_mandir}/man3

install -m 755 -d ${RPM_BUILD_ROOT}%{_pkgdocdir}
cp -r docs/html ${RPM_BUILD_ROOT}%{_pkgdocdir}
install -m 644 doc/COPYING ${RPM_BUILD_ROOT}%{_pkgdocdir}
install -m 644 doc/*.md ${RPM_BUILD_ROOT}%{_pkgdocdir}

%pyproject_install
%pyproject_save_files '*'

%ldconfig_scriptlets

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/*.md
%{_libdir}/*.so.3*

%files devel
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/*.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gumbo.pc
%{_mandir}/man3/*.3*

%files python -f %{pyproject_files}
