%global source0_hash 6c790529af9db49d9156ff06301f3a1ee553f751adf044d64054cba95dee8194

%global appdata_dir %{_datadir}/appdata

Name: vim-commentary
Version: 1.3
Release: 20%{?dist}
Summary: Comment and uncomments stuff in Vim using motion as a target
License: Vim
URL: http://www.vim.org/scripts/script.php?script_id=3695
Source0: https://github.com/tpope/vim-commentary/archive/v%{version}/%{name}-%{version}.tar.gz
# Plug-in AppData for Gnome Software.
# https://github.com/tpope/vim-commentary/pull/52
Source1: vim-commentary.metainfo.xml
Requires: vim-common
Requires(post): %{_bindir}/vim
Requires(postun): %{_bindir}/vim
# Needed for AppData check.
BuildRequires: libappstream-glib
# Defines %%vimfiles_root_root
BuildRequires: vim-filesystem
BuildArch: noarch

%description
Comment stuff out. Use gcc to comment out a line (takes a count), gc to
comment out the target of a motion (for example, gcap to comment out a
paragraph), and gc in visual mode to comment out the selection. That's it.

Oh, and it uncomments, too. The above maps actually toggle, and gcgc
uncomments a set of adjacent commented lines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -pr doc plugin %{buildroot}%{vimfiles_root}

# Install AppData.
mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}

%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.metainfo.xml

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
> %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc CONTRIBUTING.markdown README.markdown
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{appdata_dir}/vim-commentary.metainfo.xml

%changelog
%autochangelog
