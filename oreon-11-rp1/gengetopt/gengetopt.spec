%global source0_hash 3b9def48422bd45f78af95936200b7f9287369a3db76c4907c42fe10f4922ab6
Name:             gengetopt
Version:          2.23.1
Release:        1%{?dist}
Summary:        Tool to write command line option parsing code for C programs
License:          GPL-3.0-or-later
URL:              http://www.gnu.org/software/gengetopt/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%ifarch %{valgrind_arches}
%endif
Provides:         bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
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
make
%install
%make_install INSTALL="%{__install} -p"
rm -frv %{buildroot}%{_infodir}/dir
rm -frv %{buildroot}%{_docdir}/%{name}
mkdir ./examples
pushd ./doc
  cp -p README.example ../examples
  cp -p main1.cc sample1.ggo ../examples
  cp -p main2.c sample2.ggo ../examples
popd
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
