%global source0_hash 5c43e96720654df2c6b45412087343f0eac83c1ea697c1c3760d034af9e65a1f

%global _dwz_low_mem_die_limit 0
%global debug_package %{nil}

Name:           reposurgeon
Version:        5.3
Release:        3%{?dist}
Summary:        SCM Repository Manipulation Tool
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/reposurgeon/
Source0:        http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.xz

BuildRequires:  asciidoctor
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xmlto

BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/text/encoding/ianaindex)
BuildRequires:  golang(github.com/emirpasic/gods/sets/linkedhashset)
BuildRequires:  golang(github.com/anmitsu/go-shlex)
BuildRequires:  golang(github.com/kballard/go-shellquote)
BuildRequires:  golang(github.com/ianbruene/go-difflib/difflib)
BuildRequires:  golang(github.com/termie/go-shutil)
BuildRequires:  golang(github.com/xo/terminfo)
BuildRequires:  golang(github.com/pkg/term/termios)
BuildRequires:  golang(gitlab.com/ianbruene/kommandant)
BuildRequires:  golang(gitlab.com/esr/fqme)

# Tests
BuildRequires:  git
BuildRequires:  golint
BuildRequires:  hg
BuildRequires:  ShellCheck
BuildRequires:  subversion

Requires:       emacs-filesystem

%description
Reposurgeon enables risky operations that version-control systems don't want
to let you do, such as editing past comments and metadata and removing
commits. It works with any version control system that can export and import
git fast-import streams, including git, hg, fossil, bzr, CVS and RCS. It can
also read Subversion dump files directly and can thus be used to script 
production of very high-quality conversions from Subversion to any supported
DVCS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Set go build options
sed -i 's/^#GOFLAGS=-gcflags.*/GOFLAGS=-gcflags "-N -l" -ldflags "-B 0x\$\(shell head -c20 \/dev\/urandom|od -An -tx1|tr -d '\'' \\n'\'')"/g' Makefile

%build
export GOPATH=$(pwd):%{gopath}
export GO111MODULE=off

asciidoctor README.adoc NEWS.adoc

%make_build

%install
%make_install prefix=%{_prefix}

install -pDm644 reposurgeon-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/reposurgeon-mode.el

# Use %%doc to install docs.
rm -frv %{buildroot}%{_docdir}

# Strip repobench
rm -f %{buildroot}%{_bindir}/repobench
rm -f %{buildroot}%{_mandir}/man1/repobench.1*

%check
export GOPATH=$(pwd):%{gopath}
export GO111MODULE=off

# Disable go vet for newer Go versions
sed -i 's/go test /go test -vet=off /g' Makefile

make check

%files
%doc *.html oops.svg
%license COPYING
%{_bindir}/%{name}
%{_bindir}/repocutter
%{_bindir}/repomapper
%{_bindir}/repotool
%{_datadir}/emacs/site-lisp/reposurgeon-mode.el
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/repocutter.1*
%{_mandir}/man1/repomapper.1*
%{_mandir}/man1/repotool.1*

%changelog
%autochangelog
