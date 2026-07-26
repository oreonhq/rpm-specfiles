%global source0_hash fe468a4372473d85a56f05d55b14f0e0201fde6f9336a1a2322cf79421c84d9a

Name:       pyzy
Version:    0.1.0
Release:    37%{?dist}
Summary:    The Chinese PinYin and Bopomofo conversion library
License:    LGPL-2.1-or-later
URL:        http://code.google.com/p/pyzy
Source0:    http://pyzy.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    http://pyzy.googlecode.com/files/pyzy-database-1.0.0.tar.bz2
Patch0:     pyzy-0.1.0-fixes-compile.patch
Patch1:     pyzy-0.1.0-port-to-python3.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  python3

# both android db and open phrase db are data files for pyzy, either one can be installed to provide pyzy-db.
Requires:   pyzy-db = %{version}-%{release}
Obsoletes:  ibus-pinyin-db-android
Provides:   ibus-pinyin-db-android
Obsoletes:  ibus-pinyin-db-open-phrase
Provides:   ibus-pinyin-db-open-phrase

%description
The Chinese Pinyin and Bopomofo conversion library.

%package    devel
Summary:    Development tools for pyzy
Requires:   %{name} = %{version}-%{release}
Requires:   glib2-devel

%description devel
The pyzy-devel package contains the header files for pyzy.

%package    db-open-phrase
Summary:    The open phrase database for pyzy
BuildArch:  noarch
Provides:   pyzy-db

%description db-open-phrase
The phrase database for pyzy from open-phrase project.

%package    db-android
Summary:    The android phrase database for pyzy
BuildArch:  noarch
Provides:   pyzy-db

%description db-android
The phrase database for pyzy from android project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -p %{SOURCE1} data/db/open-phrase

%build
%configure --disable-static --enable-db-open-phrase
# make -C po update-gmo
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%{_libdir}/lib*.so.*
%{_datadir}/pyzy/phrases.txt
%{_datadir}/pyzy/db/create_index.sql
%dir %{_datadir}/pyzy
%dir %{_datadir}/pyzy/db

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files db-open-phrase
%{_datadir}/pyzy/db/open-phrase.db

%files db-android
%{_datadir}/pyzy/db/android.db

%changelog
%autochangelog
