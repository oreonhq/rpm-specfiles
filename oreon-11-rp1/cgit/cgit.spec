%global source93_hash b6c8374a50073ef09ded9dec45f9489237b4193254c88c2dd1536382e1f96351
%global source92_hash 946a6cf47035f35ed7efa79048c19210925f517527186f695d3a90a00f2df40b
%global source1_hash 3a0755dd1cfab71a24dd96df3498c29cd0acd13b04f3d08bf933e81286db802c
%global source0_hash c40fd71e120783d5e57d822208f3e17333cde2cd4baf3e7c8c75630b68afe12a
%global gitver      2.34.1
%global cachedir    %{_localstatedir}/cache/%{name}
%global filterdir   %{_libexecdir}/%{name}/filters
%global scriptdir   %{_localstatedir}/www/cgi-bin
%global cgitdata    %{_datadir}/%{name}
%global httpdconfd  %{_sysconfdir}/httpd/conf.d
%global gitrepodir  %{_localstatedir}/lib/git
%global gpg_cgit    AB9942E6D4A4CFC3412620A749FC7012A5DE03AE
%global gpg_git     96E07AF25771955980DAD10020D04E5A713660A7
%bcond_with     httpd_filesystem
%global use_perl_interpreter    0
%bcond_without     highlight
%global _package_note_file  %{_builddir}/%{name}-%{version}/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld
Name:           cgit
Version:        1.3.1
Release:        1%{?dist}
Summary:        A fast web interface for git
License:        GPL-2.0-only
URL:            https://git.zx2c4.com/cgit/about/
Source0:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.xz
Source2:        cgitrc
Source3:        README-SELinux.md
Source90:       gpgkey-%{gpg_cgit}.asc
Source91:       gpgkey-%{gpg_git}.asc
Source92:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.asc
Source93:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.sign
Patch0:         0001-use-highlight-3-by-default.patch
Patch1:         https://git.zx2c4.com/cgit/patch/?id=bd6f5683f#/0001-t0107-support-older-and-or-non-GNU-tar.patch
Patch2:         cgit-1.2.3-update-to-git-2.34.1.patch
Provides:       bundled(git) = %gitver
%if %{with highlight}
%endif
%if %{with httpd_filesystem}
Requires:       httpd-filesystem
%endif
Requires:       webserver
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  highlight
BuildRequires:  libcurl-devel
BuildRequires:  lua-devel
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-interpreter
BuildRequires:  strace
BuildRequires:  tidy
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  zstd
# /oreon:deps
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
%oreon_autofiles main

%check

%__make %{?_smp_mflags} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
