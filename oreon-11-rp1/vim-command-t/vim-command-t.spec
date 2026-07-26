%global source0_hash 5c63d5b427b09fbae43ed11688d22ec8c4f51a945d19556bba9951c8e74893f6

%global commandt_so_dir %{ruby_vendorarchdir}/command-t

Name: vim-command-t
Version: 5.0.5
Release: 6%{?dist}
Summary: An extremely fast, intuitive mechanism for opening files in VIM
License: BSD-2-Clause
URL: https://github.com/wincent/command-t
Source0: https://github.com/wincent/command-t/archive/%{version}/command-t-%{version}.tar.gz
# Relax the Command-T version checking.
# https://github.com/wincent/command-t/issues/192
Patch0: vim-3.0.2-Check-RUBY_LIB_VERSION-instead-of-RUBY_VERSION.patch
# Use SPDX identifier in the AppStream data.
# https://github.com/wincent/command-t/pull/427
Patch1: vim-command-t-5.0.5-Use-SPDX-identifier-in-AppStream-metadata.patch
# https://github.com/wincent/command-t/commit/5147a93a4b6cdb60cfa0ed1b792de711f44cd7b4
# Ruby3.2 finally removes Fixnum
Patch3: vim-command-t-5.0.3-ruby32-Fixnum-removal.patch
Requires: ruby(release)
# Although command-t does not depend on rubygems directly, the RubyGems are
# required by Ruby, but not always (rhbz#845011). So it is necessary to enforce
# the RubyGems dependency, to fix possile SEGFAULT (rhbz#858135). There is
# unfortunately nothing better to do about it, as long as RPM/YUM does not
# support some conditional requires.
Requires: ruby(rubygems)
Requires: vim-common
BuildRequires: make
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems
BuildRequires: rubygem(ostruct)
BuildRequires: rubygem(rspec) >= 3
BuildRequires: gcc
# Defines %%vimfiles_root
BuildRequires: vim-filesystem
BuildRequires: %{_bindir}/appstream-util

%description
The Command-T plug-in for VIM provides an extremely fast, intuitive mechanism
for opening files with a minimal number of keystrokes. It's named "Command-T"
because it is inspired by the "Go to File" window bound to Command-T
in TextMate.

Files are selected by typing characters that appear in their paths, and are
ordered by an algorithm which knows that characters that appear in certain
locations (for example, immediately after a path separator) should be given
more weight.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n command-t-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 3 -p1

%build
pushd ./ruby/command-t/ext/command-t

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
ruby extconf.rb --vendor
make %{?_smp_mflags}

popd

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -par {autoload,doc,plugin,ruby} %{buildroot}%{vimfiles_root}

mkdir -p %{buildroot}%{commandt_so_dir}
chmod 0755 %{buildroot}%{vimfiles_root}/ruby/command-t/ext/command-t/ext.so
mv %{buildroot}%{vimfiles_root}/ruby/command-t/ext/command-t/ext.so %{buildroot}%{commandt_so_dir}

# Remove all dot files.
find %{buildroot}%{vimfiles_root} -name '.*' -delete

# Install AppData.
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 appstream/vim-command-t.metainfo.xml %{buildroot}%{_metainfodir}

# GVim ID in Fedora was changed by:
# https://src.fedoraproject.org/rpms/vim/pull-request/25
# therefore extend also the new ID.
# TODO: Submit this upstream if it proves to work.
sed -i '/<\/extends>/a <extends>org.vim.Vim</extends>' %{buildroot}%{_metainfodir}/vim-command-t.metainfo.xml

%check
# Get rid of Bundler
sed -i '/Bundler/,/^end$/ s/^/#/' spec/spec_helper.rb

rspec -Iruby spec

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE
%doc README.md
%{commandt_so_dir}
%{vimfiles_root}/autoload/*
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/ext*
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.o
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.h
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.c
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/Makefile
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/mkmf.log
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/depend
%{vimfiles_root}/ruby
%{_metainfodir}/vim-command-t.metainfo.xml

%changelog
%autochangelog
