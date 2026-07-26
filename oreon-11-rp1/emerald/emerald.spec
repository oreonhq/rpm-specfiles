%global source0_hash fef4ce5675f79840b811e42006063a2f21d1f3cc721c9a6d37e1a123dc6f0c54

%global  basever 0.8.16

Name:           emerald
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Version:        0.8.18
Release:        14%{?dist}
Epoch:          1
Summary:        Themeable window decorator and compositing manager for Compiz
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

Requires:       compiz >= %{basever}

# fix rhbz (#1291897)
Obsoletes: compiz-xfce < %{epoch}:%{version}-%{release}
Obsoletes: compiz-lxde < %{epoch}:%{version}-%{release}
%if 0%{?fedora} < 24
Provides:  compiz-xfce = %{epoch}:%{version}-%{release}
Provides:  compiz-lxde = %{epoch}:%{version}-%{release}
%endif

BuildRequires:  compiz-devel >= %{basever}
BuildRequires:  libwnck3-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext-devel
BuildRequires:  libXres-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires: make

%description
Emerald is themeable window decorator and compositing
manager for Compiz.

%package devel
Summary: Development files for emerald
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
The emerald-devel package provides development files
for emerald, the themeable window decorator for Compiz.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}

%build
./autogen.sh
%configure \
    --with-gtk=3.0 \
    --disable-mime-update

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f

rm -f %{buildroot}%{_datadir}/applications/compiz-*-emerald.desktop
rm -f %{buildroot}%{_datadir}/applications/emerald-decorator.desktop
rm -f %{buildroot}%{_bindir}/compiz-*-emerald

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/emerald-theme-manager.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/*
%dir %{_libdir}/emerald
%dir %{_libdir}/emerald/engines
%{_libdir}/emerald/engines/*.so
%{_libdir}/libemeraldengine.so.*
%{_datadir}/applications/emerald-theme-manager.desktop
%dir %{_datadir}/emerald
%dir %{_datadir}/emerald/theme
%{_datadir}/emerald/theme/*
%{_datadir}/emerald/settings.ini
%{_datadir}/mime-info/emerald.mime
%{_datadir}/mime/packages/emerald.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/*.1.*

%files devel
%{_includedir}/emerald/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libemeraldengine.so

%changelog
%autochangelog
