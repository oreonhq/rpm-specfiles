%global source0_hash 6b7f7993f82796854d5036572b879ffaaf7e0b619d12abdb318ce14757bdda91

Name:               girara
Version:            0.4.5
Release:            4%{?dist}
Summary:            Simple user interface library
License:            Zlib
URL:                https://pwmt.org/projects/%{name}/
Source0:            https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz

#BuildRequires:      binutils
BuildRequires:      gcc
BuildRequires:      gettext
BuildRequires:      glib2-devel >= 2.72
BuildRequires:      gtk3-devel >= 3.24
BuildRequires:      intltool
BuildRequires:      meson >= 0.61
BuildRequires:      pango-devel >= 1.50
BuildRequires:      pkgconfig(json-glib-1.0)
# Tests
BuildRequires:      pkgconfig(check) >= 0.11
Buildrequires:      xorg-x11-server-Xvfb

# from Upstream: Mark girara_libnotify as deprecated
#BuildRequires:      libnotify-devel >= 0.7.0

%global girara_locales  lib%{name}-gtk3-4

%description
Girara is a library that implements a user interface that focuses on simplicity
and minimalism.

%package      devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson -Ddocs=disabled -Dtests=enabled
%meson_build

%install
%meson_install
%find_lang %{girara_locales}

%check
%meson_test

%files -f %{girara_locales}.lang
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libgirara-gtk3.so.4
%{_libdir}/libgirara-gtk3.so.4.0

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/girara-gtk3.pc
%{_libdir}/libgirara-gtk3.so

%changelog
%autochangelog
