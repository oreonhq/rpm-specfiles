%global source1_hash bee7d2f96844063557b07b43811d81e1fc54563e0da2c36a975dfd432b196a5c
%global source0_hash 26c56c296b38c0695b26fa95f475f1d01704d2d38e73465ca30b0b2f5dc789d3
%bcond_without docs
%bcond_without tests
%global gitexecdir          %{_libexecdir}/git-core
%bcond_with                 linkcheck
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%bcond_with                 perl_modcompat
%else
%bcond_without              perl_modcompat
%endif
%bcond_with                 asciidoctor
%bcond_without              python2
%bcond_with                 python3
%global build_cflags        %{build_cflags} -fPIC -std=gnu99
%global gitweb_httpd_conf   git.conf
%global use_glibc_langpacks 0
%global use_perl_generators 0
%global use_perl_interpreter 0
%bcond_without              cvs
%bcond_without              libsecret
%bcond_without              p4
%{?!bash_completions_dir:%global bash_completions_dir %{_datadir}/bash-completion/completions}
%global _package_note_file  %{_builddir}/%{name}-%{real_version}/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld
Name:           git
Version:        2.56.0
Release:        1%{?dist}
Summary:        Fast Version Control System
License:        BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://git-scm.com/
%global real_version %(echo %{version} | tr '~' '.')
%global rcpath  %(test "%{version}" = "%{real_version}" || echo testing/)
Source0:        https://www.kernel.org/pub/software/scm/%{name}/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/scm/git/%{rcpath}%{name}-%{real_version}.tar.sign
Source2:        gpgkey-junio.asc
Source11:       git.xinetd.in
Source12:       git-gui.desktop
Source13:       gitweb-httpd.conf
Source14:       gitweb.conf.in
Source15:       git@.service.in
Source16:       git.socket
Source99:       print-failed-test-output
Patch0:         git-cvsimport-Ignore-cvsps-2.2b1-Branches-output.patch
Patch1:         0001-t-lib-httpd-try-harder-to-find-a-port-for-apache.patch
Patch2:         0002-t-lib-git-daemon-try-harder-to-find-a-port.patch
Patch3:         0003-t-lib-git-svn-try-harder-to-find-a-port.patch
Patch5:         git-test-apache-davlockdbtype-config.patch
%if %{with docs}
%if %{with asciidoctor}
%else
%endif
%if %{with linkcheck}
%endif
%endif
%if %{with tests}
%if %{with cvs}
%endif
%if %{with python3}
%else
%if %{with python2}
%endif
%endif
%endif
Requires:       git-core = %{version}-%{release}
Requires:       git-core-doc = %{version}-%{release}
%if ! %{defined perl_bootstrap}
Requires:       perl(Term::ReadKey)
%endif
Requires:       perl-Git = %{version}-%{release}
%if %{without cvs}
Obsoletes:      git-cvs < %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{without p4}
Obsoletes:      git-p4 < %{?epoch:%{epoch}:}%{version}-%{release}
%endif
# oreon:deps
BuildRequires:  acl
BuildRequires:  asciidoc
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  cvs
BuildRequires:  cvsps
BuildRequires:  desktop-file-utils
BuildRequires:  diffutils
BuildRequires:  expat-devel
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-utils
BuildRequires:  gnupg2
BuildRequires:  httpd
BuildRequires:  libcurl-devel
BuildRequires:  libsecret-devel
BuildRequires:  make
BuildRequires:  mod_dav_svn
BuildRequires:  openssh-clients
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Carp)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Error)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(filetest)
BuildRequires:  perl(lib)
BuildRequires:  perl-podlators
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  subversion
BuildRequires:  subversion-perl
BuildRequires:  systemd
BuildRequires:  tar
BuildRequires:  tcl
BuildRequires:  time
BuildRequires:  tk
BuildRequires:  xmlto
BuildRequires:  xz
BuildRequires:  zip
BuildRequires:  zlib-devel
BuildRequires:  zstd
# /oreon:deps
%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs common set of tools which are usually using with
small amount of dependencies. To install all git packages, including
tools for integrating with other SCMs, install the git-all meta-package.

