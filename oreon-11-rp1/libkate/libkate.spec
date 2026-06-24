%global source0_hash none

%if 0%{?fedora} || 0%{?rhel} >= 8
%global _without_python2 1
%endif

Name:           libkate
Version:        0.4.1
Release:        35%{?dist}
Summary:        Libraries to handle the Kate bitstream format

License:        BSD-3-Clause
URL:            https://gitlab.xiph.org/xiph/kate
Source0:        http://libkate.googlecode.com/files/libkate-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%if 0%{!?_without_python2}
BuildRequires:  python2-devel
%endif
BuildRequires:  libogg-devel
BuildRequires:  liboggz
BuildRequires:  libpng-devel
BuildRequires:  bison
BuildRequires:  flex
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  doxygen
 

%description
This is libkate, the reference implementation of a codec for the Kate bitstream
format.
Kate is a karaoke and text codec meant for encapsulation in an Ogg container.
It can carry text, images, and animate them.

Kate is meant to be used for karaoke alongside audio/video streams (typically
Vorbis and Theora), movie subtitles, song lyrics, and anything that needs text
data at arbitrary time intervals.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libogg-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package utils
Summary:        Encoder/Decoder utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liboggz

%description utils
The %{name}-utils package contains the katedec/kateenc binaries for %{name}.

%package docs
Summary:        Documentation for %{name}

BuildArch:      noarch

%description docs
The %{name}-docs package contains the docs for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# We regenerate theses files at built step
rm tools/kate_parser.{c,h}
rm tools/kate_lexer.c


%build
%if 0%{!?_without_python2}
export PYTHON=python2
%else
export PYTHON=:
%endif
%configure --disable-static

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%if 0%{!?_without_python2}
export PYTHON=python2
%else
export PYTHON=:
%endif
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Fix for header timestramps
touch -r %{buildroot}%{_includedir}/kate/kate_config.h \
 %{buildroot}%{_includedir}/kate/kate.h

%if 0%{?_without_python2}
rm -rf %{buildroot}%{_mandir}/man1/KateDJ.1*
%endif


%check
make check


%files
%exclude %{_docdir}/libkate/html
%doc %{_docdir}/libkate
%{_libdir}/*.so.*

%files devel
%doc examples/
%{_includedir}/kate/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files utils
%if 0%{!?_without_python2}
%{python2_sitelib}/kdj/
%{_bindir}/KateDJ
%{_mandir}/man1/KateDJ.*
%endif
%{_bindir}/katalyzer
%{_bindir}/katedec
%{_bindir}/kateenc
%{_mandir}/man1/katalyzer.*
%{_mandir}/man1/katedec.*
%{_mandir}/man1/kateenc.*

%files docs
%doc %{_docdir}/libkate/html


%changelog
%autochangelog

