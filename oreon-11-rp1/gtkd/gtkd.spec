%global source0_hash c5de7ef0d955c06a35bc979858e2b67c17919294a7aabe36fd593b79c46e5928

# debug info seem not works with D compiler
%global debug_package %{nil}

%global sover 0

Name:           gtkd
Version:        3.11.0
Release:        4%{?dist}
Summary:        D binding and OO wrapper of GTK+

License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GtkD/
Source0:        https://github.com/gtkd-developers/GtkD/archive/v%{version}/%{name}-%{version}.tar.gz
# Backported from upstream
# https://github.com/gtkd-developers/GtkD/pull/361
Patch0:         361.patch
# https://github.com/gtkd-developers/GtkD/pull/363
Patch1:         gtkd-fix-version.patch

ExclusiveArch:  %{ldc_arches}

BuildRequires:  ldc
# Explicit require since gtkd use dlopen internally so rpm can't detect this.
Requires:       atk%{?_isa}
Requires:       cairo%{?_isa}
Requires:       gdk-pixbuf2%{?_isa}
Requires:       gstreamer1%{?_isa}
Requires:       gstreamer1-plugins-base%{?_isa}
Requires:       gtk3%{?_isa}
Requires:       gtksourceview4%{?_isa}
Requires:       libcurl%{?_isa}
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
Requires:       libpeas1%{?_isa}
Requires:       libpeas1-gtk%{?_isa}
%else
Requires:       libpeas%{?_isa}
Requires:       libpeas-gtk%{?_isa}
%endif
Requires:       librsvg2%{?_isa}
Requires:       mesa-libGL%{?_isa}
Requires:       mesa-libGLU%{?_isa}
Requires:       pango%{?_isa}
Requires:       vte291%{?_isa}

%description
GTK+ is a highly usable, feature rich toolkit for creating graphical user
interfaces which boasts cross platform compatibility and an easy to use API.

%description -l fr
GTK+ est très utilisable, cet outil contient de nombreuses fonctionnalités
permettant de créer des interfaces graphiques multi-plateforme.
De plus, gtkd fournit une API facile à utiliser.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The gtkd-devel package contains header files for developing gtkd
applications.

%description devel -l fr
Le paquet gtkd-devel contient les fichiers d'entêtes pour développer
des applications utilisant gtkd.

%package geany-tags
Summary:        Support for enable autocompletion in geany
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  geany
BuildRequires:  make
Requires:       geany

%description geany-tags
Enable autocompletion for gtkd library in geany (IDE)

%description -l fr geany-tags
Active l'autocompletion pour pour la bibliothèque gtkd dans geany (IDE)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n GtkD-%{version} -p1

# Fedora's pkgconfig for gtksourceview is 4, not 4.0
sed -i 's/gtksourceview-4.0/gtksourceview-4/g' GNUmakefile

# temp geany config directory for allow geany to generate tags
mkdir geany_config

%build
make %{?_smp_mflags} DC=ldc2 libdir=%{?_lib} DCFLAGS="%{_d_optflags}" LDFLAGS="" \
     shared-gtkdgl \
     shared-libs
# generate geany tags
geany -c geany_config -g gtkd.d.tags $(find src* -name "*.d")

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{?_lib} \
     install-shared-gtkdgl install-headers-gtkdgl \
     install-shared install-headers

# geany tags
mkdir -p %{buildroot}%{_datadir}/geany/tags/
install -m0644 gtkd.d.tags %{buildroot}%{_datadir}/geany/tags/

%check
make %{?_smp_mflags} DC=ldc2 libdir=%{?_lib} DCFLAGS="%{_d_optflags}" LDFLAGS="" test

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libgstreamerd-3.so.%{sover}*
%{_libdir}/libgtkd-3.so.%{sover}*
%{_libdir}/libgtkdgl-3.so.%{sover}*
%{_libdir}/libgtkdsv-3.so.%{sover}*
%{_libdir}/libpeasd-3.so.%{sover}*
%{_libdir}/libvted-3.so.%{sover}*

%files devel
%{_d_includedir}/gtkd-3/
%{_libdir}/libgstreamerd-3.so
%{_libdir}/libgtkd-3.so
%{_libdir}/libgtkdgl-3.so
%{_libdir}/libgtkdsv-3.so
%{_libdir}/libpeasd-3.so
%{_libdir}/libvted-3.so
%{_libdir}/pkgconfig/gstreamerd-3.pc
%{_libdir}/pkgconfig/gtkd-3.pc
%{_libdir}/pkgconfig/gtkdgl-3.pc
%{_libdir}/pkgconfig/gtkdsv-3.pc
%{_libdir}/pkgconfig/peasd-3.pc
%{_libdir}/pkgconfig/vted-3.pc

%files geany-tags
%{_datadir}/geany/tags/gtkd.d.tags

%changelog
%autochangelog
