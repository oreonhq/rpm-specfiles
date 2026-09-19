%global source0_hash 04a3e6a2a4e99458cdcefc96e9d91643034c8fd8c2260bd147c6eb956e0f87f1

Name:           vim-perl-support
Version:        5.4
Release:        5%{?dist}
Summary:        Perl-IDE for VIM

# according to plugin/perl-support.vim
License:        GPL-2.0-only
URL:            http://www.vim.org/scripts/script.php?script_id=556
VCS:            https://github.com/WolfgangMehner/perl-support
Source0:        %{vcs}/archive/version-%{version}/perl-support-%{version}.tar.gz
Source1:        vim-perl-support.metainfo.xml

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  vim-filesystem

Requires:         vim-enhanced
Requires(post):   vim-enhanced
Requires(postun): vim-enhanced

# optional requirements

# per-line Perl profiler
Requires:         perl(Devel::SmallProf)     
# Powerful feature-rich perl source code profiler
Requires:         perl(Devel::NYTProf)
# "fast" per-line Perl profiler
Requires:         perl(Devel::FastProf)
# Critique Perl source code for best-practices
Requires:         perl(Perl::Critic)         
# Generate Ctags style tags for Perl source code
Requires:         perl(Perl::Tags)           
# Parses and beautifies perl source
Requires:         perl(Perl::Tidy)           

# the following are not yet available in fedora
# Perl debugger using a Tk GUI
#Requires:         perl(Devel::ptkdb)         
# regular expression analyzer
#Requires:         perl(YAPE::Regex::Explain) 

# strip out false provides/requires from codesnippets
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{vimfiles_root}/perl-support/codesnippets
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{vimfiles_root}/perl-support/codesnippets

%description
Perl Support implements a Perl-IDE for Vim/gVim. It is written to considerably
speed up writing code in a consistent style.  This is done by inserting
complete statements, comments, idioms, code snippets, templates, and POD
documentation.  Reading perldoc is integrated.  Syntax checking, running a
script, running perltidy,  running perlcritics, starting a debugger and a
profiler can be done with a keystroke.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n perl-support-version-%{version}

%build
# build is empty

%install
install -m 755 -d %{buildroot}%{vimfiles_root}/perl-support
cp -r autoload %{buildroot}%{vimfiles_root}/autoload
cp -r doc %{buildroot}%{vimfiles_root}/doc
cp -r ftplugin %{buildroot}%{vimfiles_root}/ftplugin
cp -r plugin %{buildroot}%{vimfiles_root}/plugin
cp -r perl-support/codesnippets %{buildroot}%{vimfiles_root}/perl-support/codesnippets
cp -r perl-support/modules/ %{buildroot}%{vimfiles_root}/perl-support/modules
cp -r perl-support/templates %{buildroot}%{vimfiles_root}/perl-support/templates
cp -r perl-support/wordlists/ %{buildroot}%{vimfiles_root}/perl-support/wordlists
install -m 755 -d %{buildroot}%{vimfiles_root}/perl-support/scripts
install -m 755 -p perl-support/scripts/*.{pl,sh} \
    %{buildroot}%{vimfiles_root}/perl-support/scripts

# Install and validate AppData.
mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/vim-perl-support.metainfo.xml

%post
umask 022
cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit
exit 0

%postun
if [ $1 -eq 0 ]; then
   umask 022
   cd %{_datadir}/vim/vimfiles/doc
   >tags
   vim -u NONE -esX -c "helptags ." -c quit
fi
exit 0

%files
%doc perl-support/README.* perl-support/doc/* perl-support/rc
%{vimfiles_root}/perl-support
%{vimfiles_root}/autoload/*
%{vimfiles_root}/doc/*.txt
%{vimfiles_root}/ftplugin/*.vim
%{vimfiles_root}/plugin/perl-support.vim
%{_metainfodir}/vim-perl-support.metainfo.xml

%changelog
%autochangelog
