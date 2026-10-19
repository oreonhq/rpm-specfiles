%global source0_hash 8321627b55b6c7877f6a43fcc6f9f846a94b1476a081a035465f7a78d3499ab8
Summary:        Analyzes C files charting control flow within the program
Name:          cflow
Version:       1.8
Release:        3%{?dist}
License:       GPL-2.0-or-later
URL:           http://www.gnu.org/software/cflow/
Source0:        http://ftp.gnu.org/gnu/cflow/cflow-%{version}.tar.bz2
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
GNU cflow analyzes a collection of C source files and prints a graph,
charting control flow within the program.

GNU cflow is able to produce both direct and inverted flowgraphs for C
sources. Optionally a cross-reference listing can be generated. Two
output formats are implemented: POSIX and GNU (extended).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
