%global source0_hash ba5d13b9b508ec693613b3b61518163aced38f8e885f7e28dc047348a4e61365
Name:           gumbo-parser
Epoch:          1
Version:        0.14.1
Release:        1%{?dist}
Summary:        A HTML5 parser
License:        Apache-2.0
URL:            https://codeberg.org/grisha/gumbo-parser/
Source0:        https://codeberg.org/grisha/gumbo-parser/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         0001-Doxygen-tweaks.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gumbo-parser = %{version}-%{release}
# /oreon:deps
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
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n gumbo-parser-devel -f %{oreon_filedir}/gumbo-parser-devel.list
%files -n gumbo-parser-python -f %{oreon_filedir}/gumbo-parser-python.list

%changelog

%autochangelog
