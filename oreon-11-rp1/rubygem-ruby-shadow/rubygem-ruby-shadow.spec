%global source1_hash f0b0b403de277717e273464063fb59acbd4d6b26bf61f11320c41b0114d1a954
%global source0_hash b0396a82c71fe9dd4539b6706041f41ad96e8784d2d1bffeeb8033b6ef1fe6ac
%global         gem_name ruby-shadow
Name:           rubygem-%{gem_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Ruby shadow password module
License:        LicenseRef-Fedora-UltraPermissive OR Unlicense
URL:            https://github.com/apalmblad/ruby-shadow
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://raw.githubusercontent.com/apalmblad/ruby-shadow/master/test/basic_test.rb
Patch0:         ruby-shadow-2.5.1-taintedness-ruby32-removal.patch
Patch1:         ruby-shadow-2.5.1-extconf-ruby32-fix.patch
Patch2:         ruby-shadow-2.5.1-cflags.patch
Obsoletes:      ruby-shadow < 1.4.1-36
Provides:       ruby-shadow = %{version}-%{release}
Provides:       ruby(shadow) = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This module provides access to shadow passwords on Linux and Solaris.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n  %{gem_name}-%{version}
cp %{SOURCE1} .

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror=implicit-function-declaration'"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_dir}/ -name \*.so -delete
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp %{SOURCE1} .%{gem_instdir}
pushd .%{gem_instdir}
if [ $(id -u) = 0 ]; then
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)'
else
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)' || :
fi
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby-shadow-doc -f %{oreon_filedir}/rubygem-ruby-shadow-doc.list

%changelog

%autochangelog
