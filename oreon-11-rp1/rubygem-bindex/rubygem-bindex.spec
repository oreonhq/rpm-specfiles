%global source0_hash 7b1ecc9dc539ed8bccfc8cb4d2732046227b09d6f37582ff12e50a5047ceb17e

# Generated from bindex-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bindex

Name: rubygem-%{gem_name}
Version: 0.8.1
Release: 20%{?dist}
Summary: Bindings for your Ruby exceptions
License: MIT
URL: https://github.com/gsamokovarov/bindex
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test compatibility with Minitest 5.19+.
# https://github.com/gsamokovarov/skiptrace/pull/12
Patch0: rubygem-bindex-0.8.1-Fix-compatibility-with-Minitest-5.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(minitest)

%description
Bindings for your Ruby exceptions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/skiptrace/internal/
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/skiptrace/internal/*.so %{buildroot}%{gem_extdir_mri}/skiptrace/internal/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bindex.gemspec
%exclude %{gem_instdir}/skiptrace.gemspec
%{gem_libdir}
%exclude %{gem_libdir}/skiptrace/internal/*.jar
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