%package all
Summary:        Meta-package to pull in all git tools
BuildArch:      noarch
Requires:       git = %{version}-%{release}
%if %{with libsecret}
Requires:       git-credential-libsecret = %{version}-%{release}
%endif
%if %{with cvs}
Requires:       git-cvs = %{version}-%{release}
%endif
Requires:       git-daemon = %{version}-%{release}
Requires:       git-email = %{version}-%{release}
Requires:       git-gui = %{version}-%{release}
%if %{with p4}
Requires:       git-p4 = %{version}-%{release}
%endif
Requires:       git-subtree = %{version}-%{release}
Requires:       git-svn = %{version}-%{release}
Requires:       git-instaweb = %{version}-%{release}
Requires:       gitk = %{version}-%{release}
Requires:       perl-Git = %{version}-%{release}
%if ! %{defined perl_bootstrap}
Requires:       perl(Term::ReadKey)
%endif
%description all
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This is a dummy package which brings in all subpackages.

%package core
Summary:        Core package of git with minimal functionality
Requires:       less
Requires:       openssh-clients
Requires:       zlib >= 1.2
%description core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git-core rpm installs really the core tools with minimal
dependencies. Install git package for common set of tools.
To install all git packages, including tools for integrating with
other SCMs, install the git-all meta-package.

%package core-doc
Summary:        Documentation files for git-core
BuildArch:      noarch
Requires:       git-core = %{version}-%{release}
%description core-doc
Documentation files for git-core package including man pages.

%if %{with libsecret}
%package credential-libsecret
Summary:        Git helper for accessing credentials via libsecret
BuildRequires:  libsecret-devel
Requires:       git = %{version}-%{release}
%description credential-libsecret
%{summary}.
%endif
# endif with libsecret

%if %{with cvs}
%package cvs
Summary:        Git tools for importing CVS repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       cvs
Requires:       cvsps
Requires:       perl(DBD::SQLite)
%description cvs
%{summary}.
%endif
# endif with cvs

%package daemon
Summary:        Git protocol daemon
Requires:       git-core = %{version}-%{release}
%{?systemd_requires}
%description daemon
The git daemon for supporting git:// access to git repositories

%package email
Summary:        Git tools for sending patches via email
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       perl(Authen::SASL)
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(File::Spec::Functions)
Requires:       perl(File::Temp)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Mail::Address)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::QuotedPrint)
Requires:       perl(Net::Domain)
Requires:       perl(Net::SMTP)
Requires:       perl(POSIX)
Requires:       perl(Sys::Hostname)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)
Requires:       perl(Text::ParseWords)
%description email
%{summary}.

%package -n gitk
Summary:        Git repository browser
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       git-gui = %{version}-%{release}
Requires:       tk
%description -n gitk
%{summary}.

%package -n gitweb
Summary:        Simple web interface to git repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}
%description -n gitweb
%{summary}.

%package gui
Summary:        Graphical interface to Git
BuildArch:      noarch
Requires:       gitk = %{version}-%{release}
Requires:       tk >= 8.4
%description gui
%{summary}.

%package instaweb
Summary:        Repository browser in gitweb
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       gitweb = %{version}-%{release}
Requires:       lighttpd
%description instaweb
A simple script to set up gitweb and a web server for browsing the local
repository.

%if %{with p4}
%package p4
Summary:        Git tools for working with Perforce depots
BuildArch:      noarch
%if %{with python3}
BuildRequires:  python3-devel
%else
%if %{with python2}
BuildRequires:  python2-devel
%endif
%endif
Requires:       git = %{version}-%{release}
%description p4
%{summary}.
%endif
# endif with p4

%package -n perl-Git
Summary:        Perl interface to Git
BuildArch:      noarch
Requires:       git = %{version}-%{release}
%if %{with perl_modcompat}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%endif
%description -n perl-Git
%{summary}.

%package -n perl-Git-SVN
Summary:        Perl interface to Git::SVN
BuildArch:      noarch
Requires:       git = %{version}-%{release}
%if %{with perl_modcompat}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%endif
%description -n perl-Git-SVN
%{summary}.

%package subtree
Summary:        Git tools to merge and split repositories
BuildArch:      noarch
Requires:       git-core = %{version}-%{release}
%description subtree
Git subtrees allow subprojects to be included within a subdirectory
of the main project, optionally including the subproject's entire
history.

%package svn
Summary:        Git tools for interacting with Subversion repositories
BuildArch:      noarch
Requires:       git = %{version}-%{release}
Requires:       perl(Digest::MD5)
%if ! %{defined perl_bootstrap}
Requires:       perl(Term::ReadKey)
%endif
Requires:       subversion
%description svn
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Verify GPG signatures
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-

%autosetup -p1 -n %{name}-%{real_version}

