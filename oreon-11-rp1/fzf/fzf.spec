# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5529d08897b85ae773695787c811ff9c9eeee32419c8a297fa1dbe586ed0a27e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond_without check

# https://github.com/junegunn/fzf
%global goipath         github.com/junegunn/fzf
%global gourl           https://github.com/junegunn/fzf
%global gobuilddir      %{_builddir}/fzf-%{version}/_build
Version:        0.74.5

Name:           fzf
Release:        1%{?dist}
Summary:        A command-line fuzzy finder written in Go

License:        MIT
URL:            https://github.com/junegunn/fzf
Source0:        https://github.com/junegunn/fzf/archive/v%{version}/fzf-%{version}.tar.gz
Source1:        README.Oreon

BuildRequires:  golang(github.com/charlievieth/fastwalk) >= 1.0.9
BuildRequires:  golang(github.com/gdamore/tcell/v2) >= 2.7.4
BuildRequires:  golang(github.com/junegunn/go-shellwords)
BuildRequires:  golang(github.com/mattn/go-isatty) >= 0.0.20
BuildRequires:  golang(github.com/rivo/uniseg) >= 0.4.7
BuildRequires:  golang(golang.org/x/sys/unix) >= 0.28
BuildRequires:  golang(golang.org/x/term) >= 0.25
BuildRequires:  go-rpm-macros
BuildRequires:  go-srpm-macros
BuildRequires:  oreon-rpm-macros


%description
fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits,
etc.


%prep
%oreon_sha256
%setup -q
mkdir -p %{gobuilddir}/src/github.com/junegunn
ln -sfn %{_builddir}/fzf-%{version} %{gobuilddir}/src/%{goipath}
cp %{SOURCE1} .


%build
export GO111MODULE=off
export GOPATH="%{gobuilddir}:%{gopath}"
cd %{gobuilddir}/src/%{goipath}
go build -buildmode=pie -ldflags "-linkmode=external -X main.version=%{version} -X main.revision=Oreon" -o %{gobuilddir}/bin/fzf .


%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/fzf bin/fzf-tmux
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/*.1

# Install vim plugin
install -Dpm0644 -t %{buildroot}%{_datadir}/vim/vimfiles/plugin plugin/fzf.vim
install -Dpm0644 -t %{buildroot}%{_datadir}/nvim/site/plugin plugin/fzf.vim

# Install shell completion
# fzf is special, bash completion must be in /etc/bash_completion.d
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -Dpm0644 shell/completion.zsh %{buildroot}%{zsh_completions_dir}/_fzf

# Install shell key bindings (not enabled)
install -Dpm0644 -t %{buildroot}%{_datadir}/fzf/shell shell/key-bindings.*


%if %{with check}
%check
export GO111MODULE=off
export GOPATH="%{gobuilddir}:%{gopath}"
cd %{gobuilddir}/src/%{goipath}
go test ./...
%endif


%files
%license LICENSE
%doc README.md README-VIM.md CHANGELOG.md README.Oreon
%{_bindir}/fzf
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*
%{_datadir}/fzf
%dir %{_datadir}/vim/vimfiles/plugin
%{_datadir}/vim/vimfiles/plugin/fzf.vim
%dir %{_datadir}/nvim/site/plugin
%{_datadir}/nvim/site/plugin/fzf.vim
%{_sysconfdir}/bash_completion.d/fzf
%{zsh_completions_dir}/_fzf


