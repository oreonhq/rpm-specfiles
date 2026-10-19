%global source0_hash 0426b808119ad4b7a7095acd538afe6cfc69bd3227842104f086912e8dced8d4
%global release_date "February 2022"
%global shortname ngram
ExcludeArch:    %{ix86}
Name:           opengrm-%{shortname}
Version:        1.3.17
Release:        2%{?dist}
Summary:        Library for making and modifying n-gram language models
License:        Apache-2.0
URL:            http://www.opengrm.org/
Source0:        http://www.openfst.org/twiki/pub/GRM/NGramDownload/%{shortname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  openfst-devel
BuildRequires:  openfst-tools
# /oreon:deps
%description
The OpenGrm NGram library is used for making and modifying n-gram
language models encoded as weighted finite-state transducers (FSTs).  It
makes use of functionality in the OpenFst library to create, access and
manipulate n-gram models.  Operations for counting, smoothing, pruning,
applying, and evaluating models are among those provided.

%package devel
Summary:        Development files for OpenGrm NGram
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gsl-devel%{?_isa}, openfst-devel%{?_isa}
%description devel
This package includes the necessary files to develop systems with the
OpenGrm NGram library.

%package tools
Summary:        Command-line tools for working with n-gram language models
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains command-line tools that give access to OpenGrm
NGram library functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{shortname}-%{version}

%build

%configure CXXFLAGS="%{optflags} -DHAVE_GSL" \
  LIBS="-L%{_libdir}/fst -Wl,-rpath=%{_libdir}/fst -lfst -lgsl -lflexiblas"
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
make %{?_smp_mflags}
chrpath -d src/lib/.libs/libngram.so.*.*.*
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N --version-string=%{version} $f \
    -o %{buildroot}%{_mandir}/man1/$(basename $f).1
done
sed -e '2s/"1" "[[:alpha:]]* [[:digit:]]*"/"1" %{release_date}/' \
    -e 's,/builddir.*%{_bindir}/,,g' \
    -i %{buildroot}%{_mandir}/man1/*.1
sed '/Faster multinomial sampling/a#define HAVE_GSL' \
  %{buildroot}%{_includedir}/ngram/ngram-randgen.h > foo
touch -r %{buildroot}%{_includedir}/ngram/ngram-randgen.h foo
mv -f foo %{buildroot}%{_includedir}/ngram/ngram-randgen.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=$PWD/src/lib/.libs make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n opengrm-ngram-devel -f %{oreon_filedir}/opengrm-ngram-devel.list
%files -n opengrm-ngram-tools -f %{oreon_filedir}/opengrm-ngram-tools.list

%changelog

%autochangelog
