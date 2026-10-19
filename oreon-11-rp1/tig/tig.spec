%global source0_hash 5adeabdcd93aa0423d618da8b878b53482bef6e0e9e1fe224acc0f18031fe91e
%global bash_completion_dir %(pkg-config --variable=completionsdir bash-completion || echo /etc/bash_completion.d)/
Name:           tig
Version:        2.6.1
Release:        1%{?dist}
Summary:        Text-mode interface for the git revision control system
License:        GPL-2.0-or-later
URL:            https://jonas.github.io/tig/
Source0:        https://github.com/jonas/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Requires:       git-core
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xmlto
# /oreon:deps
%description
Tig is a repository browser for the git revision control system that
additionally can act as a pager for output from various git commands.

When browsing repositories, it uses the underlying git commands to present the
user with various views, such as summarized revision log and showing the commit
with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build all doc-man doc-html
sed -i -e 's/\r//' *.html
sed -i '/^#!bash/,+1 d' contrib/%{name}-completion.bash
%install
%make_install install-doc-man
install -Dpm 644 contrib/%{name}-completion.bash %{buildroot}%{bash_completion_dir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
