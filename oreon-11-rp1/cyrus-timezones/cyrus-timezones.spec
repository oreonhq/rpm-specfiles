%global source0_hash d3654417013772141e2843998957a8b08f56cc10cd9c025a50f9070572914065
%global git_commit 4f795aeba2d9ee52f82e8666d55f6a469576dfa0
%global git_date 20200903
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Summary:        Timezone information for the Cyrus IMAP Server
Name: cyrus-timezones
Version:  %{git_date}
Release:        1%{?dist}
License: GPL-2.0-or-later
Group: Applications/Internet
URL: https://github.com/cyrusimap/cyrus-timezones
Source0:        https://github.com/cyrusimap/%{name}/archive/%{git_commit}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  glib2-devel
BuildRequires:  libical-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
%{summary}

%package devel
Summary: Package config configuration for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf-pkg-config
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}
autoreconf -i --verbose  --warnings=all

%build

%configure
%make_build
%install
%make_install 
chrpath -d %{buildroot}/%{_bindir}/cyr_vzic
%oreon_autofiles cyrus-timezones-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cyrus-timezones-devel -f %{oreon_filedir}/cyrus-timezones-devel.list

%changelog

%autochangelog
