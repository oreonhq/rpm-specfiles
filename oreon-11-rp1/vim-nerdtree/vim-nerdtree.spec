%global source0_hash 1fd6a7e9ca3427c82dcf15657fff6c3e090e5d9605a7c3b382fc22c0bb3834e9

Name:           vim-nerdtree
Version:        7.1.3
Release:        3%{?dist}
Summary:        A tree explorer plugin for the editor Vim

License:        WTFPL
URL:            https://github.com/preservim/nerdtree
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Added metainfo per 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/#_metainfo_xml_file_creation
Source1:        vim-nerdtree.metainfo.xml

Requires:       vim-common

# TODO: These are needed by %%transfiletrigger provided by vim-commons,
# not sure how to get rid of these ATM :/
Requires(post): vim
Requires(postun): vim

# Needed for AppData check.
BuildRequires:  libappstream-glib

# Defines %%vimfiles_root
BuildRequires:  vim-filesystem
BuildArch:      noarch

%description
The NERD tree allows you to explore your filesystem and to open files and
directories. It presents the filesystem to you in the form of a tree which
you manipulate with the keyboard and/or mouse. It also allows you
to perform simple filesystem operations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n nerdtree-%{version}

%build
# Nothing to build. We are just copying files to the filesystem

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {autoload,doc,lib,nerdtree_plugin,plugin,syntax} %{buildroot}%{vimfiles_root}

# Install AppData.
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}

%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%doc CHANGELOG.md
%license LICENCE
%doc README.markdown
%doc %{vimfiles_root}/doc/NERDTree.txt
%{vimfiles_root}/autoload/nerdtree
%{vimfiles_root}/autoload/nerdtree.vim
%dir %{vimfiles_root}/lib
%{vimfiles_root}/lib/nerdtree
%{vimfiles_root}/nerdtree_plugin/
%{vimfiles_root}/plugin/NERD_tree.vim
%{vimfiles_root}/syntax/nerdtree.vim
%{_metainfodir}/vim-nerdtree.metainfo.xml

%changelog
%autochangelog
