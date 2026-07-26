%global source0_hash 5a5f12d2f66bd3629c8bc103ec8ec2301b292e97155d30a9a61884ea414a6da4

# Review bug: https://bugzilla.redhat.com/479723

# Defaults
%global gitver      2.34.1
%global cachedir    %{_localstatedir}/cache/%{name}
%global filterdir   %{_libexecdir}/%{name}/filters
%global scriptdir   %{_localstatedir}/www/cgi-bin
%global cgitdata    %{_datadir}/%{name}
%global httpdconfd  %{_sysconfdir}/httpd/conf.d
%global gitrepodir  %{_localstatedir}/lib/git

# GPG signing key fingerprints
%global gpg_cgit    AB9942E6D4A4CFC3412620A749FC7012A5DE03AE
%global gpg_git     96E07AF25771955980DAD10020D04E5A713660A7

# Settings for Fedora and EL >= 8
%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without  httpd_filesystem
%global use_perl_interpreter    1
%else
%bcond_with     httpd_filesystem
%global use_perl_interpreter    0
%endif

%if 0%{?rhel} >= 8
# The highlight package is only available in BR starting with RHEL10
%bcond_with  highlight
%else
%bcond_without     highlight
%endif

# Set path to the package-notes linker script
%global _package_note_file  %{_builddir}/%{name}-%{version}/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld

Name:           cgit
Version:        1.2.3
Release:        19%{?dist}
Summary:        A fast web interface for git

License:        GPL-2.0-only
URL:            https://git.zx2c4.com/cgit/about/
Source0:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.xz
Source2:        cgitrc
Source3:        README-SELinux.md

# Jason A. Donenfeld's key is used to sign cgit releases.
# https://www.zx2c4.com/keys/AB9942E6D4A4CFC3412620A749FC7012A5DE03AE.asc
Source90:       gpgkey-%{gpg_cgit}.asc

# Junio C Hamano's key is used to sign git releases.  It can be found in the
# junio-gpg-pub tag within git.
#
# (Note that the tagged blob in git contains a version of the key with an
# expired signing subkey.  The subkey expiration has been extended on the
# public keyservers, but the blob in git has not been updated.)
#
# https://git.kernel.org/cgit/git/git.git/tag/?h=junio-gpg-pub
# https://git.kernel.org/cgit/git/git.git/blob/?h=junio-gpg-pub&id=7214aea37915ee2c4f6369eb9dea520aec7d855b
# https://src.fedoraproject.org/rpms/git/raw/master/f/gpgkey-junio.asc
Source91:       gpgkey-%{gpg_git}.asc

# Tarball signatures
Source92:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.asc
Source93:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.sign

# All supported releases use highlight version 3.
Patch0:         0001-use-highlight-3-by-default.patch

# Improve test suite's support for older tar versions
# https://lists.zx2c4.com/pipermail/cgit/2020-August/004513.html
Patch1:         https://git.zx2c4.com/cgit/patch/?id=bd6f5683f#/0001-t0107-support-older-and-or-non-GNU-tar.patch

# Update to current git
#
# This is a compilation of patches Christian Hesse has sent to the cgit list.
# It was created somewhat manually by reviewing the number of patches since the
# last update to git-2.25.1 (14).  Then patch was generated via:
#
# git log --grep=git: --format='%h' --reverse -14 origin/ch/for-jason |
# while read c _; do
#     git format-patch -1 --ignore-submodules --no-signature --stdout $c
# done >~/src/dist/fedora/cgit/cgit-1.2.3-update-to-git-2.34.1.patch
Patch2:         cgit-1.2.3-update-to-git-2.34.1.patch

# Note the bundled git, per the packaging guidelines
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling
Provides:       bundled(git) = %gitver

%if %{with highlight}
BuildRequires:  highlight
%endif

BuildRequires:  asciidoc
%if 0%{?rhel} && 0%{?rhel} < 9
# Require epel-rpm-macros for the %%gpgverify macro on EL-7/EL-8, and
# %%build_cflags / %%build_ldflags on EL-7.
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  zlib-devel

# Test dependencies
BuildRequires:  gettext
BuildRequires:  lzip
%if %{use_perl_interpreter}
BuildRequires:  perl-interpreter
%else
BuildRequires:  perl
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  strace
BuildRequires:  tidy
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zstd

%if %{with httpd_filesystem}
# httpd-filesystem provides the basic apache directory layout
Requires:       httpd-filesystem
%endif
Requires:       webserver

%description
Cgit is a fast web interface for git.  It uses caching to increase performance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify GPG signatures
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE90}' --signature='%{SOURCE92}' --data=-
xz -dc '%{SOURCE1}' | %{gpgverify} --keyring='%{SOURCE91}' --signature='%{SOURCE93}' --data=-

%autosetup -a 1 -S git

# setup the git dir
rm -rf git
mv git-%{gitver} git

# add README.SELinux
cp -p %{SOURCE3} .

# Use the same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
cat << \EOF | tee cgit.conf
V = 1
CFLAGS = %{build_cflags}
LDFLAGS = %{build_ldflags}
CACHE_ROOT = %{cachedir}
CGIT_SCRIPT_PATH = %{scriptdir}
CGIT_SCRIPT_NAME = cgit
CGIT_DATA_PATH = %{cgitdata}
COPYTREE = %{__cp} -rp
INSTALL = %{__install} -p
docdir = %{docdir}
filterdir = %{filterdir}
prefix = %{_prefix}
EOF

# git build flags
cat << \EOF | tee git/config.mak
V = 1
CFLAGS = %{build_cflags}
LDFLAGS = %{build_ldflags}
NO_EXPAT = 1
NO_PERL = 1
NO_PYTHON = 1
NO_TCLTK = 1
EOF

# remove env shebang's from filter scripts
grep -rl '#!.*/env' filters/ | xargs -r sed -Ei 's@^(.+/)env (.+)$@\1\2@'

# remove execute permissions from contrib file
find contrib -type f | xargs -r chmod -x

# default httpd config
cat >httpd.conf <<EOF
Alias /%{name}-data %{cgitdata}
ScriptAlias /%{name} %{scriptdir}/%{name}
<Directory "%{cgitdata}">
    Require all granted
</Directory>
EOF
touch -r README httpd.conf

%build
%make_build all doc-man doc-html

%if %{with highlight}
highlight --print-style --style-outfile=stdout >> cgit.css
%endif

%install
%make_install install install-man
mkdir -p %{buildroot}%{cachedir} %{buildroot}%{gitrepodir}
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/cgitrc
install -Dp -m0644 httpd.conf %{buildroot}%{httpdconfd}/%{name}.conf

%check
%__make %{?_smp_mflags} test

%files
%doc README* contrib *.html
%license COPYING
%config(noreplace) %{_sysconfdir}/cgitrc
%if ! %{with httpd_filesystem}
# own httpd config dirs on systems without httpd-filesystem
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%endif
%config(noreplace) %{httpdconfd}/%{name}.conf
%dir %attr(-,apache,root) %{cachedir}
%{cgitdata}
%{filterdir}
# exclude byte-compiled python files on EL7
%{?el7:%exclude %{filterdir}/*.py[co]}
%{scriptdir}/%{name}
%{_mandir}/man*/*
%dir %{gitrepodir}

%changelog
%autochangelog
