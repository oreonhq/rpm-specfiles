%global source0_hash a3057d0c2da0a9a57f43eb8e07b73715bc5ff053467ee8349844d01da91b5efb
Name:          marisa
Version:       0.3.0
Release:        1%{?dist}
Summary:        Static and spece-efficient trie data structure library
License:       BSD-2-Clause OR LGPL-2.1-or-later
URL:  https://github.com/s-yata/marisa-trie
Source0:        https://github.com/s-yata/marisa-trie/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: requirements.txt
Patch0: marisa-fix-python-setup.patch
Patch1: marisa-fix-cmake.patch
Patch2: marisa-fix-cmake-vars.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-marisa = %{version}-%{release}
# /oreon:deps
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
Requires:      ruby(abi) = 1.9.1
%description ruby
Ruby language binding for groonga

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-trie-%{version}
%oreon_prep
%build

%set_build_flags
%cmake -DENABLE_TOOLS=ON -DLIB_INSTALL_DIR=%{_libdir} -DBIN_INSTALL_DIR=%{_bindir}
%cmake_build
pushd bindings/perl
%{__perl} Makefile.PL INC="-I%{_builddir}/%{name}-trie-%{version}/include" LIBS="-L%{_builddir}/%{name}-trie-%{version}/redhat-linux-build -lmarisa" INSTALLDIRS=vendor
%{make_build}
popd
%{make_build} --directory=bindings swig-python
pushd bindings/python3
%pyproject_wheel
popd
pushd bindings
%{make_build} swig-ruby
popd
pushd bindings/ruby
ruby extconf.rb --with-opt-include="%{_builddir}/%{name}-trie-%{version}/include" --with-opt-lib="%{_builddir}/%{name}-trie-%{version}/redhat-linux-build" --vendor
%{make_build}
popd
%install
%cmake_install
chrpath --delete %{buildroot}/%{_bindir}/marisa-*
pushd bindings/perl
%make_install INSTALL="install -p"
rm -f %{buildroot}%{perl_vendorarch}/auto/marisa/.packlist
%{_fixperms} -c %{buildroot}%{perl_vendorarch}/*
popd
pushd bindings/python3
%pyproject_install
popd
pushd bindings/ruby
%make_install INSTALL="install -p"
popd
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name 'perllocal.pod' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/sample.pl
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/marisa* usr/lib64/python3*/site-packages/marisa* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd bindings/python3
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%pyproject_check_import
popd
%files
%files -n marisa-devel -f %{oreon_filedir}/marisa-devel.list
%files -n marisa-tools -f %{oreon_filedir}/marisa-tools.list
%files -n marisa-perl -f %{oreon_filedir}/marisa-perl.list
%files -n python3-marisa -f %{oreon_filedir}/python3-marisa.list
%files -n marisa-ruby -f %{oreon_filedir}/marisa-ruby.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.0-7
- Prepare for Oreon 11 (RP1)
