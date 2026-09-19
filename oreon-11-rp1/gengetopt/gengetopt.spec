%global source0_hash b941aec9011864978dd7fdeb052b1943535824169d2aa2b0e7eae9ab807584ac

Name:             gengetopt
Version:          2.23
Release:          17%{dist}
Summary:          Tool to write command line option parsing code for C programs
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
URL:              http://www.gnu.org/software/gengetopt/
Source0:          ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gcc
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  texinfo
BuildRequires: make
Provides:         bundled(gnulib)

%description
Gengetopt is a tool to generate C code to parse the command line arguments
argc and argv that are part of every C or C++ program. The generated code uses
the C library function getopt_long to perform the actual command line parsing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Suppress rpmlint error.
chmod 644 ./AUTHORS
chmod 644 ./ChangeLog
chmod 644 ./COPYING
chmod 644 ./LICENSE
chmod 644 ./NEWS
chmod 644 ./README
chmod 644 ./THANKS
chmod 644 ./TODO
chmod 644 ./doc/README.example
chmod 644 ./doc/index.html
chmod 644 ./src/parser.yy
chmod 644 ./src/scanner.ll
find . -name '*.c' -exec chmod 644 {} ';'
find . -name '*.cc' -exec chmod 644 {} ';'
find . -name '*.cpp' -exec chmod 644 {} ';'
find . -name '*.h' -exec chmod 644 {} ';'
find . -name '*.ggo' -exec chmod 644 {} ';'

%build
%configure
# Parallel build doesn't work.
make

%install
%make_install INSTALL="%{__install} -p"
rm -frv %{buildroot}%{_infodir}/dir
# Use %%doc macro to install instead.
rm -frv %{buildroot}%{_docdir}/%{name}

mkdir ./examples
pushd ./doc
  cp -p README.example ../examples
  cp -p main1.cc sample1.ggo ../examples
  cp -p main2.c sample2.ggo ../examples
popd

%check
make check

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/index.html doc/%{name}.html
%doc examples/
%license COPYING LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_infodir}/*.info*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
