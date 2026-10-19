%global source0_hash f2bf46d410ba567cc8d01507e94916994e48742722e690dc498fab59f5250132
Name:           moreutils
Version:        0.70
Release:        1%{?dist}
Summary:        Additional unix utilities
License:        GPL-2.0-only
URL:            https://joeyh.name/code/moreutils/
Source0:        https://src.fedoraproject.org/repo/pkgs/moreutils/moreutils-0.70.tar.gz/sha512/7e6623d4ecf50a79d1301f0c63b991f5eb32e4edccb46a99df5c39a7d5cb4d5965fb7d00214afd094f7ac4db311fe49b2a785e7429da99b4324214f0ace5c7d4/moreutils-0.70.tar.gz
Patch1:         0001-dont-overwrite-docbooxsl-path.patch
Requires:       perl(TimeDate)
Requires:       perl(Time::Duration)
Requires:       perl(Time::HiRes)
Requires:       perl(IPC::Run)
# oreon:deps
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook2X
BuildRequires:  gcc
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
# /oreon:deps
%description
 This is a growing collection of the unix tools that nobody thought
 to write thirty years ago.

 So far, it includes the following utilities:
  - chronic: runs a command quietly, unless it fails
  - combine: combine the lines in two files using boolean operations
  - errno: look up errno names and descriptions
  - ifdata: get network interface info without parsing ifconfig output
  - ifne: run a program if the standard input is not empty
  - isutf8: check if a file or standard input is utf-8
  - lckdo: execute a program with a lock held
  - mispipe: pipe two commands, returning the exit status of the first
  - parallel: run multiple jobs at once (contained in moreutils-parallel
              sub package)
  - pee: tee standard input to pipes
  - sponge: soak up standard input and write to a file
  - ts: timestamp standard input
  - vidir: edit a directory in your text editor
  - vipe: insert a text editor into a pipe
  - zrun: automatically uncompress arguments to command

%package parallel
Summary:        Additional unix utility - parallel command
Requires:       %{name} = %{version}-%{release}
Conflicts:      parallel
%description parallel
 This is a growing collection of the unix tools that nobody thought
 to write thirty years ago.

 This is a sub package containing the parallel command only.

  - parallel: run multiple jobs at once

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
# the required dtd's are not where this package expects them to be, let's fix that
DTDFILE=`xmlcatalog /usr/share/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.4//EN" "-//OASIS//DTD DocBook XML V4.3//EN"|grep -v "No entry"|head -n1`
sed -r -i "s|/usr/share/xml/docbook/schema/dtd/4.4/docbookx.dtd|$DTDFILE|" *.docbook
# the docbook2x-man command is different in fedora, let's fix that too
sed -r -i "s|docbook2x-man|db2x_docbook2man|" Makefile
# a slightly different syntax is required here for the man pages to be built successfully
sed -r -i "s| rep=\"repeat\"||" *.docbook
# add path to pdf2man
sed -r -i "s|pod2man|/usr/bin/pod2man|" Makefile
# don't strip bins
sed -r -i "s|install -s|install|" Makefile

%build

%make_build
%check

make check
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n moreutils-parallel -f %{oreon_filedir}/moreutils-parallel.list

%changelog

%autochangelog
