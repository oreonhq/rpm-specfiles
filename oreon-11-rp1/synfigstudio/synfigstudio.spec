%global source0_hash 83375ae002f3a0393b7e02ff842262a089161af3b21d7f3b569cad7a819c128e
%define debug_package %{nil}
Name:           synfigstudio
Version:        1.5.5
Release:        1%{?dist}
Summary:        Vector-based 2D animation studio
License:        GPL-2.0-or-later
URL:            http://synfig.org/
Source0:        http://download.sourceforge.net/synfig/%{name}-%{version}.tar.gz
Patch1:         synfig-studio-m4_pattern_allow.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ETL-devel
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  ladspa
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  synfig-devel
# /oreon:deps
%description
Synfig Animation Studio is a powerful, industrial-strength vector-based
2D animation software, designed from the ground-up for producing
feature-film quality animation with fewer people and resources.
It is designed to be capable of producing feature-film quality
animation. It eliminates the need for tweening, preventing the
need to hand-draw each frame. Synfig features spatial and temporal
resolution independence (sharp and smoothat any resolution or framerate),
high dynamic range images, and a flexible plugin system.

This package contains the GUI-based animation studio.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p0 -b .m4allow

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoreconf -fi
intltoolize -f
%configure --disable-update-mimedb
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-install \
        --delete-original                                       \
        --dir=%{buildroot}%{_datadir}/applications           \
        %{buildroot}%{_datadir}/applications/org.synfig.SynfigStudio.desktop
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n synfigstudio-devel -f %{oreon_filedir}/synfigstudio-devel.list

%changelog

%autochangelog
