%global source0_hash 84704f484129f7c6ab6dffb5a7fecaa4cae65b32422e2a4c010c8666810c04b4
Name:		coan
Version:	6.0.1
Release:        39%{?dist}
Summary:        A command line tool for simplifying the pre-processor conditionals in source code
License:	LicenseRef-Callaway-BSD
URL:		http://coan2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz
Patch0:         expression_parser.patch
Patch1:         coan-autoconf-c99.patch
ExcludeArch:	ppc64 s390x
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-Pod-Html
BuildRequires:  perl-podlators
# /oreon:deps
%description
%{name} (formerly sunifdef) is a software engineering tool for analyzing
pre-processor-based configurations of C or C++ source code. Its principal use
is to simplify a body of source code by eliminating any parts that are
redundant with respect to a specified configuration.

%{name} is most useful to developers of constantly evolving products
with large code bases, where pre-processor conditionals are used to
configure the feature sets, APIs or implementations of different
releases. In these environments the code base steadily
accumulates #ifdef-pollution as transient configuration options become
obsolete. %{name} can largely automate the recurrent task of purging
redundant #if-logic from the code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

for i in AUTHORS LICENSE.BSD README ChangeLog ; do
    sed -i -e 's/\r$//' $i
done

%build

export CXXFLAGS="-std=c++14 -Wno-deprecated -Wno-deprecated-declarations -fpermissive $RPM_OPT_FLAGS"
autoreconf -vi
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
