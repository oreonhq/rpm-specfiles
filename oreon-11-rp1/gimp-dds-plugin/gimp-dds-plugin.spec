%global source0_hash 6e53df3b8b98c55f22fa7ea2c3ed17478626c924b24c69d499f5d813c3c2788a

Name:           gimp-dds-plugin
Version:        3.0.1
Release:        24%{?dist}
Summary:        A plugin for GIMP allows you to load/save in the DDS format
Summary(ru):    Плагин GIMP для работы с форматом DDS

License:        GPLv2+
URL:            http://code.google.com/p/gimp-dds/
Source0:        http://gimp-dds.googlecode.com/files/gimp-dds-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gimp-devel >= 2.4.0
BuildRequires: make

Requires:       gimp >= 2.4

%description
This is a plugin for GIMP. It allows you to load and save images in the
Direct Draw Surface (DDS) format.

%description -l ru
Плагин для GIMP, помогающий загружать и сохранять изображения
в формате Direct Draw Surface (DDS).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gimp-dds-%{version}
sed -i -e 's/CFLAGS.*/& $(shell echo $$CFLAGS)/' Makefile

%build
%set_build_flags
%make_build

%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
install dds $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins

%files
%{_libdir}/gimp/2.0/plug-ins/dds
%doc README
%license COPYING LICENSE

%changelog
%autochangelog