# Install print-failed-test-output script
install -p -m 755 %{SOURCE99} print-failed-test-output

# Remove git-archimport
sed -i '/^SCRIPT_PERL += git-archimport\.perl$/d' Makefile
sed -i '/^git-archimport/d' command-list.txt
rm git-archimport.perl Documentation/git-archimport.adoc

%if %{without cvs}
# Remove git-cvs* from command list
sed -i '/^git-cvs/d' command-list.txt
%endif
# endif without cvs

%if %{without p4}
# Remove git-p4 from command list
sed -i '/^git-p4/d' command-list.txt
%endif
# endif without p4

# Use these same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
# Pipe to tee to aid confirmation/verification of settings.
cat << \EOF | tee config.mak
V = 1
CFLAGS = %{build_cflags}
LDFLAGS = %{build_ldflags}
USE_LIBPCRE = 1
ETC_GITCONFIG = %{_sysconfdir}/gitconfig
INSTALL_SYMLINKS = 1
GITWEB_PROJECTROOT = %{_localstatedir}/lib/git
GNU_ROFF = 1
NO_PERL_CPAN_FALLBACKS = 1
%if %{with python3}
PYTHON_PATH = %{__python3}
%else
%if %{with python2}
PYTHON_PATH = %{__python2}
%else
NO_PYTHON = 1
%endif
%endif
%if %{with asciidoctor}
USE_ASCIIDOCTOR = 1
%endif
htmldir = %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
prefix = %{_prefix}
perllibdir = %{perl_vendorlib}
gitwebdir = %{_localstatedir}/www/git

# Test options
DEFAULT_TEST_TARGET = prove
GIT_PROVE_OPTS = --verbose --normalize %{?_smp_mflags} --formatter=TAP::Formatter::File
GIT_TEST_OPTS = -x --verbose-log
EOF

# Filter bogus perl requires
# packed-refs comes from a comment in contrib/hooks/update-paranoid
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(packed-refs\\)
%if ! %{defined perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Term::ReadKey\\)
%endif
# endif ! defined perl_bootstrap

# Exclude sample hook files from automatic dependency detection
%global __requires_exclude_from ^%{_datadir}/git-core/templates/hooks/.*sample$

# Remove Git::LoadCPAN to ensure we use only system perl modules.  This also
# allows the dependencies to be automatically processed by rpm.
rm -rf perl/Git/LoadCPAN{.pm,/}
grep -rlZ '^use Git::LoadCPAN::' | xargs -r0 sed -i 's/Git::LoadCPAN:://g'

# Update gitweb default home link string
sed -i 's@"++GITWEB_HOME_LINK_STR++"@$ENV{"SERVER_NAME"} ? "git://" . $ENV{"SERVER_NAME"} : "projects"@' \
    gitweb/gitweb.perl

# Move contrib/{contacts,subtree} docs to Documentation so they build with the
# proper asciidoc/docbook/xmlto options
mv contrib/{contacts,subtree}/git-*.adoc Documentation/

%build

export TZ=UTC
export SOURCE_DATE_EPOCH=$(date -r version +%%s 2>/dev/null)
%make_build all %{?with_docs:doc}
%make_build -C contrib/contacts/ all
%if %{with libsecret}
%make_build -C contrib/credential/libsecret/
%endif
%make_build -C contrib/credential/netrc/
%make_build -C contrib/diff-highlight/
%make_build -C contrib/subtree/ all
%if %{with python2}
sed -i -e '1s@#! */usr/bin/env python$@#!%{__python2}@' \
    contrib/fast-import/import-zips.py
%else
rm -rf contrib/fast-import/import-zips.py
%endif
%install
%make_install %{?with_docs:install-doc}
%make_install -C contrib/contacts
%if %{with libsecret}
install -pm 755 contrib/credential/libsecret/git-credential-libsecret \
    %{buildroot}%{gitexecdir}
%endif
install -pm 755 contrib/credential/netrc/git-credential-netrc \
    %{buildroot}%{gitexecdir}
mv contrib/credential/netrc .
%make_install -C contrib/subtree
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{gitweb_httpd_conf}
sed "s|@PROJECTROOT@|%{_localstatedir}/lib/git|g" \
    %{SOURCE14} > %{buildroot}%{_sysconfdir}/gitweb.conf
install -Dpm 0755 contrib/diff-highlight/diff-highlight \
    %{buildroot}%{_datadir}/git-core/contrib/diff-highlight
