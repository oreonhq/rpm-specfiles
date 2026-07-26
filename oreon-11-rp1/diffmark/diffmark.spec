%global source0_hash f970b23ae1092872c29177f885f25a1076f1383d930acd032934cee339e1c1d7

Name:       diffmark
Version:    0.10
Release:    38%{?dist}
Summary:    XML diff and merge
# COPYING:          diffmark license text
# lib/lcs.hh:       GPL-1.0-or-later OR Artistic-1.0-Perl   (based on Algorithm-Diff)
# lib/xutil.hh:     GPL-1.0-or-later OR Artistic-1.0-Perl   (based on XML-LibXML dom.c)
## Not in any binary package
# aclocal.m4:       FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later WITH Libtool-exception
#                   AND GPL-2.0-or-later WITH Autoconf-exception-generic
# cmd/Makefile.in:  FSFULLRWD
# config.guess:     GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:       GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:        FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# depcomp:          GPL-2.0-or-later WITH Autoconf-exception-generic
# diffmark.test/Makefile.in:        FSFULLRWD
# doc/Makefile.in:  FSFULLRWD
# install-sh:       X11
# lib/Makefile.in:  FSFULLRWD
# ltmain.sh:        GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:      FSFULLRWD
# missing:          GPL-2.0-or-later WITH Autoconf-exception-generic
# testdata/diff/Makefile.in:        FSFULLRWD
# testdata/faildiff/Makefile.in:    FSFULLRWD
# testdata/failmerge/Makefile.in:   FSFULLRWD
# testdata/Makefile.in:             FSFULLRWD
# testdata/merge/Makefile.in:       FSFULLRWD
# testdata/roundup/Makefile.in:     FSFULLRWD
License:    diffmark AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense: %{license} AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic
URL:        http://www.mangrove.cz/%{name}/
Source0:    %{url}%{name}-%{version}.tar.gz
# Remove a superfluous RPATH from the programs
Patch0:     %{name}-0.09-remove_rpath.patch
# Adjust to GCC 11 that defaults to -std=gnu++17 that forbirds non-const
# comparison objects
Patch1:     %{name}-gcc11.patch
# Because of diffmark-0.08-remove_rpath.patch:
# And to update config.sub to support aarch64, bug #925255
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make

%description
This is an XML diff and merge package. It consists of a shared library and
two utilities: dm and dm-merge. 

%package        devel
Summary:        Development files for %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# automake -i -f to support aarch64, bug #925255
libtoolize --force && autoreconf -i -f

%build
%configure --enable-shared --disable-static
%{make_build}

%install
%{make_install}
find "$RPM_BUILD_ROOT" -name '*.la' -delete

%files
%license COPYING
%doc doc/*.html README
%{_bindir}/dm
%{_bindir}/dm-merge
%{_libdir}/libdiffmark.so.1{,.*}

%files devel
%{_includedir}/diffmark
%{_libdir}/libdiffmark.so

%changelog
%autochangelog
