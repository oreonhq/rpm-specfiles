%global source0_hash d3654417013772141e2843998957a8b08f56cc10cd9c025a50f9070572914065

%global git_commit 4f795aeba2d9ee52f82e8666d55f6a469576dfa0
%global git_date 20200903

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Summary:  Timezone information for the Cyrus IMAP Server
Name: cyrus-timezones
Version:  %{git_date}
Release: 15.%{git_suffix}%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Group: Applications/Internet
URL: https://github.com/cyrusimap/cyrus-timezones
Source0: https://github.com/cyrusimap/%{name}/archive/%{git_commit}/%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: libical-devel
BuildRequires: glib2-devel
BuildRequires: chrpath
BuildRequires: make

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

%files
%doc AUTHORS README MAINTAINER_NOTES
%license COPYING
%{_datadir}/%{name}
%{_bindir}/cyr_vzic

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