rm -rf contrib/diff-highlight/{Makefile,diff-highlight,*.perl,t}
rm -rf contrib/persistent-https
rm -rf contrib/scalar
rm -rf contrib/subtree/{INSTALL,Makefile,git-subtree*,t}
%if %{without cvs}
find %{buildroot} Documentation \( -type f -o -type l \) \
    \( -name 'git-cvs*' -o -name 'gitcvs*' \) -exec rm -f {} ';'
%endif
%if %{without p4}
find %{buildroot} Documentation -type f -name 'git-p4*' -exec rm -f {} ';'
rm -f %{buildroot}%{gitexecdir}/mergetools/p4merge
%endif
rm -f %{buildroot}%{gitexecdir}/git-remote-testsvn
exclude_re="email|git-(citool|credential-libsecret|cvs|daemon|gui|instaweb|p4|subtree|svn)|gitk|gitweb|p4merge"
(find %{buildroot}{%{_bindir},%{_libexecdir}} -type f -o -type l | grep -vE "$exclude_re" | sed -e s@^%{buildroot}@@) > bin-man-doc-files
(find %{buildroot}{%{_bindir},%{_libexecdir}} -mindepth 1 -type d | grep -vE "$exclude_re" | sed -e 's@^%{buildroot}@%dir @') >> bin-man-doc-files
(find %{buildroot}%{perl_vendorlib} -type f | sed -e s@^%{buildroot}@@) > perl-git-files
(find %{buildroot}%{perl_vendorlib} -mindepth 1 -type d | sed -e 's@^%{buildroot}@%dir @') >> perl-git-files
grep Git/SVN perl-git-files > perl-git-svn-files
sed -i "/Git\/SVN/ d" perl-git-files
%if %{with docs}
(find %{buildroot}%{_mandir} -type f | grep -vE "$exclude_re|Git" | sed -e s@^%{buildroot}@@ -e 's/$/*/' ) >> bin-man-doc-files
%else
rm -rf %{buildroot}%{_mandir}
%endif
mkdir -p %{buildroot}%{_localstatedir}/lib/git
install -Dp -m 0644 %{SOURCE16} %{buildroot}%{_unitdir}/git.socket
perl -p \
    -e "s|\@GITEXECDIR\@|%{gitexecdir}|g;" \
    -e "s|\@BASE_PATH\@|%{_localstatedir}/lib/git|g;" \
    %{SOURCE15} > %{buildroot}%{_unitdir}/git@.service
install -Dpm 644 contrib/completion/git-completion.bash %{buildroot}%{bash_completions_dir}/git
ln -s git %{buildroot}%{bash_completions_dir}/gitk
mkdir -p %{buildroot}%{_datadir}/git-core/contrib/completion
install -pm 644 contrib/completion/git-completion.tcsh \
    %{buildroot}%{_datadir}/git-core/contrib/completion/
mkdir -p %{buildroot}%{_datadir}/git-core/contrib/completion
install -pm 644 contrib/completion/git-prompt.sh \
    %{buildroot}%{_datadir}/git-core/contrib/completion/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE12}
pushd %{buildroot}%{gitexecdir} >/dev/null
if cmp -s git-gui git-citool 2>/dev/null; then
    ln -svf git-gui git-citool
