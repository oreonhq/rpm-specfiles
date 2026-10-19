%global source0_hash 34fba8e0ac59fb9729170c91e06a90a228a7d9110b13c9b06f6a6ed417aa2711
Name:		guilt
Version:	0.36
Release:        1%{?dist}
Summary:        Scripts to manage quilt-like patches on top of git
License:	GPL-2.0-only
URL:		http://repo.or.cz/guilt.git
Source0:        %{name}-%{version}.tar.gz
Requires:	git, gawk, sed, bash
BuildArch:	noarch
Patch0:		guilt-0.36-git-decorate.patch
Patch1:		guilt-0.36-filter-dd.patch
Patch2:		guilt-0.36-fix-regressions-newer-git.patch
Patch3:		guilt-0.36-fix-portability-problem-with-using-find-perm-111.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
Guilt allows one to use quilt functionality on top of a Git repository.
Changes are maintained as patches which are committed into Git.  Commits can
be removed or reordered, and the underlying patch can be refreshed based on
changes made in the working directory. The patch directory can also be
placed under revision control, so you can have a separate history of changes
made to your patches.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make ASCIIDOC='asciidoc --unsafe' %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/usr
make install-doc PREFIX=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/usr/share/man
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
