%global source0_hash fc6fd9640eb03b0fa1e2ebd40455b87e39119e99b78212d8f3b1441de3a7a8bc

%global         upstream_name   ale
%global         vimfiles        %{_datadir}/vim/vimfiles
%global         nvimfiles       %{_datadir}/nvim/runtime

Name:           vim-%upstream_name
Version:        4.0.0
Release:        3%{?dist}
Summary:        Asynchronous Vim Lint Engine
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            https://github.com/dense-analysis/ale
Source0:        https://github.com/dense-analysis/%upstream_name/archive/v%version/%upstream_name-%version.tar.gz

BuildArch:      noarch

Requires:       (vim-enhanced or vim-X11)

%define desc(n:) \
ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking \
and semantic errors) in %{-n*} while you edit your text files, \
and acts as a Vim Language Server Protocol client. \
\
ALE makes use of NeoVim and Vim job control functions and timers to run \
linters on the contents of text buffers and return errors as text is changed \
in %{-n*}.  This allows for displaying warnings and errors in files being \
edited in %{-n*} before files have been saved back to a filesystem. \
\
In other words, this plugin allows you to lint while you type.

%description
%desc -n Vim

%package -n neovim-%upstream_name
Requires:       neovim
Summary:        Asynchronous NeoVim Lint Engine

%description -n neovim-%upstream_name
%desc -n NeoVim

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %upstream_name-%version

%install
for dest in %vimfiles %nvimfiles; do
mkdir -p %buildroot"$dest"
cp -r ale_linters %buildroot"$dest"
cp -r autoload %buildroot"$dest"
cp -r doc %buildroot"$dest"
cp -r ftplugin %buildroot"$dest"
cp -r plugin %buildroot"$dest"
cp -r rplugin %buildroot"$dest"
cp -r syntax %buildroot"$dest"
cp -r lua %buildroot"$dest"
done

# Lua files for neovim only

%define ale_files(d:) \
%license LICENSE \
%doc %{-d*}/doc/* \
%{-d*}/ale_linters \
%{-d*}/autoload/* \
%{-d*}/rplugin \
%{-d*}/plugin/* \
%{-d*}/lua/* \
%{-d*}/ftplugin/* \
%{-d*}/syntax/* \

%files
%ale_files -d %vimfiles

%files -n neovim-%upstream_name
%ale_files -d %nvimfiles

%changelog
%autochangelog
