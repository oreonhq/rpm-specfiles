%global source0_hash a1f537b67ac37319740d747a5eb101f0a327b0c483aecf8030c32eb3a133b07f

Name:		zinnia
Version:	0.07
Release:	8%{?dist}
Summary:	Online handwriting recognition system with machine learning

License:	BSD-3-Clause
URL:		https://github.com/silverhikari/zinnia
Source0:	https://github.com/silverhikari/zinnia/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/silverhikari/%{name}/master/%{name}/tomoe2s.pl
Source2:	Makefile.tomoe
Source3:	requirements.txt
Patch0:		zinnia-0.05-bindings.patch
Patch2:		always-store-data-in-little-endian-format.patch
Patch4:		zinnia-fixes-python-setuptools.patch
Patch5:		zinnia-fixes-divide-by-zero.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	libdb-devel, python3-devel
BuildRequires:	swig
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	tomoe
BuildRequires:	autoconf
BuildRequires:	gnome-common

%description
Zinnia provides a simple, customizable, and portable dynamic OCR
system for hand-written input, based on Support Vector Machines.

Zinnia simply receives user pen strokes as coordinate data and outputs
the best matching characters sorted by SVM confidence. To maintain
portability, it has no rendering functionality. In addition to
recognition, Zinnia provides a training module capable of creating
highly efficient handwriting recognition models.

This package contains the shared libraries.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package 	utils
Summary:	Utils for the zinnia library
Requires:	%{name} = %{version}-%{release}

%description	utils
The %{name}-utils package provides utilities for zinnia library that 
use %{name}.

%package 	doc
Summary:	Documents for the zinnia library
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
The %{name}-doc package provide documents for zinnia library that 
use %{name}.

%package  	perl
Summary:	Perl bindings for %name
Requires:	%{name} = %{version}-%{release}

%description 	perl
This package contains perl bindings for %{name}.

%package 	-n python3-zinnia
Summary:	Python bindings for %{name}
Requires:	%{name} = %{version}-%{release}

%description 	-n python3-zinnia
This package contains python bindings for %{name}.

%package	tomoe-ja
Summary:        Japanese tomoe model file for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-ja
This package contains Japanese tomoe model files for %{name}.

%package	tomoe-zh_CN
Summary:        Simplified Chinese tomoe model file for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-zh_CN
This package contains Simplified Chinese tomoe model files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .bindings
%patch -P2 -p1 -R -b .little-endian
%patch -P4 -p1 -b .python
%patch -P5 -p1 -b .divide-by-zero

find . -type f -name "*.pyc" -exec rm -f {} ';'
cp %{SOURCE1} .
cp %{SOURCE2} .
pushd doc
iconv -f latin1 -t utf8 zinnia.css > zinnia.css.bak 
mv -f zinnia.css.bak zinnia.css
popd

# re-generate zinnia.py and zinnia_wrap.cxx for python 3.x
pushd swig
make python
popd

%generate_buildrequires
%pyproject_buildrequires -N %{SOURCE3}

%build
gnome-autogen.sh
%configure --disable-static --disable-rpath
make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %{?_smp_mflags}
make -f Makefile.tomoe build

pushd perl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
popd

pushd python
%pyproject_wheel
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make -f Makefile.tomoe install DESTDIR=$RPM_BUILD_ROOT

pushd perl
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
popd

pushd python
%pyproject_install
%pyproject_save_files '%{name}*' _%{name}
pushd

#remove something unnecessary
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.bs" -size 0c -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

#change the privilege of some files
chmod 0755 $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/%{name}.so

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%pyproject_check_import

%files
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/zinnia
%{_bindir}/zinnia_convert
%{_bindir}/zinnia_learn

%files doc
%doc doc/*

%files	perl
%{perl_vendorarch}/auto/%{name}/
%{perl_vendorarch}/%{name}.pm

%files	-n python3-zinnia -f %{pyproject_files}
%exclude %{python3_sitearch}/zinnia_python-0.0.0.dist-info

%files tomoe-ja
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-ja.model

%files tomoe-zh_CN
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-zh_CN.model

%changelog
%autochangelog
