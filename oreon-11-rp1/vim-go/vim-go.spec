%global source0_hash 4c2b7facf78b20c9186f1070b7acff4cf7cf85fdf55fc255199cfef026bc5803

%global vimfiles_root %{_datadir}/vim/vimfiles
%global appdata_dir %{_datadir}/appdata

# do not build debugsource and debuginfo subpackages
%global debug_package %{nil}

Name:           vim-go
Version:        1.29
Release:        1%{?dist}
Summary:        Go development plugin for Vim

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD 
URL:            https://github.com/fatih/vim-go
Source0:        https://github.com/fatih/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

# cannot build as noarch until golang is available on all arches
#BuildArch:      noarch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?golang_arches}%{!?golang_arches:%{ix86} x86_64 %{arm}}

Requires:       vim-common
Requires(post): vim
Requires(postun): vim

Requires:       golang

%description
Go (golang) support for Vim. It comes with predefined sensible settings
(like auto gofmt on save), has auto-complete, snippet support, improved syntax
highlighting, go tool-chain commands, etc...
If needed vim-go installs all necessary binaries for providing seamless Vim
integration with current commands. It's highly customizable and each individual
feature can be disabled/enabled easily.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {autoload,compiler,doc,ftdetect,ftplugin,gosnippets,indent,plugin,rplugin,syntax,templates} \
    %{buildroot}%{vimfiles_root}
# remove version control files
find %{buildroot}%{vimfiles_root} -name .gitignore -o -name .gitkeep -delete

mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}

# up until version 1.22, %%{vimfiles_root}/autoload/go/test-fixtures/fmt/src/imports was a symlink,
# but it changed to a directory in later versions - remove it to avoid conflict
%pretrans -p <lua>
path = rpm.expand('%{vimfiles_root}') .. '/autoload/go/test-fixtures/fmt/src/imports'
st = posix.stat(path)
if st and st.type == 'link' then
    os.remove(path)
end

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%license LICENSE
%doc README.md
%{vimfiles_root}/autoload/*
%{vimfiles_root}/compiler/*
%{vimfiles_root}/doc/*
%{vimfiles_root}/ftdetect/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/gosnippets/*
%{vimfiles_root}/indent/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/rplugin/*
%{vimfiles_root}/syntax/*
%{vimfiles_root}/templates/*
%{appdata_dir}/%{name}.metainfo.xml

%changelog
%autochangelog
