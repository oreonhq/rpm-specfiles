%global source1_hash bdd248c278953122a87b4033a0194e8e281b940540447b61935524253c0f8388
%global source0_hash 4b4314bbf1c2029fdf793637e6c7bb15c1b1730d22be9aa04803c98c5bbc446f
%bcond distrobuild 1
%bcond tests 1
%bcond sfsexp 1
%bcond mutt 1
%bcond vim 1
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global with_emacs28 1
%endif
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global with_emacs29 1
%endif
Name:		notmuch
Version:	0.40
Release:        1%{?dist}
Summary:        System for indexing, searching, and tagging email
License:	GPL-3.0-or-later
URL:		https://notmuchmail.org/
Source0:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz
Source1:	https://notmuchmail.org/releases/notmuch-%{version}.tar.xz.asc
Source2:	gpgkey-7A18807F100A4570C59684207E4E65C8720B706B.gpg
Patch:		0001-test-allow-to-use-full-scan.patch
Patch:		0002-test-use-NOTMUCH_NEW-consistently.patch
Patch:		0003-test-use-NOTMUCH_NEW_OPTIONS-in-atomicity.py.patch
Patch:		0004-test-correct-comparison-order-in-T380.patch
Patch:		0005-test-do-not-pass-T380.1-for-the-wrong-reasons.patch
Patch:		0006-test-reword-T380.2-to-be-clearer.patch
Patch:		0007-test-set-up-the-outcount-for-T380.1.patch
%if %{with sfsexp}
%endif
%if %{with tests}
%if %{with sfsexp}
%endif
%endif
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-notmuch = %{version}-%{release}
# /oreon:deps
%description
Fast system for indexing, searching, and tagging email. Even if you
receive 12000 messages per month or have on the order of millions of
messages that you've been saving for decades, Notmuch will be able to
quickly search all of it.

Notmuch is not much of an email program. It doesn't receive messages
(no POP or IMAP support). It doesn't send messages (no mail composer,
no network code at all). And for what it does do (email search) that
work is provided by an external library, Xapian. So if Notmuch
provides no user interface and Xapian does all the heavy lifting, then
what's left here? Not much.

%package	devel
Summary:	Development libraries and header files for the Notmuch library
Requires:	%{name} = %{version}-%{release}
%description devel
Notmuch-devel contains the development libraries and header files for
Notmuch email program. These libraries and header files are
necessary if you plan to do development using Notmuch.

Install notmuch-devel if you are developing C programs which will use the
Notmuch library. You'll also need to install the notmuch package.

%if %{with sfsexp}
%package	git
Summary:	Manage notmuch tags with git
Requires:	%{name} = %{version}-%{release}
Requires:	git-core
Recommends:	python3-notmuch2
%description git
This package contains a simple tool to save, restore, and synchronize
notmuch tags via git repositories.
%endif

%package -n emacs-notmuch
Summary:	Not much support for Emacs
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	emacs(bin) >= %{_emacs_version}
%description -n emacs-notmuch
%{summary}.

%package -n python3-notmuch2
Summary:	Python3 bindings for notmuch (cffi)
Requires:	%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-notmuch2}
Requires:	python3
Obsoletes:	python-notmuch < 0.39~rc2-1
Obsoletes:	python3-notmuch < 0.39~rc2-1
%description -n python3-notmuch2
%{summary}.

%package -n ruby-notmuch
Summary:	Ruby bindings for notmuch
Requires:	%{name} = %{version}-%{release}
%description -n ruby-notmuch
%{summary}.

%if %{with mutt}
%package	mutt
Summary:	Notmuch (of a) helper for Mutt
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	perl(Digest::SHA)
Requires:	perl(Mail::Box)
Requires:	perl(Mail::Header)
Requires:	perl(Term::ReadLine::Gnu)
%description mutt
notmuch-mutt provide integration among the Mutt mail user agent and
the Notmuch mail indexer.
%endif

%if %{with vim}
%package	vim
Summary:	A Vim plugin for notmuch
Requires:	ruby-%{name} = %{version}-%{release}
Requires:	rubygem-mail
Requires:	vim-enhanced
Requires(post): vim-enhanced
Requires(postun): vim-enhanced
%description vim
notmuch-vim is a Vim plugin that provides a fully usable mail client
interface, utilizing the notmuch framework.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with distrobuild}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
%else
# unversioned dir for git build, no check
%autosetup -n notmuch -p1
%endif
# we build the wheel using pyproject macros instead
sed -i -e '/setup.py build/ d' bindings/Makefile.local

%build

%configure --emacslispdir=%{_emacs_sitelispdir}
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC" notmuch-shared
pushd bindings/python-cffi
%pyproject_wheel
popd
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC"
pushd contrib/notmuch-mutt
make
popd
%install
%make_install
find %{buildroot}%{_libdir} -name *.so* -exec chmod 755 {} \;
%if %{with sfsexp}
install -m0755 notmuch-git nmbug %{buildroot}%{_bindir}/
%endif
pushd bindings/python-cffi
%pyproject_install
popd
pushd bindings/ruby
make install DESTDIR=%{buildroot}
popd
%if %{with mutt}
install -m0755 contrib/notmuch-mutt/notmuch-mutt \
	%{buildroot}%{_bindir}/notmuch-mutt
install -m0644 contrib/notmuch-mutt/notmuch-mutt.1 \
	%{buildroot}%{_mandir}/man1/notmuch-mutt.1
%endif
%if %{with vim}
pushd vim
make install DESTDIR=%{buildroot} prefix="%{_datadir}/vim/vimfiles"
popd
%endif
%if %{without sfsexp}
rm -f %{buildroot}%{_mandir}/man1/nmbug.1*
rm -f %{buildroot}%{_mandir}/man1/notmuch-git.1*
rm -f %{buildroot}%{_infodir}/nmbug.info*
rm -f %{buildroot}%{_infodir}/notmuch-git.info*
%endif
rm -f %{buildroot}/%{_datadir}/applications/mimeinfo.cache
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles emacs-notmuch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-notmuch2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ruby-notmuch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

NOTMUCH_SKIP_TESTS="asan"
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{!?with_sfsexp: git}"
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{?with_emacs29: emacs-tree.14}"
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{!?with_emacs28: emacs-tree.23}"
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS" \
NOTMUCH_TEST_SERIALIZE="yesplease" \
NOTMUCH_TEST_TIMEOUT="10m" \
%{py3_test_envvars} make test V=1 %{?rhel:NOTMUCH_TEST_FULLSCAN=1}
%endif
%if %{with vim}
%post vim

cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit
%postun vim

cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit
%endif
%files
%files -n notmuch-devel -f %{oreon_filedir}/notmuch-devel.list
%files -n notmuch-git -f %{oreon_filedir}/notmuch-git.list
%files -n emacs-notmuch -f %{oreon_filedir}/emacs-notmuch.list
%files -n python3-notmuch2 -f %{oreon_filedir}/python3-notmuch2.list
%files -n ruby-notmuch -f %{oreon_filedir}/ruby-notmuch.list
%files -n notmuch-mutt -f %{oreon_filedir}/notmuch-mutt.list
%files -n notmuch-vim -f %{oreon_filedir}/notmuch-vim.list

%changelog

%autochangelog
