%global source0_hash a6726eef3a041dcb30249a3be7aa4e04bf6617d8da4228f45580dc1b923474f2
Name:           powwow
Version:        1.2.23
Release:        1%{?dist}
Summary:        A console MUD client
License:        GPL-2.0-or-later
URL:            http://hoopajoo.net/projects/powwow.html
Source0:        http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz
Patch0:         powwow-no-termio.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
# /oreon:deps
%description
Powwow is a powerful console MUD client that supports triggers, aliases,
multiple connections, and more. It is primarily designed for DikuMUDs, but
nothing prevents its use for other types of MUDs. This client is also
extensible through a plugin interface.

%package devel
Summary:        Development files for powwow
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The powwow-devel package contains the headers files and developer docs
for developing applications which use powwow plugin interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Convert to utf-8
for file in README doc/powwow.doc; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build

%global optflags %optflags -std=gnu17
%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_datadir}/powwow/powwow.doc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n powwow-devel -f %{oreon_filedir}/powwow-devel.list

%changelog

%autochangelog
