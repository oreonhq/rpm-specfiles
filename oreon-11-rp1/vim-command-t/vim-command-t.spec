%global source0_hash 5c63d5b427b09fbae43ed11688d22ec8c4f51a945d19556bba9951c8e74893f6
%global commandt_so_dir %{ruby_vendorarchdir}/command-t
Name: vim-command-t
Version: 5.0.5
Release:        1%{?dist}
Summary:        An extremely fast, intuitive mechanism for opening files in VIM
License: BSD-2-Clause
URL: https://github.com/wincent/command-t
Source0:        https://github.com/wincent/command-t/archive/%{version}/command-t-%{version}.tar.gz
Patch0: vim-3.0.2-Check-RUBY_LIB_VERSION-instead-of-RUBY_VERSION.patch
Patch1: vim-command-t-5.0.5-Use-SPDX-identifier-in-AppStream-metadata.patch
Patch3: vim-command-t-5.0.3-ruby32-Fixnum-removal.patch
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: vim-common
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems
BuildRequires:  vim-filesystem
# /oreon:deps
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
find %{buildroot}%{vimfiles_root} -name '.*' -delete
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 appstream/vim-command-t.metainfo.xml %{buildroot}%{_metainfodir}
sed -i '/<\/extends>/a <extends>org.vim.Vim</extends>' %{buildroot}%{_metainfodir}/vim-command-t.metainfo.xml
%oreon_autofiles main

%check

sed -i '/Bundler/,/^end$/ s/^/#/' spec/spec_helper.rb
rspec -Iruby spec
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
