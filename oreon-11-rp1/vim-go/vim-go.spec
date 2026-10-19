%global source0_hash 4c2b7facf78b20c9186f1070b7acff4cf7cf85fdf55fc255199cfef026bc5803
%global vimfiles_root %{_datadir}/vim/vimfiles
%global appdata_dir %{_datadir}/appdata
%global debug_package %{nil}
Name:           vim-go
Version:        1.29
Release:        1%{?dist}
Summary:        Go development plugin for Vim
License:        LicenseRef-Callaway-BSD 
URL:            https://github.com/fatih/vim-go
Source0:        https://github.com/fatih/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml
ExclusiveArch:  %{?golang_arches}%{!?golang_arches:%{ix86} x86_64 %{arm}}
Requires:       vim-common
Requires(post): vim
Requires(postun): vim
Requires:       golang
# oreon:deps

# /oreon:deps
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
find %{buildroot}%{vimfiles_root} -name .gitignore -o -name .gitkeep -delete
mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
