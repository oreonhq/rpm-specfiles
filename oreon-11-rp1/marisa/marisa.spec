%global source0_hash a3057d0c2da0a9a57f43eb8e07b73715bc5ff053467ee8349844d01da91b5efb

Name:          marisa
Version:       0.3.0
Release:       7%{?dist}
Summary:       Static and spece-efficient trie data structure library

License:       BSD-2-Clause OR LGPL-2.1-or-later
URL:  https://github.com/s-yata/marisa-trie
Source0:        https://github.com/s-yata/marisa-trie/archive/refs/tags/v0.3.0.tar.gz#/marisa-0.3.0.tar.gz
Source1: requirements.txt

Patch0: marisa-fix-python-setup.patch
Patch1: marisa-fix-cmake.patch
Patch2: marisa-fix-cmake-vars.patch

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: python3-devel
BuildRequires: ruby-devel
BuildRequires: chrpath

%generate_buildrequires
%pyproject_buildrequires -N %{SOURCE1}

%description
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
static and space-efficient trie data structure. And libmarisa is a C++
library to provide an implementation of MARISA. Also, the package of
libmarisa contains a set of command line tools for building and
operating a MARISA-based dictionary.

A MARISA-based dictionary supports not only lookup but also reverse
lookup, common prefix search and predictive search.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:       Tools for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%package perl
Summary:       Perl language binding for marisa
Requires:      %{name} = %{version}-%{release}

%description perl
Perl language binding for marisa


%package -n python3-%{name}
Summary:       Python 3 language binding for marisa
Requires:      %{name} = %{version}-%{release}

%description -n python3-%{name}
Python 3 language binding for marisa


%package ruby
Summary: Ruby language binding for marisa
Requires:      %{name} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:      ruby(release)
%else
Requires:      ruby(abi) = 1.9.1
%endif

%description ruby
Ruby language binding for groonga


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-trie-%{version}


%build
%set_build_flags

%cmake -DENABLE_TOOLS=ON -DLIB_INSTALL_DIR=%{_libdir} -DBIN_INSTALL_DIR=%{_bindir}
%cmake_build

# build Perl bindings
pushd bindings/perl
%{__perl} Makefile.PL INC="-I%{_builddir}/%{name}-trie-%{version}/include" LIBS="-L%{_builddir}/%{name}-trie-%{version}/redhat-linux-build -lmarisa" INSTALLDIRS=vendor
%{make_build}
popd

# build Python bindings
# Regenerate Python bindings
%{make_build} --directory=bindings swig-python

pushd bindings/python3
%pyproject_wheel
popd

# build Ruby bindings
# Regenerate ruby bindings
pushd bindings
%{make_build} swig-ruby
popd

pushd bindings/ruby
ruby extconf.rb --with-opt-include="%{_builddir}/%{name}-trie-%{version}/include" --with-opt-lib="%{_builddir}/%{name}-trie-%{version}/redhat-linux-build" --vendor
%{make_build}
popd

%install
%cmake_install

# work around some install issue
chrpath --delete %{buildroot}/%{_bindir}/marisa-*

# install Perl bindings
pushd bindings/perl
%make_install INSTALL="install -p"
# Remove hidden files
rm -f %{buildroot}%{perl_vendorarch}/auto/marisa/.packlist
%{_fixperms} -c %{buildroot}%{perl_vendorarch}/*
popd

# install Python bindings
pushd bindings/python3
%pyproject_install
%pyproject_save_files '_marisa*' marisa
popd

# install Ruby bindings
pushd bindings/ruby
%make_install INSTALL="install -p"
popd

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name 'perllocal.pod' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/sample.pl

%check
pushd bindings/python3
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%pyproject_check_import
popd


%files
%doc docs/style.css AUTHORS README.md docs/readme.en.html
%lang(ja) %doc docs/readme.ja.html
%license COPYING.md
%{_libdir}/libmarisa.so.*

%files devel
%{_includedir}/marisa*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Marisa/Marisa*.cmake

%files tools
%{_bindir}/marisa-benchmark
%{_bindir}/marisa-build
%{_bindir}/marisa-common-prefix-search
%{_bindir}/marisa-dump
%{_bindir}/marisa-lookup
%{_bindir}/marisa-predictive-search
%{_bindir}/marisa-reverse-lookup

%files perl
%{perl_vendorarch}/marisa.pm
%{perl_vendorarch}/auto/marisa
%{perl_vendorarch}/benchmark.pl

%files -n python3-%{name} -f %{pyproject_files}
%exclude %{python3_sitearch}/marisa-0.0.0.dist-info

%files ruby
%{ruby_vendorarchdir}/marisa.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.0-7
- Prepare for Oreon 11 (RP1)
