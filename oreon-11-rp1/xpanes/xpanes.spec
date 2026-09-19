%global source0_hash d5253a13ffc7a63134c62847d23951972b75bd01b333f6c02449b1cd1e502030

Name:           xpanes
Version:        4.2.0
Release:        %autorelease
Summary:        Awesome tmux-based terminal divider
License:        MIT
URL:            https://github.com/greymd/tmux-xpanes
Source0:        %{url}/archive/v%{version}/tmux-xpanes-%{version}.tar.gz
BuildArch:      noarch

Requires:       tmux
Provides:       tmux-xpanes = %{version}-%{release}

%description
Xpanes is the ultimate terminal divider powered by tmux.  It has the following
features:

- Split tmux window into multiple panes
- Construct command lines & execute them on the panes
- Runnable from outside of tmux session
- Runnable from inside of tmux session
- Record operation log
- Flexible layout arrangement for panes
- Select layout presets
- Set columns or rows as you like
- Display pane title on each pane
- Generate command lines from standard input (Pipe mode)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n tmux-xpanes-%{version}

%install
install -D -p -m 0755 bin/xpanes %{buildroot}%{_bindir}/xpanes
install -D -p -m 0644 man/xpanes.1 %{buildroot}%{_mandir}/man1/xpanes.1
install -D -p -m 0644 completion/zsh/_xpanes %{buildroot}%{zsh_completions_dir}/_xpanes
ln -s xpanes %{buildroot}%{_bindir}/tmux-xpanes
ln -s xpanes.1 %{buildroot}%{_mandir}/man1/tmux-xpanes.1
ln -s _xpanes %{buildroot}%{zsh_completions_dir}/_tmux-xpanes

%files
%license LICENSE
%doc README.md
%{_bindir}/xpanes
%{_bindir}/tmux-xpanes
%{_mandir}/man1/xpanes.1*
%{_mandir}/man1/tmux-xpanes.1*
%{zsh_completions_dir}/_xpanes
%{zsh_completions_dir}/_tmux-xpanes

%changelog
%autochangelog
