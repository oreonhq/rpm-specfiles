Name:           libpinyin
Version:        2.11.91
Release:        2%{?dist}
Summary:        Library to deal with pinyin

License:        GPL-3.0-or-later
URL:            https://github.com/libpinyin/libpinyin
Source0:        http://downloads.sourceforge.net/libpinyin/libpinyin/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  kyotocabinet-devel, glib2-devel
BuildRequires:  make
Requires:       %{name}-data%{?_isa} = %{version}-%{release}

%description
The libpinyin project aims to provide the algorithms core
for intelligent sentence-based Chinese pinyin input methods.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libzhuyin = %{version}-%{release}
Provides:       libzhuyin-devel = %{version}-%{release}
Obsoletes:      libzhuyin-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}

%description data
The %{name}-data package contains data files.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools.

%package -n     libzhuyin
Summary:        Library to deal with zhuyin
Requires:       %{name} = %{version}-%{release}

%description -n libzhuyin
The libzhuyin package contains libzhuyin compatibility library.


%prep
%setup -q

%build
%configure --disable-static \
           --with-dbm=KyotoCabinet \
           --enable-libzhuyin
%make_build

%check
make check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING README
%{_libdir}/libpinyin*.so.*
%dir %{_libdir}/libpinyin

%files devel
%doc
%dir %{_includedir}/libpinyin-%{version}
%{_includedir}/libpinyin-%{version}/*
%{_libdir}/libpinyin.so
%{_libdir}/pkgconfig/libpinyin.pc
%{_libdir}/libzhuyin.so
%{_libdir}/pkgconfig/libzhuyin.pc

%files data
%doc
%{_libdir}/libpinyin/data

%files tools
%{_bindir}/gen_binary_files
%{_bindir}/import_interpolation
%{_bindir}/gen_unigram
%{_mandir}/man1/*.1.*

%files -n libzhuyin
%{_libdir}/libzhuyin*.so.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11.91-2
- Import
