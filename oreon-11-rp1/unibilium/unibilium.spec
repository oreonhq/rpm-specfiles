%global source0_hash 7360907bcf79ba49f6fc4a504767ff86e93ab9018477026fcc70d5ab77e1f2c1
Name:           unibilium
Version:        2.1.4
Release:        1%{?dist}
Summary:        Terminfo parsing library
License:        LGPL-3.0-or-later
URL:            https://github.com/neovim/unibilium
Source0:        https://github.com/neovim/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/bin/prove
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fi

%build

%configure
%make_build
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n unibilium-devel -f %{oreon_filedir}/unibilium-devel.list

%changelog

%autochangelog
