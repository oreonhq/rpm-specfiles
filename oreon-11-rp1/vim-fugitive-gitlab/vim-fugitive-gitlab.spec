%global source0_hash 5c60b632d4a883d39ecdd079e32437a26148c26a56f0cef4a8b0ae295a4b970a

%global revdate     20220701
%global gitrevision b73a8e97de95d26280082abb7f51465a3d3b239e
%global gitrev      %(full=%gitrevision ; echo ${full:0:6} )
%global posttag     %{revdate}git%{gitrev}
%global upstream_n  fugitive-gitlab.vim

Name: vim-fugitive-gitlab
Version: 0~%posttag
Release: 9%{?dist}
Summary: GitLab support for vim-fugitive plugin
License: MIT
BuildArch: noarch

URL: https://github.com/shumphrey/%upstream_n.git
Source0: https://github.com/shumphrey/%upstream_n/archive/%gitrevision/%upstream_n-%gitrevision.tar.gz
Source1: vim-fugitive-gitlab.metainfo.xml

Requires: vim-fugitive
Requires: vim-filesystem

# for appstream-util
BuildRequires: libappstream-glib
BuildRequires: vim-filesystem

%description
GitLab support for vim-fugitive plugin.  Enables :Gbrowse from fugitive.vim to
open GitLab URLs.  Sets up :Git to use hub if installed rather than git (when
available).  In commit messages, GitLab issues, issue URLs, and collaborators
can be omni-completed (<C-X><C-O>, see :help compl-omni).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %upstream_n-%gitrevision

%install
mkdir -p %{buildroot}/%{_metainfodir}

install -p -m 0644 %{SOURCE1} %{buildroot}/%{_metainfodir}

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml

mkdir -p %{buildroot}%{vimfiles_root}/autoload/gitlab
mkdir -p %{buildroot}%{vimfiles_root}/doc
mkdir -p %{buildroot}%{vimfiles_root}/plugin

install -p -m 0644 doc/fugitive-gitlab.txt %{buildroot}%{vimfiles_root}/doc
install -p -m 0644 plugin/gitlab.vim %{buildroot}%{vimfiles_root}/plugin
for filename in api fugitive omnifunc utils; do
    install -p -m 0644 autoload/gitlab/$filename.vim %{buildroot}%{vimfiles_root}/autoload/gitlab
done

%files
%license LICENSE
%doc %{vimfiles_root}/doc/*.txt
%dir %{_metainfodir}
%{_metainfodir}/vim-fugitive-gitlab.metainfo.xml
%{vimfiles_root}/plugin/gitlab.vim
%{vimfiles_root}/autoload/gitlab

%changelog
%autochangelog
