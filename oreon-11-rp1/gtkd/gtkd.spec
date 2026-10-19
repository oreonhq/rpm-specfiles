%global source0_hash c5de7ef0d955c06a35bc979858e2b67c17919294a7aabe36fd593b79c46e5928
%global debug_package %{nil}
%global sover 0
Name:           gtkd
Version:        3.11.0
Release:        1%{?dist}
Summary:        D binding and OO wrapper of GTK+
License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GtkD/
Source0:        https://github.com/gtkd-developers/GtkD/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         361.patch
Patch1:         gtkd-fix-version.patch
ExclusiveArch:  %{ldc_arches}
Requires:       atk%{?_isa}
Requires:       cairo%{?_isa}
Requires:       gdk-pixbuf2%{?_isa}
Requires:       gstreamer1%{?_isa}
Requires:       gstreamer1-plugins-base%{?_isa}
Requires:       gtk3%{?_isa}
Requires:       gtksourceview4%{?_isa}
Requires:       libcurl%{?_isa}
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
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
# oreon:deps
BuildRequires:  geany
BuildRequires:  ldc
BuildRequires:  make
# /oreon:deps
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
geany -c geany_config -g gtkd.d.tags $(find src* -name "*.d")
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{?_lib} \
     install-shared-gtkdgl install-headers-gtkdgl \
     install-shared install-headers
mkdir -p %{buildroot}%{_datadir}/geany/tags/
install -m0644 gtkd.d.tags %{buildroot}%{_datadir}/geany/tags/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make %{?_smp_mflags} DC=ldc2 libdir=%{?_lib} DCFLAGS="%{_d_optflags}" LDFLAGS="" test
%files -f %{oreon_filedir}/main.list
%files -n gtkd-devel -f %{oreon_filedir}/gtkd-devel.list
%files -n gtkd-geany-tags -f %{oreon_filedir}/gtkd-geany-tags.list

%changelog

%autochangelog