fi
popd >/dev/null
%find_lang %{name} %{name}.lang
cat %{name}.lang >> bin-man-doc-files
chmod -R g-w %{buildroot}
chmod a-x %{buildroot}%{gitexecdir}/git-mergetool--lib
find . -regex '.*/\.\(git\(attributes\|ignore\)\|perlcriticrc\)' -delete
chmod a-x Documentation/technical/api-index.sh
find contrib -type f -print0 | xargs -r0 chmod -x
not_core_re="git-(add--interactive|contacts|credential-netrc|filter-branch|instaweb|request-pull|send-mail)|gitweb"
grep -vE "$not_core_re|%{_mandir}" bin-man-doc-files > bin-files-core
touch man-doc-files-core
%if %{with docs}
grep -vE "$not_core_re" bin-man-doc-files | grep "%{_mandir}" > man-doc-files-core
%endif
grep -E  "$not_core_re" bin-man-doc-files > bin-man-doc-git-files
not_core_doc_re="(git-(cvs|gui|citool|daemon|instaweb|subtree))|p4|svn|email|gitk|gitweb"
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr CODE_OF_CONDUCT.md README.md Documentation/*.adoc Documentation/RelNotes contrib %{buildroot}%{_pkgdocdir}/
rm -rf %{buildroot}%{_pkgdocdir}/contrib/{contacts,credential}/
cp -p gitweb/INSTALL %{buildroot}%{_pkgdocdir}/INSTALL.gitweb
cp -p gitweb/README %{buildroot}%{_pkgdocdir}/README.gitweb
%if %{with docs}
cp -pr Documentation/*.html Documentation/docbook-xsl.css %{buildroot}%{_pkgdocdir}/
cp -pr Documentation/{howto,technical} %{buildroot}%{_pkgdocdir}/
find %{buildroot}%{_pkgdocdir}/{howto,technical} -type f \
    |grep -o "%{_pkgdocdir}.*$" >> man-doc-files-core
%endif
{
    find %{buildroot}%{_pkgdocdir} -type f -maxdepth 1 \
        | grep -o "%{_pkgdocdir}.*$" \
        | grep -vE "$not_core_doc_re"
    find %{buildroot}%{_pkgdocdir}/{contrib,RelNotes} -type f \
        | grep -o "%{_pkgdocdir}.*$"
    find %{buildroot}%{_pkgdocdir} -type d | grep -o "%{_pkgdocdir}.*$" \
        | sed "s/^/\%dir /"
} >> man-doc-files-core
%oreon_autofiles gitk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gitweb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-Git usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-Git-SVN usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without tests}
echo "*** Skipping tests"
exit 0
%endif
%if %{with docs} && %{with linkcheck}
find %{buildroot}%{_pkgdocdir} -name "*.html" -print0 | xargs -r0 linkchecker
%endif
GIT_SKIP_TESTS="t5559"
%ifarch aarch64 %{arm} %{power64}
GIT_SKIP_TESTS="$GIT_SKIP_TESTS t5541.37 t5551.25"
%endif
%if "%{_arch}" == "s390x"
GIT_SKIP_TESTS="$GIT_SKIP_TESTS t8020.16 t8020.19"
%endif
export GIT_SKIP_TESTS
export LANG=en_US.UTF-8
export GIT_TEST_GIT_DAEMON=true
export GIT_TEST_HTTPD=true
export GIT_TEST_SVNSERVE=true
export GIT_TEST_SVN_HTTPD=true
export testdir=$(mktemp -d -p /tmp git-t.XXXX)
sed -i "s@^GIT_TEST_OPTS = .*@& --root=$testdir@" config.mak
touch -r GIT-BUILD-OPTIONS ts
sed -i "s@\(GIT_TEST_OPTS='.*\)'@\1 --root=$testdir'@" GIT-BUILD-OPTIONS
touch -r ts GIT-BUILD-OPTIONS
%__make -C t all || ./print-failed-test-output
mkdir -p contrib/credential
mv netrc contrib/credential/
%make_build -C contrib/credential/netrc/ test || \
%make_build -C contrib/credential/netrc/ testverbose
rmdir --ignore-fail-on-non-empty "$testdir"
%post daemon

%systemd_post git.socket
%preun daemon

%systemd_preun git.socket
%postun daemon

%systemd_postun_with_restart git.socket
%files -f %{oreon_filedir}/main.list
%files -n git-all -f %{oreon_filedir}/git-all.list
%files -n git-core -f %{oreon_filedir}/git-core.list
%files -n git-core-doc -f %{oreon_filedir}/git-core-doc.list
%files -n git-credential-libsecret -f %{oreon_filedir}/git-credential-libsecret.list
%files -n git-cvs -f %{oreon_filedir}/git-cvs.list
%files -n git-daemon -f %{oreon_filedir}/git-daemon.list
%files -n git-email -f %{oreon_filedir}/git-email.list
%files -n gitk -f %{oreon_filedir}/gitk.list
%files -n gitweb -f %{oreon_filedir}/gitweb.list
%files -n git-gui -f %{oreon_filedir}/git-gui.list
%files -n git-instaweb -f %{oreon_filedir}/git-instaweb.list
%files -n git-p4 -f %{oreon_filedir}/git-p4.list
%files -n perl-Git -f %{oreon_filedir}/perl-Git.list
%files -n perl-Git-SVN -f %{oreon_filedir}/perl-Git-SVN.list
%files -n git-subtree -f %{oreon_filedir}/git-subtree.list
%files -n git-svn -f %{oreon_filedir}/git-svn.list

%changelog

%autochangelog
