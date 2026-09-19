%global source0_hash 9cf4727526d988cee62705f29f53c21765838302713ed6e6c0b29ac117c66af5

Name:           jdupes
Version:        1.30.0
Release:        2%{?dist}
Summary:        Duplicate file finder and an enhanced fork of 'fdupes'

License:        MIT
URL:            https://codeberg.org/jbruchon/jdupes
Source0:        https://codeberg.org/jbruchon/jdupes/archive/jdupes-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libjodycode-devel >= 4.0.1

%description
jdupes is a program for identifying and taking actions upon duplicate
files.

A WORD OF WARNING: jdupes IS NOT a drop-in compatible replacement for
fdupes! Do not blindly replace fdupes with jdupes in scripts and
expect everything to work the same way. Option availability and
meanings differ between the two programs. For example, the -I switch
in jdupes means "isolate" and blocks intra-argument matching, while in
fdupes it means "immediately delete files during scanning without
prompting the user."

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
%make_build CFLAGS="%{optflags} -DENABLE_DEDUPE -DHARDEN" PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"

%install
%make_install PREFIX="%{_prefix}" MAN_BASE_DIR="%{_mandir}"

%files
%license LICENSE.txt
%doc CHANGES.txt INSTALL.txt ISSUES.txt README.md README.stupid_dupes
%{_bindir}/jdupes
%{_mandir}/man1/jdupes.1.gz

%changelog
%autochangelog
