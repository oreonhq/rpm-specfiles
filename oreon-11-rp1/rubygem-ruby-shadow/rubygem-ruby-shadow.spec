%global source0_hash b0396a82c71fe9dd4539b6706041f41ad96e8784d2d1bffeeb8033b6ef1fe6ac

%global         gem_name ruby-shadow

Name:           rubygem-%{gem_name}
Version:        2.5.1
Release:        15%{?dist}
Summary:        Ruby shadow password module
License:        LicenseRef-Fedora-UltraPermissive OR Unlicense
URL:            https://github.com/apalmblad/ruby-shadow
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://raw.githubusercontent.com/apalmblad/ruby-shadow/master/test/basic_test.rb
# https://github.com/apalmblad/ruby-shadow/pull/29
# Ruby3.2 completely removes taintedness function
Patch0:         ruby-shadow-2.5.1-taintedness-ruby32-removal.patch
# https://github.com/apalmblad/ruby-shadow/pull/31
# Ruby3.2 mkmf CONFIG uses reference for other variables yet more
Patch1:         ruby-shadow-2.5.1-extconf-ruby32-fix.patch
Patch2:         ruby-shadow-2.5.1-cflags.patch
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
Obsoletes:      ruby-shadow < 1.4.1-36
Provides:       ruby-shadow = %{version}-%{release}
Provides:       ruby(shadow) = %{version}
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

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# two identical so files confuses rpmbuild
find %{buildroot}%{gem_dir}/ -name \*.so -delete

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
cp %{SOURCE1} .%{gem_instdir}
pushd .%{gem_instdir}
if [ $(id -u) = 0 ]; then
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)'
else
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)' || :
fi
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/*
%doc %{gem_instdir}/HISTORY
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.euc

%changelog
%autochangelog
