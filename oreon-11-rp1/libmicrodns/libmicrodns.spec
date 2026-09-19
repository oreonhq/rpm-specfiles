%global source0_hash 9864a088ffef4d4255d5abf63c6f603d1dc343dfec2809ff0c3f1624045b80fa

Name:           libmicrodns
Version:        0.2.0
Release:        15%{?dist}
Summary:        Minimal mDNS resolver library

License:        LGPL-2.1-or-later
URL:            https://github.com/videolabs/libmicrodns
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc

%description
Minimal mDNS resolver (and announcer) library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libmicrodns.so.1*

%files devel
%{_includedir}/microdns
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc

%changelog
%autochangelog
