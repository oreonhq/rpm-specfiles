%global source0_hash 3b3fe6008445feb1fca61b17b9d950d688e49dcca60dbbf8667c0f980ddfc563

Summary: Rendering of internationalized text for SDL2 (Simple DirectMedia Layer)
Name: SDL2_Pango
Version: 2.1.5
Release: 6%{?dist}
License: LGPL-2.1-or-later
URL: https://github.com/markuskimius/SDL2_Pango

Source0: https://github.com/markuskimius/SDL2_Pango/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: pango-devel
BuildRequires: SDL2-devel

%description
SDL2_Pango is a library for graphically rendering
internationalized and tagged text in SDL2 using TrueType fonts.

%package devel
Summary: Development files for SDL2_pango
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pango-devel%{?_isa}
Requires: SDL2-devel%{?_isa}
Requires: pkgconfig

%description devel
Development files for SDL2_pango.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.4*

%files devel
%doc docs/html/*
%{_includedir}/SDL2_Pango.h
%{_libdir}/pkgconfig/SDL2_Pango.pc
%{_libdir}/*.so

%changelog
%autochangelog
