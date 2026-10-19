%global source0_hash 5c43e96720654df2c6b45412087343f0eac83c1ea697c1c3760d034af9e65a1f
%global _dwz_low_mem_die_limit 0
%global debug_package %{nil}
Name:           reposurgeon
Version:        5.11
Release:        1%{?dist}
Summary:        SCM Repository Manipulation Tool
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/reposurgeon/
Source0:        http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.xz
Requires:       emacs-filesystem
# oreon:deps
BuildRequires:  ShellCheck
BuildRequires:  asciidoctor
BuildRequires:  git
BuildRequires:  golang
BuildRequires:  golint
BuildRequires:  hg
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  subversion
BuildRequires:  xmlto
# /oreon:deps
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
rm -frv %{buildroot}%{_docdir}
rm -f %{buildroot}%{_bindir}/repobench
rm -f %{buildroot}%{_mandir}/man1/repobench.1*
%oreon_autofiles main

%check

export GOPATH=$(pwd):%{gopath}
export GO111MODULE=off
sed -i 's/go test /go test -vet=off /g' Makefile
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
