%global source0_hash fef4ce5675f79840b811e42006063a2f21d1f3cc721c9a6d37e1a123dc6f0c54
%global  basever 0.8.16
Name:           emerald
License:        GPL-2.0-or-later
Version:        0.8.18
Release:        1%{?dist}
Epoch:          1
Summary:        Themeable window decorator and compositing manager for Compiz
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       compiz >= %{basever}
Obsoletes: compiz-xfce < %{epoch}:%{version}-%{release}
Obsoletes: compiz-lxde < %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  compiz-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libXres-devel
BuildRequires:  libtool
BuildRequires:  libwnck3-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/emerald-theme-manager.desktop
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n emerald-devel -f %{oreon_filedir}/emerald-devel.list

%changelog

%autochangelog
