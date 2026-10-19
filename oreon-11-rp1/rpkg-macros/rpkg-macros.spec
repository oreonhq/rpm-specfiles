%global source0_hash 22092227fbd4c2b3f3478e967cae2fdd7d850e690db2ccd56d2989804aae567c
%global libdir %{_prefix}/lib
Name: rpkg-macros
Version: 2.0
Release:        1%{?dist}
Summary:        Set of preproc macros for rpkg utility
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git
Source0:        rpkg-util-macros-28034317.tar.gz
BuildArch: noarch
Requires: bash
Requires: git
Requires: coreutils
Requires: findutils
Requires: rpm-git-tag-sort
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  git
BuildRequires:  preproc
BuildRequires:  rpm-git-tag-sort
# /oreon:deps
%description
Set of preproc macros to be used by rpkg utility. They
are designed to dynamically generate certain parts
of rpm spec files. You can use those macros also without
rpkg by:

   $ cat <file_with_the_macros> | preproc -s /usr/lib/rpkg.macros.d/all.bash -e INPUT_PATH=<file_with_the_macros>

INPUT_PATH env variable is passed to preproc to inform
macros about the input file location. The variable is used
to derive INPUT_DIR_PATH variable which rpkg macros use.

If neither INPUT_PATH nor INPUT_DIR_PATH are specified,
INPUT_PATH will stay empty and INPUT_DIR_PATH will default
to '.' (the current working directory).

Another option to experiment with the macros is to source
/usr/lib/rpkg.macros.d/all.bash into your bash environment
Then you can directly invoke the macros on your command-line
as bash functions. See content in /usr/lib/rpkg.macros.d to
discover available macros.

Please, see man rpkg-macros for more information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -b 0 -q -n rpkg-util-macros

%check

export GIT_CONFIG_GLOBAL=`pwd`/gitconfig
git config --global protocol.file.allow always
git config --global init.defaultBranch master
PATH=bin/:$PATH tests/run
%install
install -d %{buildroot}%{libdir}
install -d %{buildroot}%{libdir}/rpkg.macros.d
cp -ar macros.d/* %{buildroot}%{libdir}/rpkg.macros.d
install -d %{buildroot}%{_bindir}
install -p -m 755 bin/pack_sources %{buildroot}%{_bindir}/pack_sources
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/rpkg-macros.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
