%global source0_hash 1046857c337f5bd05f6fa482446b5a42a011615105743efbe4efee0970b24bb7
%bcond check 0
%global goipath         github.com/junegunn/fzf
Version:                0.74.4
%gometa
Name:           fzf
Release:        1%{?dist}
Summary:        A command-line fuzzy finder written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        README.Fedora
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits,
etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{SOURCE1} .
%autopatch -p1

%build

export LDFLAGS='-X main.version=%{version} -X main.revision=Fedora '
%gobuild -o %{gobuilddir}/bin/fzf %{goipath}
%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/fzf bin/fzf-tmux
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/*.1
install -Dpm0644 -t %{buildroot}%{_datadir}/vim/vimfiles/plugin plugin/fzf.vim
install -Dpm0644 -t %{buildroot}%{_datadir}/nvim/site/plugin plugin/fzf.vim
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -Dpm0644 shell/completion.zsh %{buildroot}%{zsh_completions_dir}/_fzf
install -Dpm0644 -t %{buildroot}%{_datadir}/fzf/shell shell/key-bindings.*
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
