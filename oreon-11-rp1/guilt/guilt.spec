%global source0_hash 34fba8e0ac59fb9729170c91e06a90a228a7d9110b13c9b06f6a6ed417aa2711

Name:		guilt
Version:	0.36
Release:	26%{?dist}
Summary:	Scripts to manage quilt-like patches on top of git

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://repo.or.cz/guilt.git
Source:		%{name}-%{version}.tar.gz
Requires:	git, gawk, sed, bash

BuildArch:	noarch
BuildRequires:	asciidoc, xmlto, git-core
BuildRequires: make

Patch0:		guilt-0.36-git-decorate.patch
Patch1:		guilt-0.36-filter-dd.patch
Patch2:		guilt-0.36-fix-regressions-newer-git.patch
Patch3:		guilt-0.36-fix-portability-problem-with-using-find-perm-111.patch

%description
Guilt allows one to use quilt functionality on top of a Git repository.
Changes are maintained as patches which are committed into Git.  Commits can
be removed or reordered, and the underlying patch can be refreshed based on
changes made in the working directory. The patch directory can also be
placed under revision control, so you can have a separate history of changes
made to your patches.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make ASCIIDOC='asciidoc --unsafe' %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/usr
make install-doc PREFIX=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/usr/share/man

%check
make test

%files
%doc COPYING Documentation/HOWTO Documentation/Contributing Documentation/Features
%{_bindir}/guilt
%{_prefix}/lib/*
%{_mandir}/man1/guilt*.1*
%{_mandir}/man7/guilt*.7*

%changelog
%autochangelog
