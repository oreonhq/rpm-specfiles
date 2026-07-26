%global source0_hash d2dce8e3f04e195c786f7049ce0b5990124ffd58488b509467d59bb0bcac4f0c

Name:		topgit
Version:	0.19.14
Release:	3%{?dist}
Summary:	A different patch queue manager
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://mackyle.github.io/topgit/
Source0:	https://github.com/mackyle/topgit/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	%{_bindir}/rst2html
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(App::Prove)
BuildRequires:	git sed gawk diffutils findutils perl-interpreter
Requires:	git sed gawk diffutils findutils perl-interpreter

%description
TopGit aims to make handling of large amount of interdependent topic
branches easier. In fact, it is designed especially for the case when
you maintain a queue of third-party patches on top of another (perhaps
Git-controlled) project and want to easily organize, maintain and
submit them - TopGit achieves that by keeping a separate topic branch
for each patch and providing few tools to maintain the branches.

This version of TopGit contains everything from its parent (including
the parent’s new location) and then it’s Patched Really Overall (PRO)
to fix a number of bugs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make %{?_smp_mflags} all html prefix=%{_prefix} V=1

%install
make install install-html prefix=%{_prefix} DESTDIR=%{buildroot} V=1
install -m 0644 -D -p contrib/tg-completion.bash \
  %{buildroot}%{_sysconfdir}/bash_completion.d/tg-completion.bash

# fix HTML installation directory
mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/*.html %{buildroot}%{_pkgdocdir}

%check
make DEFAULT_TEST_TARGET=prove \
     TESTLIB_PROVE_OPTS="%{?_smp_mflags} --timer" \
     prefix=%{_prefix} test || :

%files
%doc README
%license COPYING
%{_pkgdocdir}
%{_bindir}/tg
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%if !(0%{?fedora} || 0%{?rhel} >= 7)
%dir %{_sysconfdir}/bash_completion.d/
%endif
%{_sysconfdir}/bash_completion.d/tg-completion.bash

%changelog
%autochangelog
